---
title: "Hazel Onboarding Kick-Off — Part 2"
document_type: "transcript"
source: "meeting"
client: "Hazel"
date: "2026-07-16"
status: "parsed"
version: "1.0"
tags:
  - "onboarding"
  - "kickoff"
  - "requirements"
confidentiality: "client-confidential"
source_file: "../raw/2026-07-16-hazel-onboarding-kickoff-part-2.pdf"
content_sha256: "c07a9bb7fd7a65f9399765e448b8f9389439a105b9b6274e89ec514ac91ce78d"
---

# Hazel Onboarding Kick-Off — Part 2

## Transcript

Theorem Labs on Site – Hazel Onboarding
Kick-Off Pt 2 Transcript
Date: July 16, 2026
Format: In-person | Teams
Duration: 1hr 1m 52s
FortWorth-MuseumPlace-Boardroom 0:03
Yeah.
You see my screen? You good? Yeah, it's up there. It's coming up.
Yeah.
So...
Sing.
In.
Okay, so what I was uh...
Suggesting was.
So, Sandra, this is probably like this kind of stuff is little, so what I understand is, hey,
this is...
Um...
Pizu.
Data Tricks.
K.
Inside that, you are having a, you're hosting one app, okay, which is external facing.
And then your.
Having another app.
And let's say that is internal.
Okay.
So, that's your internal app. OK, now what I what I think we're saying here is, hey,
listen, we need to have a intra.
Intra ID, which is Hazel.
Need a power cord and I have it to hold on.
Hey, right here.
Yeah.
Intra ID, but that this Intra Infrastructure is Hazel specific, correct? This is Hazel
specific database, this is Hazel specific Intra ID. Now, think about member banks over
here, right?
So these are the member banks.
This is member bank one, there is another one, but in addition to that, we also have
Vantage, correct? Yes, so there is a Vantage as a member bank. I mean, it doesn't
care, right? So now, hey, this...
This has its own intro.
Right, so they have to, so you're SSOing everywhere, right? Yes, right. So, so once
you set this up as an SSO framework.
Right, whether you are a member bank or you are any, it doesn't matter. The only
difference is...
This particular app, Shantanu.
This particular app is going to show up. It's also going to get, it's also going to get
available over here, correct, while the other one does not does not, and that's the
external version of it, right?
Makes sense? Yes, yeah. Great. So that's one thought process, but to make this green
app show inside Teams.
I have not figured out.
Do I need to worry about SSO of Hazel?
That I don't know.
Bidding.
Uh...
If there is a Databricks instance, so, so today what we are simply saying is...
Today, we are simply saying, "Hey, for..."
For time being, OK, this particular stuff.
Is going to work on Vantage.
Databricks.
OK, and both of these green.
So both of this green and the blue.
that are over here, we will build over here. Eventually, we will go over here.
And that, so, so that's our short-term, short-term goal to make progress fast. Well,
potentially, but we we were talking about, yeah, maybe just getting this built as a dev
instance inside of Hazel right away. If it is there, it is there, but what I'm saying is like,
hey, today, or since we kind of ended up starting casually on next steps, yeah.
If we have this much level of the detail in the Word document and the PowerPoint.
We can start putting an asset, a real app, and start building the React app. Like, what
did we do? You can deploy it anywhere, right? Yeah, yeah, yeah, yeah. So, for Rafa,
we started building the app, and then we started using Joel to react to it. Hey, what
do you want in this screen?
What do you want in that?
And we, we, we, the spec was earlier, we we did it in an interactive way. Maybe we'll
now write us open spec. Are you guys familiar with open spec dot open spec right
now? Open and open spec is a new standard wherein you.
You write everything in English, you feed it to a copilot or you feed it to a cloud, and
it will code, it will go in a long, long-running iterative cycle and code or it will design
or it will produce wire and so on and so forth. But now you're not talking to it in an
interactive mode.
Because whatever you talk to it in an interactive mode is there in the memory, but it's
not, yeah, well done, so, so you're actually provisioning the specs.
Yeah, there's a popular idea nowadays. It's called spec-driven AI development. You
set the spec and then you set a goal to just wrap it up to, whether it takes 10 hours
or it doesn't take most, depending on the size of the, most things don't take 10
hours, it will be 15, 20 minutes.
So, so we have one hour percent left, yeah, right now.
Obviously, you know, we understand the team at some level, but from tomorrow,
when we are talking about spend.
day-to-day, little more time, and focus on getting few things delivered, right? Plan,
execute, so we know Aaron is gonna drive the daily research. I thought I assumed,
you mentioned, you mentioned, am I am I right, Adam? By driving what? The he will
be the program manager for this.
Or now? Well, actually, and that's Chris, we've joined the call. Okay. Yeah, not
immediately though. So Chris can only dedicate a small amount of time initially. So a
lot of the early setup is going to be just him learning and washing because obviously
still a lot to pick up about Hazel and everything else.
But yes, you know, I think initially, Aaron, you're probably best positioned right now.
And then if we need to find some other assistance or help, then we can do that.
But.
Glad I came to those meetings, yeah, so I think what will help is, yeah, Chris won't be
really fully available, yeah, yeah, no, that makes sense. So, so we have enough
functional input now, publicly available, as well as whatever was discussed yesterday,
casually yesterday formally.
What needs, where it takes a long time is the infrastructure setup. So, and I hope I'm
not coming as being critical over here. So, what our immediate request is, if we can,
so for the three engineers that we have on our side,
Plus, Shantanu and me, if we can quickly get provisioned our dev cloud boxes.
That's the immediate one ask of us of you, and then basically coding assistant setup.
And then third is access to.
Access to the databricks is going on, right? That those are the three.
things that are like a prerequisite for not prerequisite weekends. So this is 1 track. I
would call it as infra.
Infrastructure and maybe Chris stuff can get started now as well. So this is the
infrastructure. The second part is.
Um, the Jerry.
Onboarding journey evolution, right?
Onboarding journey plus UX. I would say.
I think one hour, we should have one, you know, every day we should have one hour
call. That's what I'm thinking. For next seven days when we're talking about
onboarding, yeah, yeah, yeah, because there are a lot of open questions, yeah,
Aaron's going, when am I going to do this? You can do it, and then...
And what we would like to know, like...
Well, and just to make sure too, because I mean, obviously Aaron's got plenty of
other things too. And so if you can't support this, then maybe we need to find
someone who's more on, you know, that's actually doing something on board that
can help with that. I mean, you know, I just don't want to.
We love consent, all and all, you know, so...
I mean, but the other thing is, like, I'm in, I'm in the middle of it now, too, so I might
talk to Diana, maybe we get some of Victoria and Alvaro's time, but if something
comes up, but just wanna make sure.
So the Infrastructure will work with you. Yeah, right. So I think we are glad to be here.
I mean, if it needs for us to come here again, we'll come here again. So I think.
This level of acceleration wouldn't have come to us if we were sitting on the other
side. I'll be honest with you. Yeah. It was fast because we are in the same room.
Like, so, so, so I think if we...
I think our next steps are even without number one.
We will start producing some renditions of the vision that got spoken over here.
What we also need, we need one or two people named who will be more or less
guiding us, driving us when we are talking of a UX.
You know, see, it's not easy to get this entire teams against another team. Every day.
Yeah, that's not possible. So what we want to have is one person saying, like, you
know what, you talk with this person and then after seven or eight days, review with
the team so that we know what we are doing is right.
And there is a progression.
Because the experience at the moment, the way it stands phase one, I mean, it's like,
it's like what, 5 steps, but those five steps has internally, right, like another half a
dozen steps in it. And those half a dozen steps are crisscrossing, let's say one team
versus another team. It's not like that one team is going to be the sole.
Stakeholder, but even if you say, hey, steps one through 4.
These are the three teams, so, so, so, so who is the general contractor and who is the
vertical? I mean, that is like such a big problem, yeah, right? So, so we don't want to
then...
Put so much of if you don't want to overwhelm Aaron.
If we get our cloud PCs and if we understand, okay, for steps one through 5, sure,
Aaron is our go-to guy from a direction and making sure that he's in the loop. But we
may not need to wait. We may actually start pushing without.
If I, if I see the calendar, we can start negotiating and facilitating, yeah, so now we
facilitate through, yeah, we say, "Hey, so who needs to our we used to facilitate
through Adam prior to so having access to it?"
The cookie.
Yeah, so I think initially I'll be your GC, yeah, and help direct to what you need, and
and if you can say who are step one through 5 specialists, yeah, well, yeah, give us
the list and and we can we can identify those S.M.E.'s for those S.M.E.'s are set some
expectations saying, "Hey, will come to you."
Along with Aaron, because...
2026 doesn't have a lot of time remaining. No, no, agreed, agreed. Right, and if
you're going, trying to do 10 banks or 20 banks, a lot of details to be figured out.
Yeah, absolutely. And again, I do not know if we had anybody, I thought I saw
somebody from CoverBiz today on the call, right? No, no, there was not.
It's all internal, ohh, all internal, all internal, he, he UL runs our third-party risk
management, so he's go with his, yeah, he's he's a S95 OK internal.
Joel Olivares 13:51
Yeah, and I'll be happy to organize something with CoverBase if we need to. They're
really good with working with us on something like that. So just keep me posted.
FortWorth-MuseumPlace-Boardroom 13:58
Absolutely.
Yeah, so just like internal stakeholders, we need some quote un quote introductions.
Yeah, and you need somebody from the prelim side.
Yeah, we need to meet with Norma next week, even though Diana is out, probably
just to get that moving forward. Cover this is number one, next is interlace.
I don't think Vanta is that important for us. That's what we are changing. And then
third is...
Ileana, I think, yes.
Yeah, and um, well, you know, with the internet internet platform, we're trying to
think what is ready for them.
To integrate with their, I mean, even if we, I mean, here's the thing, right? We are not
even warned of who's who, they don't know us, we don't, I mean, we kind of know
them, but like just getting to know that, hey, we are coming.
Yeah, well, and they're in Charles.
They're in the same building. I really think so. I mean, like, they're in the Bank of
America building that is like a U-shaped building.
Like, if it's 2 towers, no, what's the address of the uh, Trianon Street? We have 101
South Trianon Street, two blocks away from us, two blocks away. OK, I mean, they're
right next to Bank of America, yeah, but somebody needs to probably give me a one,
kind of like...
Yeah, he already did the warm intro, we went and did our side, but I think probably
we need to say, "Listen, we are now going, you're a dependency in progress of H2
deliverable, so, so, so that part probably not yet."
It's quite likely by the time we go to them, they may be heads down with some stuff,
other stuff, which I don't know. I've got a visit with them about some other work, so
I'll give them the heads up that I'm dealing with the technical piece. So if you're
coming to Charlotte, I want to know. I will. I want to go for another round of wines.
Absolutely. And I want to see that.
Fifth largest or 5th wealthiest house? No, that you won't see.
That is, I'm not allowed, no, no, you're not allowed, but it doesn't qualify for that.
Well, yeah, we got a call with him at 2 if we want to. Well, actually, truthfully, yes, that
is true. We have a 2:00 project status meeting with Infinite. OK, and several of us are
on that call, so we can we can provide the discussion and introduce you.
In person, you're not sure, so, so, Chantal, three things.
What else? Well, then I'm thinking about, we can, I can help with that. My team is
responsible for digital branding and all that kind of stuff, so, ohh, UX, OK, OK.
And just on the journey too, you know, we can either create some drafts just from
the recording of this call, or we can send you all the recording. Give us the recording,
sir. Yeah, it's recording and you'll have a transcript as well. I have my notes as well, so
we'll mix multiple things. Ileana, do you mind to send out the recording to...
Prashant and Chatnu after this.
Ileana Martell 17:26
Yeah, that's fine. I can do that.
FortWorth-MuseumPlace-Boardroom 17:27
You get that figured out with share file? I haven't figured that out yet.
Ileana Martell 17:31
Yeah, no problem.
FortWorth-MuseumPlace-Boardroom 17:32
Thank you.
Go on the first three things that has to be built, so, but the, but we're doing that in
the existing tenant, right? No, no, no, no, no, we are gonna do it in the new one, so
we've got a, I reached out today to Rick already and asked Steve for help, so
hopefully he'll get us response. Ohh, that's pretty easy, but...
We don't care so much, like node is node, react is react. It should work flawlessly.
And in the stage we are at, security is important, but not that important when we are
just doing the discovery. Okay, so just another question, you know, we know the
build we are trying to use, Databricks.
A lot, most of the stuff, but...
Even in addition to the database, we might need some network component or
something which are hazel.com, right? That's where Cloudflare and all that stuff will
come. Yeah, yeah, yeah, we can help you out with that. OK, OK, so, so then I would, I
would, I would...
Just put it over here, security.
Yeah, security infra, all the same, yeah, it doesn't need to be out there day one, but
yeah, but then just we just start figuring out at least what is a version of design on
paper that we can start working, yeah, name for subdomain for Hazelnetwork.com,
go to that, get their app on.
How will they solve for attacks?
Yeah, so green attacks. Well, how do we do we have any technology to figure out if
what traffic is coming to us? Yeah, so we got all of that and so road meter just
reconfigure that for for the new tenant and and domains.
So, there is infrastructure work stream, there is a journey work stream, and then there
is an integration work stream. That's how I see, yeah, since we have, yeah.
That was.
Organizing construct perspective.
How do we manage the work?
Do we have Jira? How do you create visibility for everybody? Like, hey.
So, Aaron uses planner. We also have another tool one plan for.
Project management, and then we've got our our ticketing software for actually
change management and and Azure Tickets, how fancy Azure DevOps, if it's oh yeah,
the Azure DevOps, like for that side, yeah, so what is the leadership expectation like?
Hey, these three work streams are work streams, do you so how much?
Formally, we go, right? Hey, we actually use Jira, not Jira, sorry, planner, and then
create the kind of Kanban boards, and each Kanban board has a ticket, so we don't
want to track it. I'm not sold on ADO specifically for Hazel directly.
Um...
I don't know if there's native integrations for GitHub and just using that directly. That
seems to be where Microsoft spends. Well, do we load Jitub? Jitub is good. If Jitub, if
you, if we can create, yeah, we don't have a subscription, you'd have to stand it up
for for Bazel, Bazel.
Well, I mean, we, we, I mean, we have a subscription right now, but it's... Well, you're
saying Jira, so, so what tracking we can do Kanban, all that Jira has that, well, yeah,
but GitHub has all that, not Jira, Jira, that's where I was saying, no, I'm sorry, GitHub
right now, I'm fine with us starting in GitHub, I mean...
ADO has proven to be a little complicated. What do they do? Azure DevOps. Azure
DevOps. Yeah, yeah. I mean, it's basically GitHub, but it's the... It seems like they
spent most of their effort insight into GitHub then. Yeah, all the AI is there, all the
GitHub actions, everything's flowing in that direction, so...
We've talked about internally moving to that. It's just, well, I said, let's start with that.
Yeah, let's put it in. We just try to figure out how to organize it over. It doesn't
complicate. Yeah, this side, you know, we'll just stand up GitHub and then add some
people and it's very easy.
everything in the bridge and nothing in the bridge.
That's right, yeah, and it has the concept of, I think, boards, right? So we can have
three separate boards, and yeah, it has it has tickets, it has all sorts, yeah, different
tracking is also, so, so I already allow us to access GitHub, well, it's actually, yeah,
yeah, that's just certain teams.
Ohh.
Well, luckily, this is all outside of. That's right. So maybe we're not involved in any of
this. I like it. Ignore the very fast, great things. Yes.
You hear that, I mean?
Yeah, so yeah, I mean, so it sounds like, yeah, the main infrastructure is gonna be
GitHub, it's gonna be Databricks, a little bit of Azure, I don't really need M365 right
now, but well, we are, we will, yeah, in the work teams app, yeah.
It doesn't matter, just add it, I guess.
We're gonna have.
I do feel like most of our people use web portals versus Teams experience, I think.
Ohh, but it is, but the opportunity there with basically creating an app, it's going to
create some shortcuts, so people will just have to, yeah.
I mean, because you'll get the alerting, you'll get all that kind of stuff, right? He
doesn't have to build that. He just triggers.
Yeah.
So, I think, yeah, I guess the outgoing plan right now is you guys are gonna kind of
say, "Here's the proposed architecture and the things we need to get things going.
Obviously, then the IT team will say, 'All right, we can tackle this, this, and this, and
then you guys need to do this, and this, right?
The Karla, yeah, I mean, 3 three work streams, and then finally is the integrations.
Yeah.
We did not talk about the data, what data this whole process would need it, and
where this resides, how do we get it out? You know, it would follow from the middle
one journey, most likely it would fall from there. Well, yeah, and then just kind of as a
reminder, so when we're deploying apps on Databricks, then we would be using the
Databricks late base, which is their...
Postgres database, then we would be using their data lake, which ties into that, to
hold all the raw data. For now, we don't need the data models, I don't think, because
we'll wait on, you know, Databricks to tell us, hey, here's the tougher model you need
to have and all this kind of stuff. But, you know, for Rudy, it should be able to help.
with some of that, some of Databricks on. Here's how you set up LinkBase. This is
how you configure apps against LinkBase. There are skills for Databricks for you to
do these things, get these things deployed. The whole idea is everything, the whole
stack is sitting on top of Databricks, like, you know, the database side of the
compute, deployment, etc.
Anything else that we should have talked that we haven't talked?
No, I think you know with the idea of doing the standing meeting, so that you know
we we get some some traction, I think is good. Most of the teams that you would
need to work with are in our McAllen office, so Maruthi.
David, Diana, the onboarding team. So if we needed to do another workshop type of
activity, it would make sense to come to McAllen because you could get all the
people that are online right now. OK.
Sounds good. And I'm sure you've never been to McAllen's field. I'm working there.
Very good way. Yeah.
Yeah.
Yeah.
I think #2 is by far the most important the faster we start. It has zero dependencies in
some of these things in my view.
And more of it's on your side, right? Sorry? More of it's on your side, they start?
Yeah, we'll start #2 as soon as possible. The 3 engineers are already ramped up with
essential knowledge, today's session, and the documents that will clarify many of the
dependencies which we hear.
K.
I mean, we the way we work with on Rafa is.
Literally, for the first month we were meeting.
Three times a week, we had a standing meet, two standing meetings, one in the
morning, half an hour, 9, 9 A.m. Eastern or 10 A.m. Eastern, I don't remember, and
one in the afternoon, so we did not have, we did not have the work management
system per se, yeah, so we just had access to Shawn and...
Joel, for first two or three weeks, I think we...
very religiously followed the three-day session where we are not meeting one big
continuous slot. We say, hey, we start to meet in the morning. Some days we met in
morning, but did not meet in the afternoon. Some days we met in the afternoon. But
we were able to collect enough information, quickly convert it into the user
experience app.
Next day we are say showing it to him and then oh maybe this doesn't look right or
well how do you do this weightage calculation? So that kind of discovery process is
what we are trying to stand up.
That clarified the medallion layer. It clarified the assumptions that we had in our area.
It started making progress fast. All this time, I thought you had by coded yourself the
Rafa. I did, and then we they realized how broken it was when they.
We can tell you that.
It's awesome. This is why we can go so fast. Yeah.
So that became the substitute for the Word document or the PowerPoint
presentation. That makes sense.
I think, you know, as we talk about UX and our workflow, right, our process is very
complex, what we are talking about. Plus, this is all new, right? We have an
advantage to, you know, define what can be...
scope, you know, MVP or what can be phase one or phase two. Right, so we can even
say like, oh, you know what, this workflow will have more complexity, you know,
behind. Let's not worry about getting it for the external user. We'll have it as a, you
know, manual right now. So those discussion also will help us prioritize and define
our workflow for today.
What is that we want to anticipate after three months or six months? That way, we
know, like, the core engine has to be built. Yeah, what is a backend priority and step
one, step two in terms of build on that?
Call.
And so, I don't know this piece, because y'all, you know, obviously you've been
working with Shawn and Joel and others prior to this part of me being involved. So,
are you going to put in a scope of work and then we're going to have kind of an
estimate of how much this is going to cost us?
You're doing it for free. You're, you know, how are we, you know, how do we
understand, you know, what amount of the effort is gonna be involved with building
this out? So, yeah, I think, see, think it this way.
The work will start maybe from today. That's what it is. I think this is all TNM setup.
So we are working as a team.
you know, part of your journey together, find out, you know, 10 days down the line,
find out like, is it a two months of work or one month of work? And we plan it and
move forward. The deadline deliverables will follow what we conclude together. So,
so I think if the conversation is...
We have a contract which is already signed by Shawn, so we have a team, 2 1/2
person team already set up, right?
So that team is already being wrapped up. Today is probably the first day of that
team from an official perspective, which is why we were talking about getting them
the access and all that. Like what we did for ACE, like what we did for Rafa, once we
understand what needs to be done at a functional level.
Once we understand they are the business objectives more towards building a point
deck version right away at the first go, or is there an incremental approach to
sophistication, quality, blah blah blah blah, not quality in terms of item, yeah,
beautification, I said, that's what I meant.
So, once we start blowing up the app, meaning once we start describing the app, the
requirements, like today, right? I mean, we feel we have enough to start building the
vision as an app and start showing it.
From that, I think we anticipate that we will have, I would say, another two weeks if
we are sticking to our discipline of meet every day.
I would say, give two or three weeks for the onboarding journey that should lock
down. Hey, what do you want to do?
So now once you log the experience piece of what you want to do, the data piece
will start to fall off from over here. Then we will start to ask questions like, hey, do we
integrate with Rafa or do we give a manual input? Do we integrate with...
the credit unions data set from American bankers, what have you, right? So all those
things will start to fall once we lock down the MVP. So I'm anticipating if we, in
another two to three weeks, we should have a solid looking rendition, which is
running on our infrastructure, like with the mock data.
Um...
which will produce clarity, functional features wise and data wise. Hopefully by then
the database standard is up. Hopefully by then the product owner role is onboarded.
Then basically we just try to figure out like, hey, how quickly can the rest of the
pieces move?
Right, so, but from a, so we already assembled a seed team. The seed team will start
working across all the three streams wherever. That was the proposal that we
ordered. Generally, we don't wait for paper documentation to start.
So, I mean, that's really kind of where my mind was going, like, do we gotta wait for
scope of work? Do we have to sign off on the scope of work? And then, you know,
it's very attractive, commercials and all that.
How much was that? Yeah, we've signed an SOW and it's designed by a couple of
engineers. They start working and, obviously, I know Sean or Sean both basically
adjust that basically on how much they really do. So, I'm not too worried about that. I
think the key thing is, you know, once we get a good understanding of what we want
to build,
We would like to set some, like, here's some clear goals and political things you want
to shoot for. Yeah.
I would think kind of phase one, like your depth diagramming out here too, is also
like, you know, what is the actual application architecture from a high level? You
know, what open source workflow engines or toolings are we going to use, you
know, so that we're not building those things ourselves. So, yeah, stuff like that. Yeah,
yeah, yeah, so we may.
Design for more than MVP one, but we may implement.
Yeah, yeah, I think we should totally, you know, set the architectural runway, right,
with a pretty good distance, so that we've got the right pool sets embedded, but we
may not be leveraging them all up until, right? So, both in Rafa as well as in ACE, in
ACE, Aaron was our...
Product owner, program manager, technical direction part, so we would, once we
understood the requirement, we would then that was also involved heavily. I think
there are a few other people, but we would document, hey, here is what we are
intending to build, here are the components, here is the UML sequence diagram,
here is the rationale behind our suggestion.
Here is how we'll do the security testing. Here is what we will do the update. So we'll
ask somebody to sign off.
Right, and then that would decide what are the so, typically, we'll Rafa was very
quick, was like, yeah, I think thirty-five, 40 days is had more than one stakeholder
input for Adam to be assembled, and then sometimes we started with basket one.
But then one or two use cases of basket one would get deprioritized, so we will do
basket two, so we will do the basketing with Aaron.
Yeah, and then you know one of the thing we may want to think about is, if we're
gonna use UVPR pretty heavily, I mean we've done a lot of the build and the data
bricks integration there, so maybe there's maybe you either expand that or maybe
we have to kind of retool it into this somehow, potentially just something to think
about, yeah, just to this part right there, it's already kind of.
functioning. Yeah, so Rafa is going to be a system dependency. That's what my notes
are. So it may need a little bit of massaging here and there to support this. Yeah,
well, and that's what I'm saying. I don't think it has to say in its current form. I mean,
obviously, the...
UI and stuff that you build is perfect, right? But we expanded after we guys handed it
over to you guys. Yeah, well, like why not just take that and start expanding this into
the larger portal, right? So you can think about those things. Okay, I'm sorry. So, but I
haven't seen the latest step. No, we haven't changed it. Yeah, no, we haven't changed
it. Y'all don't know.
Right, it sounded like you you said you you modified it already. Ohh, no, so we
modified it to make it independent for the stuff that we got.
Hey, UVPR for everybody, correspondent banking angle, right? Remember? So we
expanded the app and... You did it here internally? Not the internal one, externally.
So whatever app we had, we created a copy version of it and we made it Vantage
independent. Yes. Oh, okay.
OK, Vantage logo independent, and that's what Soham showed you, right?
Sorry, what? So, so the version that we handed over you, the new UI, we preserved
that version and froze it. Okay, then we created a copy where we started expanding
the UI of it, but that's still paying expose. We removed Vantage Loop out of it.
And we tried to use it in Inspire as a, here is an app if you want to, you can get it
from the Vantage Collab partner stuff. So we did that, we didn't want to show the
Vantage version of it.
OK, so on this past week, updated the RUI, matched our new one. OK, so we're also
gonna show that to you before you got into production. Yeah, just wanna make sure
that that remains being whenever you, yeah, yeah, yeah, yeah, yeah, but what I'm
saying is take that and then maybe just expand that into what we call this portal that
becomes HASUS, because we're gonna have such...
dependencies on it. It's already given you a starting point. We've got the code base,
we've got the Databricks integration, those types of things. Yeah, yeah, so, so, so, so
deep into it, Sharadul went deep into Databricks as a result of the security work, and
then the other two people are also ramped up, so, so we are not worried about.
We don't have a massive lead time to create with the first version. Yeah, no, that's
fine. I was just, yeah. Yeah, so point taken. Yeah. And it's your IP. Not that, and not
just that, but I was just saying, it seems like since we already have a deployed app,
we've got deployed, it's connected to Databricks. You have some things, maybe you
just.
Kind of report that into what this becomes, just so you know. So, basically, you start
what you are saying is like, hey, why don't you start on journey to and not wait for
the Hazel databricks piece of it, right? That's what is is the you take what you have
now, start going on that, yeah, and then you can port that into this.
Once it's done, and so you've got the UVPR piece already built, which is 1 menu item
or stage or whatever, yeah, and then you just keep from there into the new feature
functionality for onboarding, and for clarity, the are they going to create a?
or port Rafa into the Hazel tenant. So, yeah, they're not going to rely on the existing.
So, why would you need Rafa in its current form for Hazel? You probably need the
data of Rafa, right, with the UX.
Head chopped off as a part of your rules. Absolutely, yeah, absolutely, potentially,
yeah, I mean, but I mean, you know, when someone's looking at a bank though, the
UI's already got a lot of, oh, that's for negative, yeah, yeah, yeah, yeah, for the
internal view, for the internal view, yeah, not for the external view, but yeah, yeah, I
got, but the more important part is the data to.
perform the risk assessment on the bank. Yeah, that's already been built, right? Yeah,
yeah, yeah, but just to be clear, right? So whether it's an external UX or an internal
UX, at least at this point with whatever information I have, at the moment, the
onboarding, so what I'm thinking of is probably a single app.
Exactly, you have one, one that is an external one that's facing it, exactly. So, what we
are thinking is, so I treat them as buckets that are separate. Yeah, it's just a single
app. So, so what I'm thinking, instead of making the experience look like Hazel
onboarding.
I don't want, my recommendation is we don't think onboarding. We think, so would
we call that hops?
Hazel, on, no, no, we don't want to call it. Get me onboarding portal, onboarding
process. I mean, I, we just we just need to call it, just call Hazel, right? Yeah, and it's a
sick, you won't get in. I'm.hazelnetwork.com. See, it is going to it's going to look
like...
ACE, that's how I am looking at it. Like ACE has this whole concept, right? So now
today onboarding, you may start with onboarding. Once you're onboarded, right, I
mean.
I'm anticipating more capabilities inside this, so we want to design Hazel Portal with
the first app inside Hazel Portal, which is the onboarding app. That's how I'm, that's
what we are recommending onboarding portal, so that way that this is called hot. OK.
We'll also have some, yeah, does that make sense? Yeah, no, no, it makes perfect
sense. I mean, I, I, it's all a means, but this is the first. I mean, to me, this feels like this
is Hazel Business Center or something, some functional name, which is...
Larger than onboarding, no, it is, it is right, larger than onboarding, onboarding is, it's
the operational port, yeah, it's just like ACE, it's gonna have all our workflows, that's
staff, yeah, well, they're still on the names, so, okay, I, I like Hop and I like the bunny,
and so, like, it's the Hazel, Hazel.
Operations portal, but then that's fine, or if you keep the business information,
something you could do a big wig kind of analogy. I'm not going to get into this, but
for now I will call it off, but either way, yes, it is a single portal to run the business,
and underneath that portal there will be various.
Uh, workflows, utilities, etcetera, like they can pop through, because, because it's a
bunny.
And we're we're definitely doing that. I gotta jump to another call real quick, but
jump. No, we had a, we don't jump in, we don't jump in. Was there alcohol in lunch?
The basic thing, I'll jump back in a second, the authentication, authorization, user
management, all that will be needed.
Absolutely, right? Because you, you don't know who is the today's owner from the
bank side is gonna be changing tomorrow, right? So, you need that whole set of,
yeah, user management, so you probably did not cover this.
What he's saying is, you know, he's saying, like, hey, tell me.
We just say, hey, this portal is for member banks. That is fine.
What are the member banks role for which HOP is designed?
Yeah, so...
Like Diana provisions users on Infinite today. Infinite has a way of provisioning.
Or will she use hop external or will she will she use hop internal?
Well, it might be both.
Yeah, so, so in, you know, so for infinite, that's the the actual core engine set up,
right? Yes. Can we have a demo of that, so that we know this is the, you know,
Mercedes engine, this is how it's getting set up, now we are trying to onboard, I need
to, no, absolutely, we can do that and and get.
Get the right people to stop kidding.
Yeah, I mean, if you guys want to do that now, that's an easy thing to reschedule as
well. I'm trying to think.
I think most of our...
If.
So, but so, so hop dot, I mean, hop in external dot hop dot Vantage, no Vantage, but
it will probably be hop.hazelnetwork.com, right, and then hop.vantage.com.
For the for the inside view, yes, we could do that right for the inside, and then hop,
yeah, so, so word goes in hop insider.
versus what goes hop member versus hop associate.
So, hub associate portal, hub member portal, member portal, right? And then
member portal will have different kinds of personas. We do not just know, because
what is going to happen is the member portal will have their right operational
people, operational people, exactly, and treasury people, exactly, right?
So even though HOPS is onboarding today, it might become an operational tool for
member banks. So it's a back office, mid office order for back office, mid office users
in the member side. Absolutely. Probably not member banks.
Direct users, but hop external or hop member portal.
So, this is...
Yeah.
Diana, are you on the call still?
Diana Plata 46:24
Sure, I'm here.
FortWorth-MuseumPlace-Boardroom 46:26
Okay.
I didn't know if we had a to get on with infinite figure out that issue.
Diana Plata 46:34
Yeah, we got it solved, dude.
FortWorth-MuseumPlace-Boardroom 46:37
Beautiful. So yeah, so if we want to do a little demo, Diana can do that for us. Okay,
so if we have 5 minutes, I'd like just to wrap up the onboarding process, just a typo
on that. But would that demo be helpful though while we're here? Yeah, let me stop
sharing.
I think we finished the process first, and then let's schedule a different time, yeah,
yeah, for for the demo of the portal, that way we can have the, you know, all the right
people.
That's okay, I will take it from you.
The last piece here of phase five is the end of day file, posting file. So we just need to
work with the member bank to get some kind of SFTP process to send them, set up
with Infinite so that we can send that file at the end of each step.
Hmm, and so...
Yeah, we haven't, we haven't had to do that yet, but that's the member bank to
infinite, infinite, infinite, yeah, and Diana is not through the portal, right? It's a, that's
not an option.
Diana Plata 47:52
No, it's through an SFTP. Not that I understand. It's not through the portal.
FortWorth-MuseumPlace-Boardroom 47:59
So, that's a whole kind of separate process.
And then the...
Training certification, we'll have some training for them. There may be some guides
in the future. Maybe we have videos, but we'll probably have some sessions to train a
member bank on the console. So maybe the HOP console has a...
a feature there where you can do training. Yeah, yeah. So, you know, it's probably not
a day one kind of need, but.
But there is a separate third-party platform for training, right? That's what my
understanding is.
We don't have one now.
Yeah, I mean, it could just be PDFs and video links. So I don't think we need to get
too robust there. Okay.
Um...
The certification plan is just us walking through the portal with the member bank and
having them actually send some transactions. So just, it's part of training. And then
we'll actually do some penny testing there at the end.
So, we have a list of tests will have them run, so that will that will all be in the the
consoles, nothing we would build out.
And then whatever sign-offs we have at the end, so maybe maybe that's a piece in
the in what you're building, some kind of sign-off kind of a collection.
or something there.
And then, really, we should be finished.
And then there's some kind of ongoing oversight, which I, yeah, I don't really know.
I would be there. So what would be like a setup? How do you test a sample
transaction once everything gets done?
in production. So for a member bank, who I went through this entire eight-step
workflow with in step three of maybe four or five, there is a two-week custom activity
on interlaced side.
No.
Like when I when I have a Zen set of done, and if I have to send $5000, I will do a
$1.00 transaction, right? What is the $1.00 transaction that how do we do that?
We would just log into the console and we would help them, you know, set up, make
sure they have the right users set up and the right accounts created. And then we
would fund their account, like from a liar, they would send that to, yeah, but that's all
that is out of band, right?
So, so my question is, yeah, my question is, is infinite is gonna be the operational
portal for the visibility, money movement, yes, and reconcile, yeah, yes, yes, if that is
the case.
Diana Plata 51:02
Yes.
FortWorth-MuseumPlace-Boardroom 51:07
On HCL, if I on board.
and onboarding is successful, is there anything we are thinking of that daily visibility
will come on Hazel? Or we will have a user going on infinite and see everything? No,
so what should be on Hazel will be...
Live dashboards, all the data coming out of out of infinite of the interlace is going
into Databricks, and so we're gonna create dashboards, you can see things, but to
actually do anything, if I wanna go into the details, I've gotta go like...
So Diana can kind of give you a rundown of the type of activities that a back office
person would do on a day-to-day basis within the interlace console. But for most
purposes, so anybody other than backroom people that are working on transactions,
everything else should be available through.
Hazel.
Because you know, if, if I'm if I'm the CFO, I'm the treasurer, whatever, whatever's
going on, these live dashboards should give me the information that I need. Yeah,
and how much detail as in? I'm sorry, I'm sorry, so, so, so, so in has a same.
back end, which is our data bricks, or they have their own? No, what we're setting up
is the API to stream the transaction, the data out of Interlace into our databricks.
So, from infinite, we will have a streams coming into, and so then you, you, so on
whoever's building the other applications, you know, the widgets, whatever.
So, that's the design of right now, or that's so development work right now. Has to
be DBD. Yeah, well, see, that's what I wasn't sure, because you can see all all the you
have all the reporting options in Interlace now, you do, so...
Diana Plata 53:19
That's exactly right. Yeah.
FortWorth-MuseumPlace-Boardroom 53:21
But you're saying, Jay, is that we'll be duplicating some of that. Well, we have to get
the data.
into Databricks. Now, that's for sure, yeah. Yeah, I mean, so that, and I've, you know,
Sean, Sean's the, obviously the best person to talk about this design, because the
idea is that any of the more complex data analysis that needs to happen is gonna
happen.
from the data in Databricks. We're not going to rely on, oh, we've got to work with
Infinite to create a dashboard for us to do this X, Y. So you are becoming like a Swift
network, and if the Swift network is providing certain guarantees and monitoring and
observability, they cannot have a dependency on a third party and say, hey, I am the
network.
But then, for whatever reasons, infrastructure is down, then hey, you do not have any
visibility into it, right? So as a network operator, you have certain rights, I feel, to say,
hey,
Enterprise every communication, every end of the day activity that you are doing
with your member bank. I need to see all portions of it or select your portions of it.
Again, you know, Shawn would have more details around this, but we also have to
consider the consolidation of different data sets. So Custodia may also be streaming
data that we need access to around the minting burning, all that kind of stuff that
maybe we've got to have visibility for traceability.
of certain things that we want to consolidate and combine and present as... But that
probably so that on the chain analysis and...
And the T.R.N. T.R.N. right, so those two vendors are going to give you wallet level
observability keys, yes, wallet level fraud and that kind of stuff, right?
So do we care to bring that data into database at some point, if not now?
Diana Plata 55:34
So...
So Jay, quick, and I'm sorry to interrupt, but when you're talking about data, what
data exactly are you expecting Infinite to send? Because they do that today for like
transaction monitoring, things like that. What additional data would we be wanting
to go ahead and receive from them?
FortWorth-MuseumPlace-Boardroom 55:52
No, I'm not saying additional data, I'm saying data analytics. So, you know, being
able to just to say, all right, I want to be able to generate specific reports that I want
to offer to my Hazel members saying, hey, here, the network,
Diana Plata 55:57
Mhm.
FortWorth-MuseumPlace-Boardroom 56:11
may want to share network level data with participants. The network may want to
provide data about the total number of fraud cases across the network. So I've got to
be able to have a centralized database and work stream to consolidate.
data. So yes, for individual banks, they may be sufficient with looking at the console
and looking at the data and pulling those reports, but being able to provide a hazel
dashboard that gives them some nice visual, clickable, drillable type of dashboards.
Diana Plata 56:51
Well, and that's where I'm getting to. I think we received some data, but do we want
to check or get a list of what that data is and make sure that Infinite is able to
provide? Because today, I mean, we've asked for some data and we struggle to go
ahead and receive some. We receive the basic data, transaction, name, things like
that.
FortWorth-MuseumPlace-Boardroom 56:52
Is.
Diana Plata 57:11
But once we drill down into fraud cases and things like that, I mean, I would want to
make sure that we have a list of the type of data that we would want to receive and
make sure that they're able to provide.
FortWorth-MuseumPlace-Boardroom 57:22
Absolutely, and so, but that, but that's kind of the point is, we want to have the data.
Diana Plata 57:27
And when you say, Hazel, are we talking about what hazel.com or what exactly,
where exactly would this data live? Or are we...
FortWorth-MuseumPlace-Boardroom 57:35
Yeah, I think we're saying Hazel to differentiate that in this isolated data bricks
environment, in this isolated database and tenant and all that. So you have that
Hazel will consolidate the data from interlays, from
Diana Plata 57:41
And it.
FortWorth-MuseumPlace-Boardroom 57:53
CRM, chain analysis, all of the different data points, bringing it together, and then
presenting one story for the customer, for the member bank, and then one story for
the entire network performance. I think, Diane, we...
Diana Plata 57:55
Got it.
Mhm.
FortWorth-MuseumPlace-Boardroom 58:11
probably need to use the UX design, what we are thinking of, to make a decision
around the interlays, what data need, and all that stuff, right? So that we can decide
and define on the day one, we need this data coming out from the platform.
We all can conclude, is that right, yes or no? And if we conclude, yes, we want to
present it to the customer, and then we can go back to them saying, like, we need
this from you, let's plan and design. That's right. I mean, at the end of the day, Diana,
what my mental model, and I think the mental model that Shanti is talking about as
well, Long Jay.
Is, as a network owner, I need to know that interlace daily activity of side core to
main core reconciliation process is happy, or if there is a delay, or if there is a...
Like at the end of the day, if there's a problem between a member bank and
interlaces reconciliation process, calculation errors, delays, what have you, the
network ends up becoming the final authority to complain. So if the network says, I
don't have a view.
Diana Plata 59:16
Yeah.
FortWorth-MuseumPlace-Boardroom 59:32
Uh...
At all that, even though my view might be informed by interface, but I'm watching it
to at least have some background information to be able to support any kind of
disputes.
Diana Plata 59:48
Yeah. Well, and I welcome all that data because like I'm saying, even for the network
and the owner, the member banks, it's not just about data, but they want to drill into,
you know, like you're saying, fraud, ACH returns, things like that, that are going to go
ahead and help them make sure that they make the right decisions and they keep
compliant and
all that. So I welcome that. I just want to make sure that we sort of define what that
data looks like and ensure that Infinite is able to support all that.
FortWorth-MuseumPlace-Boardroom 1:00:12
Okay.
Yeah, and I think that's where we'll get into MVP and say, hey, what is that day one
visibility that the Hazel network wants for MVP one? Yeah.
For a basic implementation, what are the risks that we have to be able to be ready to
handle based on 10 banks as our initial scope of?
GTM.
Right, and yeah, I, I, I don't know what that would look like, but I think we'll have to,
really, day one is all onboarding, so...
Diana Plata 1:00:53
Onboard nagging.
FortWorth-MuseumPlace-Boardroom 1:00:53
I think we can focus, yeah. All right, so, all right, we've got the 2:00 with infinite that
we've got to jump over to. So we'll end this meeting and Ileana will get the meeting
recording and the transcript out to share. Cool. So I will ask others to disperse from
theorem left side also, okay? Yeah, because, yeah, we're ending this call and we'll
have to jump on a different meeting.
Diana Plata 1:01:11
You guys?
FortWorth-MuseumPlace-Boardroom 1:01:17
Okay, cool. Super. Thank you so much. Thank you so much. Thanks everybody else
from Theorem. Good to meet you today. Thank you. Thank you very much. Bye bye.
Bye bye. Thanks guys.
Shardul Patki 1:01:29
Thank you.
FortWorth-MuseumPlace-Boardroom 1:01:31
Interesting.
Aaron McWilliams stopped transcription
