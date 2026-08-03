<#
.SYNOPSIS
    Install Hazel skills from this repository to your machine.

.DESCRIPTION
    Copies skills/* to ~/.claude/skills/, where Claude Code finds them for
    every project on this machine.

    The installed copies are REPLICAS. Never edit them. Authoring happens in
    Hazel-KB/skills/ through a pull request; everyone else pulls and re-runs
    this script.

    A manifest at ~/.claude/.hazel-skills-manifest.json records what was
    installed and its hash, so a locally modified replica is detected and
    reported rather than silently overwritten.

.PARAMETER WhatIf
    Show what would change without writing anything.

.PARAMETER Force
    Overwrite locally modified replicas without prompting.

.EXAMPLE
    .\install-skills.ps1
    .\install-skills.ps1 -WhatIf
    .\install-skills.ps1 -Force
#>

[CmdletBinding(SupportsShouldProcess)]
param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

$RepoRoot    = $PSScriptRoot
$SourceDir   = Join-Path $RepoRoot 'skills'
$TargetDir   = Join-Path $HOME '.claude\skills'
$ManifestPath = Join-Path $HOME '.claude\.hazel-skills-manifest.json'

function Write-Status {
    param([string]$Tag, [string]$Message, [string]$Colour = 'Gray')
    Write-Host ("{0,-9}" -f $Tag) -ForegroundColor $Colour -NoNewline
    Write-Host $Message
}

function Get-FileHashHex {
    param([string]$Path)
    (Get-FileHash -Path $Path -Algorithm SHA256).Hash.ToLower()
}

# ---------------------------------------------------------------------------

if (-not (Test-Path $SourceDir)) {
    Write-Status 'ERROR' "No skills/ directory at $SourceDir" 'Red'
    Write-Host  "          Run this from the root of the Hazel-KB repository."
    exit 1
}

$skillDirs = Get-ChildItem -Path $SourceDir -Directory | Sort-Object Name
if ($skillDirs.Count -eq 0) {
    Write-Status 'ERROR' "skills/ contains no skill directories" 'Red'
    exit 1
}

# Warn about a stale project-level copy that would shadow the replica.
$projectSkills = Join-Path $RepoRoot '.claude\skills'
if (Test-Path $projectSkills) {
    $shadowed = Get-ChildItem -Path $projectSkills -Directory -ErrorAction SilentlyContinue
    if ($shadowed) {
        Write-Status 'WARN' "$projectSkills contains $($shadowed.Count) skill(s)" 'Yellow'
        Write-Host  "          These shadow the installed replicas inside this repo."
        Write-Host  "          Authoring belongs in skills/. Consider removing them.`n"
    }
}

# Load the previous manifest.
$manifest = @{}
if (Test-Path $ManifestPath) {
    try {
        $raw = Get-Content $ManifestPath -Raw | ConvertFrom-Json
        $raw.files.PSObject.Properties | ForEach-Object { $manifest[$_.Name] = $_.Value }
    } catch {
        Write-Status 'WARN' "manifest unreadable, treating all replicas as unknown" 'Yellow'
    }
}

# ---------------------------------------------------------------------------
# Plan
# ---------------------------------------------------------------------------

$plan = @()   # each: RelPath, Source, Target, Action, SourceHash

foreach ($dir in $skillDirs) {
    $files = Get-ChildItem -Path $dir.FullName -File -Recurse
    foreach ($file in $files) {
        $rel        = $file.FullName.Substring($SourceDir.Length).TrimStart('\')
        $target     = Join-Path $TargetDir $rel
        $sourceHash = Get-FileHashHex $file.FullName

        $action = 'install'
        if (Test-Path $target) {
            $targetHash = Get-FileHashHex $target
            $recorded   = $manifest[$rel]

            if ($targetHash -eq $sourceHash) {
                $action = 'current'
            } elseif ($recorded -and $targetHash -ne $recorded) {
                $action = 'modified'     # edited locally since last install
            } else {
                $action = 'update'
            }
        }

        $plan += [pscustomobject]@{
            RelPath    = $rel
            Source     = $file.FullName
            Target     = $target
            Action     = $action
            SourceHash = $sourceHash
        }
    }
}

# ---------------------------------------------------------------------------
# Report and confirm
# ---------------------------------------------------------------------------

$modified = @($plan | Where-Object Action -eq 'modified')
$toWrite  = @($plan | Where-Object { $_.Action -in @('install','update','modified') })
$current  = @($plan | Where-Object Action -eq 'current')

Write-Host ""
Write-Host "Hazel skills" -ForegroundColor Cyan
Write-Host "  from  $SourceDir"
Write-Host "  to    $TargetDir"
Write-Host ""

foreach ($item in $plan | Sort-Object RelPath) {
    switch ($item.Action) {
        'install'  { Write-Status 'INSTALL'  $item.RelPath 'Green' }
        'update'   { Write-Status 'UPDATE'   $item.RelPath 'Cyan' }
        'modified' { Write-Status 'MODIFIED' $item.RelPath 'Yellow' }
        'current'  { Write-Status 'CURRENT'  $item.RelPath 'DarkGray' }
    }
}

if ($modified.Count -gt 0) {
    Write-Host ""
    Write-Status 'WARN' "$($modified.Count) replica(s) were edited locally" 'Yellow'
    Write-Host  "          Replicas are not an authoring location. Any change made"
    Write-Host  "          there exists only on this machine and will be lost."
    Write-Host  "          To keep a change, apply it in Hazel-KB/skills/ and open a PR."
    Write-Host  ""

    if (-not $Force -and -not $WhatIfPreference) {
        $answer = Read-Host "          Overwrite the locally modified replica(s)? [y/N]"
        if ($answer -notmatch '^[Yy]') {
            Write-Host ""
            Write-Status 'ABORT' "nothing was written" 'Red'
            exit 1
        }
    }
}

if ($toWrite.Count -eq 0) {
    Write-Host ""
    Write-Status 'OK' "$($current.Count) file(s) already current — nothing to do" 'Green'
    exit 0
}

# ---------------------------------------------------------------------------
# Write
# ---------------------------------------------------------------------------

$written = 0
foreach ($item in $toWrite) {
    if ($PSCmdlet.ShouldProcess($item.Target, 'Copy skill file')) {
        $parent = Split-Path $item.Target -Parent
        if (-not (Test-Path $parent)) {
            New-Item -ItemType Directory -Path $parent -Force | Out-Null
        }
        Copy-Item -Path $item.Source -Destination $item.Target -Force
        $manifest[$item.RelPath] = $item.SourceHash
        $written++
    }
}

if (-not $WhatIfPreference) {
    $commit = try { (git -C $RepoRoot rev-parse --short HEAD 2>$null) } catch { 'unknown' }
    if (-not $commit) { $commit = 'unknown' }

    $out = [ordered]@{
        installed_at  = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
        source_repo   = $RepoRoot
        source_commit = $commit
        files         = $manifest
    }
    $manifestParent = Split-Path $ManifestPath -Parent
    if (-not (Test-Path $manifestParent)) {
        New-Item -ItemType Directory -Path $manifestParent -Force | Out-Null
    }
    $out | ConvertTo-Json -Depth 4 | Set-Content -Path $ManifestPath -Encoding UTF8

    Write-Host ""
    Write-Status 'DONE' "$written file(s) written · $($skillDirs.Count) skill(s) available" 'Green'
    Write-Host  "          Open any repo in Claude Code and type / to see them."
}
