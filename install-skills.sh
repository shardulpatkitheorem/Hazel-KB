#!/usr/bin/env bash
#
# Install Hazel skills from this repository to your machine.
#
# Copies skills/* to ~/.claude/skills/, where Claude Code finds them for every
# project on this machine.
#
# The installed copies are REPLICAS. Never edit them. Authoring happens in
# Hazel-KB/skills/ through a pull request; everyone else pulls and re-runs this.
#
# A manifest at ~/.claude/.hazel-skills-manifest.json records what was installed
# and its hash, so a locally modified replica is reported rather than silently
# overwritten.
#
# Usage:
#   ./install-skills.sh            install
#   ./install-skills.sh --dry-run  show what would change
#   ./install-skills.sh --force    overwrite local edits without prompting

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$REPO_ROOT/skills"
TARGET_DIR="$HOME/.claude/skills"
MANIFEST="$HOME/.claude/.hazel-skills-manifest.json"

DRY_RUN=0
FORCE=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    --force)   FORCE=1 ;;
    -h|--help) sed -n '3,20p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown option: $arg" >&2; exit 2 ;;
  esac
done

if command -v tput >/dev/null 2>&1 && [ -t 1 ]; then
  GREEN=$(tput setaf 2); CYAN=$(tput setaf 6); YELLOW=$(tput setaf 3)
  RED=$(tput setaf 1);   DIM=$(tput dim);      RESET=$(tput sgr0)
else
  GREEN=""; CYAN=""; YELLOW=""; RED=""; DIM=""; RESET=""
fi

status() { printf "%s%-9s%s%s\n" "$2" "$1" "$RESET" "$3"; }

hash_file() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | cut -d' ' -f1
  else
    shasum -a 256 "$1" | cut -d' ' -f1
  fi
}

recorded_hash() {
  [ -f "$MANIFEST" ] || return 0
  python3 - "$MANIFEST" "$1" <<'PY' 2>/dev/null || true
import json, sys
try:
    with open(sys.argv[1]) as fh:
        print(json.load(fh).get("files", {}).get(sys.argv[2], ""))
except Exception:
    pass
PY
}

# ---------------------------------------------------------------------------

if [ ! -d "$SOURCE_DIR" ]; then
  status "ERROR" "$RED" "No skills/ directory at $SOURCE_DIR"
  echo "          Run this from the root of the Hazel-KB repository."
  exit 1
fi

skill_count=$(find "$SOURCE_DIR" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')
if [ "$skill_count" -eq 0 ]; then
  status "ERROR" "$RED" "skills/ contains no skill directories"
  exit 1
fi

if [ -d "$REPO_ROOT/.claude/skills" ] && \
   [ -n "$(find "$REPO_ROOT/.claude/skills" -mindepth 1 -maxdepth 1 -type d 2>/dev/null)" ]; then
  status "WARN" "$YELLOW" ".claude/skills/ in this repo contains skills"
  echo "          These shadow the installed replicas inside this repo."
  echo "          Authoring belongs in skills/. Consider removing them."
  echo ""
fi

echo ""
printf "%sHazel skills%s\n" "$CYAN" "$RESET"
echo "  from  $SOURCE_DIR"
echo "  to    $TARGET_DIR"
echo ""

# ---------------------------------------------------------------------------
# Plan
# ---------------------------------------------------------------------------

plan_file=$(mktemp)
trap 'rm -f "$plan_file"' EXIT
modified_count=0

while IFS= read -r src; do
  rel="${src#"$SOURCE_DIR"/}"
  tgt="$TARGET_DIR/$rel"
  src_hash=$(hash_file "$src")
  action="install"

  if [ -f "$tgt" ]; then
    tgt_hash=$(hash_file "$tgt")
    rec=$(recorded_hash "$rel")
    if [ "$tgt_hash" = "$src_hash" ]; then
      action="current"
    elif [ -n "$rec" ] && [ "$tgt_hash" != "$rec" ]; then
      action="modified"
      modified_count=$((modified_count + 1))
    else
      action="update"
    fi
  fi

  printf '%s\t%s\t%s\t%s\n' "$action" "$rel" "$src" "$src_hash" >> "$plan_file"

  case "$action" in
    install)  status "INSTALL"  "$GREEN"  "$rel" ;;
    update)   status "UPDATE"   "$CYAN"   "$rel" ;;
    modified) status "MODIFIED" "$YELLOW" "$rel" ;;
    current)  status "CURRENT"  "$DIM"    "$rel" ;;
  esac
done < <(find "$SOURCE_DIR" -type f | sort)

# ---------------------------------------------------------------------------

if [ "$modified_count" -gt 0 ]; then
  echo ""
  status "WARN" "$YELLOW" "$modified_count replica(s) were edited locally"
  echo "          Replicas are not an authoring location. Any change made"
  echo "          there exists only on this machine and will be lost."
  echo "          To keep a change, apply it in Hazel-KB/skills/ and open a PR."
  echo ""
  if [ "$FORCE" -eq 0 ] && [ "$DRY_RUN" -eq 0 ]; then
    printf "          Overwrite the locally modified replica(s)? [y/N] "
    read -r answer
    case "$answer" in
      [Yy]*) ;;
      *) echo ""; status "ABORT" "$RED" "nothing was written"; exit 1 ;;
    esac
  fi
fi

to_write=$(grep -vc '^current' "$plan_file" || true)
if [ "${to_write:-0}" -eq 0 ]; then
  echo ""
  status "OK" "$GREEN" "all files already current — nothing to do"
  exit 0
fi

if [ "$DRY_RUN" -eq 1 ]; then
  echo ""
  status "DRY-RUN" "$CYAN" "$to_write file(s) would be written"
  exit 0
fi

# ---------------------------------------------------------------------------
# Write
# ---------------------------------------------------------------------------

written=0
while IFS=$'\t' read -r action rel src src_hash; do
  [ "$action" = "current" ] && continue
  mkdir -p "$(dirname "$TARGET_DIR/$rel")"
  cp "$src" "$TARGET_DIR/$rel"
  written=$((written + 1))
done < "$plan_file"

commit=$(git -C "$REPO_ROOT" rev-parse --short HEAD 2>/dev/null || echo unknown)

mkdir -p "$(dirname "$MANIFEST")"
python3 - "$MANIFEST" "$plan_file" "$REPO_ROOT" "$commit" <<'PY'
import json, sys, datetime, os
manifest_path, plan_path, repo, commit = sys.argv[1:5]

files = {}
if os.path.exists(manifest_path):
    try:
        with open(manifest_path) as fh:
            files = json.load(fh).get("files", {})
    except Exception:
        files = {}

with open(plan_path) as fh:
    for line in fh:
        action, rel, src, src_hash = line.rstrip("\n").split("\t")
        files[rel] = src_hash

with open(manifest_path, "w") as fh:
    json.dump({
        "installed_at": datetime.datetime.now(datetime.timezone.utc)
                          .strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_repo": repo,
        "source_commit": commit,
        "files": files,
    }, fh, indent=2)
PY

echo ""
status "DONE" "$GREEN" "$written file(s) written · $skill_count skill(s) available"
echo "          Open any repo in Claude Code and type / to see them."
