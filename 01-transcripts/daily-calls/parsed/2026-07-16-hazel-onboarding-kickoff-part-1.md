---
title: "Hazel Onboarding Kick-Off — Part 1"
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
source_file: "../raw/2026-07-16-hazel-onboarding-kickoff-part-1.pdf"
content_sha256: "b13cf4795088ca3a945a27d46a203a373de6f7b5a4ac52ecd2bccf646cf4cdd1"
---

# Hazel Onboarding Kick-Off — Part 1

## Transcript

Theorem Labs on Site – Hazel Onboarding
Kick-Off Pt 1 Transcript
Date: July 16, 2026
Format: In-person | Teams
Duration: 2hrs 51s
FortWorth-MuseumPlace-Boardroom 0:21
there'll be heavy demand to grow the network very rapidly. So really we have, in my
estimation, between now and towards the end of the year to kind of perfect at least
the initial onboarding kind of journey. Perfect's not the right word. Get it good
enough. Something like that.
Yeah, so just kind of keep that in mind. That's generally what we're trying to shoot
for timeline-wise, target-wise, so forth.
But the MVP one is really the H2 of 2026. How many banks are we looking at MVP
and such to prove the MVP one? The goal is roughly 10 to 15 banks by the end of
the year onboarded, no matter how clunky, manual or otherwise.
And then, yeah, 2026, taking on the larger buckets of banks.
And so I would say, you know, Aaron, Aaron, and you know, Chris will help us with
this kind of process, as well as obviously the ops team of, you know, let's take some
of these first few banks that that we're talking to right now, and you know, help have
them help us, you know, flush out some of the details behind.
Is it cover base to be clunky? Is it Vantage, or you know, whatever it might be? Yeah,
because we've got a, I think, a very defined good structure right now, but we don't
know where some of the, you know, gremlins are in it yet.
So then you talk about the onboarding.
There's A functional part of it, and even there will be the on-chain, the technical part
of it, right? A lot of things you, you know, when you talk about the getting it onto the
network, like the certificate authority, you know, I don't think the bank of business
folks will know that all, so we'll have to have a...
structure, where did we talk about, hey, get the functional details in, have a process
moving forward and get the blockchain related technical configuration as well to be
part of the onboarding. Yeah, there's no, there's no blockchain, but it would, no, it's
really just interacting with something like Infinite to actually set up all their accounts,
set up their configurations.
You know, get them, you know, live effectively. And when we say live, we're talking,
we have a model that we call basic. And basic is literally just opening an account for
these member banks. That's really kind of the initial goal. The other stuff is way more
complicated. But all the information we have to collect, and you know, Aaron can
to go over that here in a second, is a lot. And, you know, there's a lot of risk
assessments, there's a lot of scoring, there's a lot of kind of ongoing back and forth
and due diligence. And so really, we are going to have to journey map, you know,
what, where do they start? You know, what are the stages between, you know, that
initial start and then where does it stop?
And so, we have not mapped that out, so that that's an exercise that we can, you
know, go through a little bit today and try to, you know, get through that journey
map, and then we'll flush out what are those kind of, you know, scenarios where, you
know, maybe there's different stages within those stage gates, those journeys that
we have to think about on happy pass, happy pass, etcetera.
Yeah, so I guess we should be approaching this thinking it like, this is them applying
for access to the network. And so it's data collection, it's risk assessments, it's
document reviews, and walking through that process. And then
contracting.
And then after all that, then it's firing off API calls to Infinite to say, go create this
account, I have everything I need. All right, so this is the journey starts after the
banker has pursuaded the...
The banker has persuaded the prospect to say, hey, let's go. But yeah, that's where
the journey starts. Absolutely. Yeah, and I think we'd probably, you know, obviously
there'll be pre-conversations prospecting, but, you know, go to the website, you
know, pick a plan, click the button, start your journey to.
get going, get started. So it might be good, Aaron, if, because I know you flushed out
a good amount of like what we plan to go through with Diana and you know, just
what's the team's plan right now on on onboarding. So our current journey as we
foresee it. And I think that's a good point. That's this is this is us.
Guessing this is the right.
data and information and workflow that we need. Yeah, so I would even challenge
everybody, you know, first principle thinking, if we don't think we need this, or the
process seems odd or redundant or relying on something manual when we can
automate it, let's think about that. You know, so let's reduce these things down if we
can, you know, that that would be better.
than trying to recreate what we've got today, just because today is what we can do
today. But let's try to think about what should we be doing tomorrow. And one other
piece that I think is important, because I've seen this in other third-party platforms, is
where there are opportunities for us to shortcut
the person who's going through this process.
shortcut what information they have to provide. If there's a way that, you know, hey,
I'm the banker from First National Bank of Small Town. I start popping that in and
maybe I ask, you know, what's your FDIC number? They pop in an FDIC number, refill
in as much information as possible. Yep.
You know, why, why make them type in addresses and blah blah blah? You know, if
there's other data sources that we can pull in to pre-populate and they just have to
verify, that's a great process. Well, and then that leads, actually, it's one thing I forgot
to mention. The other, the first internal app will actually be the Rafa report.
So, we already have that, and that Rafa report provides us the risk scoring and the
bank information that we are going to use anyways. So, just tap into that that that
apps API, which is already ready. Yep, yep. So, that would be part of pulling like, who
is this bank? What's the details on them? So, that's even that prospecting stage of.
who is this bank? And in fact, that's where the prospecting stage should start is who
is this bank? What's their score? Are they even qualified at this point? Most of them
will be. And in the 1st 10 to 15 banks, those banks that we try to acquire, are they
through a correspondent relationship or are they
direct relationship? It could be either. So there is a divergent path there where, you
know, one bank might be direct and it's an instant open for that bank. The other
might be a correspondent and there's more details. I would say we focus on just
direct bank right now, because correspondent will get complicated.
But, so even a correspondent could open up a direct account, but then they have
downstream nested banks beneath them, and I don't think we need to plan for that.
Who do we see? It'll vary by bank size, but...
Who's going through this process at the bank? Is it Treasurer? Is it someone in Ops?
Oh yeah, who's the audience? That's a good question. I think we need to nail that
down. Again, it's going to vary, but... The first two people we've talked to, one was a
COO, and the other one was a digital banking lead.
But then we have who has the authority to actually open an account for that. Right.
And there may be questions that they want to defer to somebody else on their team
to answer. So I see, you know, today in CoverBase, which we use for third-party risk
management, it
fires up a portal, and I'm not suggesting this is the right way to do it, but they fire up
a portal that is a unique URL with a token attached to it, and anybody who has that
link can fill in the information. So they can say, hey, you know, I don't know this, you
know,
They just send the link out to their internal team members and any team member
can click the link and provide the information. I'm not suggesting that that's the right
way to do it. This probably needs to be a little more secure. But giving people the
option to, without involving anybody else, hey, help me fill out this application.
Especially with larger organizations would be helpful.
Well, yeah, so maybe we...
Joel Olivares 9:02
Aaron, hey guys, this is Joel real quick. Aaron, have you discussed a little bit of what
our process is going to be so far, what we have documented so far, and what we've
done in cover base for intake?
FortWorth-MuseumPlace-Boardroom 9:10
No.
So, we'll get to that here in a few minutes.
Joel Olivares 9:14
Okay, yeah, I hear a lot that we've already implemented, so I wanted to make sure
that, you know, we were all going to get on the same page.
FortWorth-MuseumPlace-Boardroom 9:22
Don't worry, you will get all the credit.
Joel Olivares 9:25
I don't need the credit.
FortWorth-MuseumPlace-Boardroom 9:26
Yeah.
Yeah, you want to go ahead and just kind of walk through the process now, Sean?
Yeah, yeah. I think let's at least show the team and everybody what the current idea
for the onboarding is. I think that will inform us all on how we potentially think about
kind of next steps.
Let me do just a brief overview, just show you one slide, and then we'll actually kind
of talk through the details and go as in depth as we need to. But overall, we're
looking at six steps. So we make a decision in the beginning based off of, we call it
the Rafa Report. It's theorem built the...
an automatic report that looks at all the UPBR public data and builds all that. So with
that, we get a score and that tells us whether we should, at early age, we should
move forward or not. So if so, we give them, we send out an NDA. We were doing a
pilot or LOI.
Earlier on, but we were kind of past that stage ready.
Then we have a brief due diligence that we do. I'll walk through that. And then we
are discovering that banks are asking us to do due diligence on ourselves as well.
And so each bank will have a different process there. We've got a couple of things in
place to try and streamline that. But depending on what the bank requires.
Asking us, them asking us, yeah, which is the whole point of Fanta is like, we just,
yeah, we're gonna give them all the documentation right here, so when they click go,
it's here's all the documentation about Vantage Hazel and everything they should
need, so they don't have to hammer us about it. Theoretically, they'll have to, yeah,
so whether they will be okay with that or not.
And we'll see. Then we have a quick approval process. We do initial setup and then
the agreements that we send to the bank to get some signatures, some
acknowledgements. And then we provision the bank and Infinite's console. So
Infinite's helping us with that, but they told us that we'll have API access to that in
the future so that we can do more of that.
Which would be great, and then there is some training of the bank and how to use
the console, some certification testing that we'll go through with them, and hopefully
over time that will get shorter just as we can improve it out, and then they're live and
ready to go, so that's the overall.
Six steps, but I'll walk through this, and of course I can share any of this after that,
and that's all on the basic model, right? So that's just getting this is just basic, this is
not advanced or enterprise or...
One.
Dedicated.
Play.
I don't know if this matters, but what timing do we think is, because the NDA alone
makes legal team, that's probably weak, right? And due diligence plus reverse due
diligence is.
Ohh.
Right now, we're saying it should take one to two weeks, but yeah. Well, I would
argue that the MDA that we have is pretty generic. Yeah. And so if we were just
thinking about it as an onboarding flow, that seems like a terms and conditions click
through that they can.
Yeah, that's, yeah, they're not, I mean, today we we're executing on NDA, but you
know, we can probably...
Click through that and say, "Hey, you know, I'm you know, blah blah blah, and I'm
obligating to."
So, before that...
So, I heard that, hey, before we even prospect somebody, we probably use the
information from Rafa to figure out who should we prospect. So, between identifying
and actually recruiting a bank, no, what is the lead time? Most, well, yeah, that lead
time could be large, so yes, there is a...
step right before this or a gate before this which is prospecting.
prospecting. Bank sales cycle is about two years with this, you know, with the
associations and possibly, you know, moving forward with us, you know, that might
shrink to a few months. But the way that I look at it is what I do when I'm trying to
talk to a bank is I literally try to figure out what's their asset size, who are the main
players, just basic information about who am I talking to, is it COO, CFO, etc. That
information would be useful for just the conversation.
That information could actually defer to this office once that is signed. It could be.
Well, and that's part of the information stored. Well, right now there is no true CRM.
So yes, maybe a CRM line, but that's why we were. So there is a product from
Databricks called.
customer data lake or something like that, our hope is that they'll be able to spin that
up. That is basically a modern CRM. Yeah. Yes. And so we want to leverage that data
to manage it because it does, you know, continuous.
Marketing campaigns and, you know, tracking on an individual level of.
So that I would say is going to be the CRM. Let's just assume that that CRM is going
to give us the data we need. And let's just understand what the data inputs are from
that. Because my hope would be is that Databricks employs that. They really want
that live.
Yeah, don't want to build it, but yeah.
Now, there's probably some...
plugins or integration that you would want to do into that data set and or I don't
know how it operates everything now. It's so new. But if it doesn't have a UI, then
maybe there is something we have to do there.
Rudy, I don't know. Did you see the customer data lake thing?
Maruthi Dantu 15:24
No, not in detail, but I know they're still also in the preview phase. I don't think it's
completely launched out to GA yet. So maybe it's a good time for us to explore.
FortWorth-MuseumPlace-Boardroom 15:40
Yeah, so when we bring in someone like Zeb as an example, that might be something
that we get them to build the infrastructure, get them to build the customer data
piece, and then you guys work with them to figure out how you plug those two
things together or make it a menu item in the portal or whatever it may be. So.
But yeah, good, good, good call out there. Yes, there is a stage point just before that
prospecting.
So let me walk you guys through this in more detail. Now, this is in flight. We change
this, you know, once or twice a week. We have not walked anybody through this all
the way. And I think the phases align with the doc I just showed you. We'll find out.
So you can see the comments in here, you know, that we're
Still building this out. So, base one, as far as eligibility, that yeah, once we have bank
interest logged, then we can go to the Rafa report and do a check. And so, Sofia and
Ethereum Labs did just finish, I think yesterday, a download of the full report. So,
that's kind of the first step.
of when we want to pull this, we can download it, and then we can have all that
information in one PDF. But it sounds like, Prashant, you've already got an API piece
of that, which is perfect, and that will be the next stage after. We might do a little bit
of a cleanup to see if it needs additional hardening. It's public data anyway, so.
But then just figure it out. Yeah. I've got a quick question on that front. Does that
include data only for financial, for banks, or does it also cover credit unions? Today,
just banks. So yeah. We may have to expand it or do something later on.
Because the scope of Hazel is not just banks, it's also credit unions. Yeah, it's a good
question.
Breaking in data on.
And I would, you think so, have something.
So yeah, maybe an asterisk on that of, today we'll focus on banks. I think that's just
because it's what we have and what we know, but credit unions could be in scope in
the future. FDIC chartered banks or FDIC chartered banks.
Because the speedies and others aren't in there either. Yeah, right. Well, actually,
that's a good call. Yeah, we like what it what if, yeah.
Yeah, or or a trust charter, right? That's where I'm also thinking, you know, 'cause...
We are gonna onboard ripple.
And you know, they they've got a trust bank, right? Or they're pursuing whatever.
Yeah, so I mean, I guess the best way to think about that is, you know, let's not hang
our hat on that being the sole data point for the risk assessment in the review. We
may have to expand that. And so the architecture itself needs to support future
expansion of that data model. Probably the 90% of solution.
Yeah.
and foreign banks as we start talking about onboarding banks from outside the US.
Joel put his earmuffs on. However, I have had quite a few foreign banks ask about us
potentially bringing them into the network.
We have talked about that, because the truth is...
Jurisdictional lines may not be as important.
Or money.
Oh.
Interesting in theory, yes.
Doesn't mean different frameworks won't apply, like a micro framework for
statement clients versus US framework.
So.
Oh, sorry. Go ahead. No, no, no. Actually, this is a good point. Joel has it up. It might
be good if Joel shows what the UVPR so people know what we're looking at.
Oh, here, yeah, I can do it, yeah.
So really the idea here on this phase, right? It's just understand who the bank is, who
are the key players, what is the risk of that bank? And we do it through our own, you
know, it says camels, it's not, they're not real scores. There are a version of Campos.
And then we come up with a final score that two up top in this particular case.
says, you know, this bank is satisfactory based on our metrics that we've calculated
off their own public data. So, you know, obviously we would probably just embed
this somewhere in that portal and then tie some of the data sets back to the
onboarding workflow phase.
Would the applicant have visibility into this data from Rafa?
That's a good question. I'll see why.
It's all public.
Well, right, I mean, but, but our assessment of that public data, I would think they
want to know what we're raising them, right? Yeah, and it brings up a...
I'd rather have it route a workflow than the banks see it. Well, I also, I'm thinking, I
wouldn't want to call it camel. Yeah, yeah, for sure, for sure. No, they would freak out.
How'd they get that? Yeah. Well, maybe we just do like, you know. Well, I mean, like
what you're showing here, Aaron, you know, just the.
You know, you know, component analysis and, and you know, call it a star rating or
something, you know, as opposed to trying to, because they may say, well, you're
rating me a two, you know, the OCC rates me a one or...
They're going to try and reconcile that. Yeah. Well, I think maybe we just deal with it
as, you know, if they're either green, good, you know, yellow or red, and then if they
need detail, that's a reach out conversation. Yeah.
But are we, from a regulation perspective, are we required to give them that
information if we reject? No, no, this is all up to us. Right, and so that's why I was
asking, are we going to make this something that they see and they can say, oh, well,
this isn't the only component. We have the Wolfsburg questionnaire, some other
data that we, so we're going to ultimately come up with an aggregate risk score.
That includes this, includes their questionnaire, includes some other data points. So,
yeah, this is just eligibility to, yeah, like, can't we, we want to keep talking, yeah, we
want to send you an NDA, and I will say that.
Again, the goal is not for us to talk to every bank. They may require that. But if
there's a bank that's on the internet, goes to hazelnetwork.com, loves what they read,
and wants to sign up, we want them to just click the button and go. So just keep that
in mind. There may not always be that BD business development side.
We want it to, we want it to be like, if they were signed up for...
Venmo or Starbucks or whatever it might be, go click a few buttons, walk through
the process, you're onboarded.
It's mostly just notified.
Our guesstimate, our...
Just so that I can understand, what is our guesstimate of banks that we would turn
away?
Is it 1% or is it going to be? I mean any bank that's undercapitalized for sure.
Just so that if somebody starts the process and we say, well, we're not, you know,
and then it's almost like a credit card denial, like, and these are the reasons why, you
know, we're denying you. I don't know. I would think that's we're talking about an
edge case at that point.
I agree. So that's why I want to understand that it is in fact an edge case and not like,
yeah, that way we're not denied in the system. You know, 10, 20% are going to be
denied.
Okay.
Well, go ahead, Aaron.
Marie Alonzo 23:57
What would what what would be the defining factors of why we would deny a bank?
Would we have to outline that?
FortWorth-MuseumPlace-Boardroom 23:59
Yep.
Well, let's talk through that in the next phase, because I think that's more of where it
will happen. The Rafa report, we're like, you get a one or two, you're good. You get a
three or four, probably we just need to watch it and you get a five, no. So I think
that'll be a minimum. Out of 4,298 banks, there's...
15 on the watch list that are struggling. Yeah, all right. So not a something work
around. Yeah, that's a good question, Marie, but yeah, it's going to be a little bit of,
you know, capital liquidity and so forth. And these are probably banks that are not.
Yeah, exactly. I got bigger fish to fry. So I, so I like Sean, I like your explanation of
basically you type in your name and online or on the website, we do this UBPR check
in the background and green light. Most people will be green lighted through and
then it's like a online NDA kind of check box thing. And then answer the
questionnaire to get to the next phase of the risk assessment.
Whereas right now, it's just it's a manual, a couple of manual steps.
And so phase two is going to be more of the due diligence, and that's where we'll
answer more of your question, Marie. So we get an NDA, and then we're using
CoverBase right now. That's our third-party risk management solution. And we will
set up a user in there, and we can walk through all if you want.
I've been kind of doing some testing here. Basically, this is an online form that we
send to someone. I think the question, we have around under, I think it's under 30
questions last I looked, that they answer, they upload 2 documents, that is their BSA,
AML, OFAC policy, and that may be
more than one document, depending on how they flesh that out. And then the
Wolfsburg report, which is more of a correspondent banking document that we've
assumed that most people have. We may need to double check that. But we try to
find things that people already have. And then the almost 30 questions people go
through, most of them are yes or no.
because what we're doing here is since we are working with FDIC insured banks,
we're going to let the regulators, we're going to rely on them to really regulate the
specifics with these banks. And we're just going to verify that, you know, they are
regulated. And then we do have those specific questions there. So
You just want to put them.
Diana Plata 26:31
Aaron, we're not seeing your document. We're seeing the... Oh, cover base, okay.
FortWorth-MuseumPlace-Boardroom 26:36
Yeah, I'll show you the cover base page and just kind of show you a little bit, you
know, you, well, let me do this. I'll show you the questionnaire just so you can kind of
see. This is something that we can help them fill out. So in the beginning, I'll
probably walk through banks with this.
But as Shawn pointed out, there's probably some questions in here, like, is this your,
is the key information correct? Well, yeah, that's a yes, that's probably easy. They
might know any trade names. They'll put their own name as a primary contact. But
they, at some point, they're going to have to call in other people here to answer
some of these questions too. And so they can just share the link.
Um, those kind of stuff, so that's basically what this looks like.
Marie Alonzo 27:26
I might be jumping ahead, but on the watch list, is that tied to a number, just when
we think about onboarding, if that's one of the first things that we would capture,
maybe not having one of these banks or credit unions have to go through the whole
process if it's someone that we're going to decline right off the bat. So
Is that watch list tied to like an insurance verification number for the bank?
FortWorth-MuseumPlace-Boardroom 27:46
Yes.
Marie Alonzo 27:52
or we would have to go out to an external source to find that.
FortWorth-MuseumPlace-Boardroom 27:57
No, that's kind of what we were talking about. The Rafa portal will pre-screen that. So
we'll know ahead of time. So if they type in their name, bailingbank, you know,.com,
whatever, it'll automatically pull that information up and then say, I'm sorry, you
know, based off our
Marie Alonzo 28:06
Okay.
FortWorth-MuseumPlace-Boardroom 28:18
you know, our assessment, you're not eligible, sorry. But that's a pre-NDA stage.
Right, exactly. Because we're pulling up the name, it's doing the dip into Rafa. Rafa
then comes back and says, no, we're not banking them.
Marie Alonzo 28:22
Okay.
FortWorth-MuseumPlace-Boardroom 28:37
Yep, and then obviously...
Marie Alonzo 28:38
And is there some kind of disclosure required if we turn away a bank? Because today,
a consumer, right, if we turn them away, we have to give them.
FortWorth-MuseumPlace-Boardroom 28:44
Ohh.
No.
Marie Alonzo 28:48
Okay.
FortWorth-MuseumPlace-Boardroom 28:49
Nope.
We would probably just say, yeah, sorry, you're not eligible if you'd like to be
representative.
Something like that, because there might be something get flagged accidentally,
who knows, but...
for the most part, we would not allow them to automatically.
Does Coverbase support APIs? Yes, so has a full scope API, and do they let you show
up widgets? They can, but I also, because I've been working on it intently, you know,
over the last couple of months.
Even at a very primal basic level, they can they can automatically complete their
assessment based off data that we supply. So, in some cases, as I've been going
through the embedded banking stuff, and as we've changed, you know, questions
that we've asked or whatever,
They're able, because they're AI enabled as well. So they can use AI to answer
questions based off documents provided. So if we collect documents up front, so if,
as we're saying, the Wolfsburg questionnaire, that's an upload, the BSA documents
upload.
then we can pass those over to them. They have their AI automatically answer the
questionnaires based off that information. So the human is then just correcting the
AI information and certifying. Certifying that that information is correct. So then the
act of.
New bank creation in cover base could be activity of well, the NDA is signed. Where
are we collecting the documents? Well, so that's what he's stepping through today,
that the process that we're talking about is...
We're launching Coverbase, and Coverbase is asking for the documents and
providing the answering the questionnaire that he just showed on the screen, but we
can pass that information from an application portal that y'all build and say, "Hey,
thanks, you know, here."
You signed the MDA. We need 3 documents to get started. Please upload these
three documents. Or...
Or an agent, AI agent on Vantage side could running databricks could get notified
like the IND is signed.
And here are the three documents posted here.
So those three documents get uploaded and a new account get created as a part of
an API activity. Yeah. So then you basically create the new bank in cover this, upload
the document, and even make it trigger a URL and send it to the people.
I think having the Rafa report already added in there would be one of those
automated steps. Yeah, and so I'm thinking.
I don't need to.
here in the process, I don't think that we have to provide them the URL to Coverbase.
I think that if we have the application to collect this information, then we push that
data to Coverbase, Coverbase doesn't say. And then you, so the external portal starts
to engage.
After, yes, yes, after the NDA signed, so we can create a portal, you say, I need these
three documents, and then you send those documents over to Coverbase. Coverbase
does their, you know, pre-fills in the information, and then you're just asking
questions up front, hey, is this information correct? Yeah, based on what Coverbase
found.
What is this information? Well, and currently, Cover Base is still going to have, you
know, 20 or so questions that won't be in the document that we either have the
portal display or we have them do it through Cover Base. Yeah, I'd rather have it not
surface Cover Base. I mean, like, give them one unified experience, and then you're
sending data over to Cover Base.
Yeah, and the back office works in Coverbase, so you use Corp is more like an engine
with an API, and then you host a much minimalized user experience for the due
diligence inside the portal.
And you are dealing to yourself from Coverbase as a vendor. Is that the intent? Yeah,
the back office would deal with Coverbase. Yeah. So, you know, I would see the
portal from, let's say, an internal employee side as just being a quick link into
Coverbase, right? Like, yeah, it's front end for my Coverbase. Yeah.
Call Kishi.
Diana Plata 33:36
But to his point, all this data or all these documents that are being collected are
being initially what stored in cover base.
FortWorth-MuseumPlace-Boardroom 33:44
Well, no, no, you can't think of it that way. If the starting point would be this portal
that we're creating, this application that we're building, it's going to collect the data
and send it over to Coverbase to do what it needs to do.
Diana Plata 33:45
Because I think that was that was.
It.
But any documents that we collect from the member banker or the applicant, where
are those going to live initially?
FortWorth-MuseumPlace-Boardroom 34:06
Well, when you're saying live, they're going to live in data bricks. Yeah.
Yeah, we're going to put, we're going to store all data in Databricks. Everything from
the analytics, the security, the documents, everything is going to live in Databricks.
So, so that's why to me it doesn't matter if it's cover base or why I want to streamline
it, but if...
If Coverbase is collecting this, then we're having to send it back over to Databricks. If
here instead, this process collects it, stores it in Databricks, and then I go tell
Coverbase, hey, here's the document, that's a better process.
Diana Plata 34:48
Okay, so initially all the data intake and documentation and everything that is being
received to perform due diligence on the member bank or the credit union is going
to live in Databricks, and then we're basically letting CoverBase know to go to
Databricks and...
FortWorth-MuseumPlace-Boardroom 35:08
Yeah, we need to do the assessment and then spit out the results of that assessment,
and then we're going to send that back over to...
Diana Plata 35:08
Okay, got it.
FortWorth-MuseumPlace-Boardroom 35:17
to the applicant so they can see and then they're going to verify is this information
correct.
Diana Plata 35:20
And.
Yeah.
Set, think.
Marie Alonzo 35:25
And, and just for clarity, too.
When they upload, the bank is going to upload all of their entity documents or is
there going to be some automation? I'm sorry, I don't remember who the gentleman
there in the room is. Like if it is a state filing, is there some connection that could be
done where those documents can automatically be uploaded without having the
bank upload every single entity?
Document.
FortWorth-MuseumPlace-Boardroom 35:57
Yes, that would be the hope. So if there's anything that we can collect from public
data or known data, then yes, we should do that. And so we'll need to map out a lot
of that. Obviously, my hope is that what we're saying now is being captured by AI
and then we'll use that to map out what that journey is.
Yeah, so that we can figure out where can we reduce this actual touchpoint for
friction.
Marie Alonzo 36:22
Perfect.
FortWorth-MuseumPlace-Boardroom 36:23
So if you have the external portal day one and the experience becomes self-service
after the NDA is signed, ops people don't get involved in catching the documents
and pushing it to cover base. So now beyond the people who need to monitor.
That cover these from a perspective of pay house that is assessment showing up.
Ops people that do not have to create the bank and upload the doc, that could be a
friction item, really eliminate if we follow this process.
That would be a process we want to eliminate right now. Yeah, I mean, yeah, yeah, I
mean, if we are building some sort of an external portal as MVP, then we might as
well as remove that friction of projects, yeah, yeah.
Anywhere we, as we being covered, this is a good API and ready to go, right? Yep,
yep, yes.
Diana Plata 37:15
Quick question, question real quickly. Two things. When you said ops, people
wouldn't be involved in creating that bank. Are you referring of creating sort of that
tenant within Databricks, right?
FortWorth-MuseumPlace-Boardroom 37:25
No, no, no, this is creating in cover space, but what Aaron just showed, where you
know, he's got to create a client and then you go through the questionnaire.
Diana Plata 37:30
Cover me, okay.
Got it.
FortWorth-MuseumPlace-Boardroom 37:38
We don't want somebody physically doing that. We want that automated.
Diana Plata 37:41
Excellent.
Okay. And then just a question, going back to the documentation that we're
requesting, the Rafa report and the Wolfsburg, that documentation gives us insight
into who has authority to request an account to go ahead and be open on behalf of
the member banks?
FortWorth-MuseumPlace-Boardroom 38:03
No, I think, well, I mean, Aaron will go through the whole process that y'all have
talked through, but the assumption would be this is just gathering information. This
isn't opening the account yet. So we will have to understand who are authorized
signers and go through whatever process is involved with that.
So this is just saying, hey, I'm collecting data. I'm collecting data of this bank. I'm
certifying that this bank is eligible and, you know, collecting BSA, collecting whatever
documentation I need, and then validating that this information is correct.
Yeah, Aaron, when we get to the reverse utility, so...
thought that, you know, I'm going to wait. Well, no, we can do that next. So I mean,
at this point, we are only working with regulated banks, FDIC insured. And so this is
our due diligence that as we if we open up to credit unions or foreign banks, those
kind of things, we'll need to come up with that process. And then for the reverse due
diligence,
What we built out here is on, with Vanta, we have a trust center where someone
comes in here and they click this request access button, fill this out, and then on the
back end, we would approve that request. And then that gives them access to just
download all of our documents.
theoretically should answer all their questions and that they would just upload into
their own systems if they're willing to do that.
I just, I expect that some banks will be like, "No, you have to go fill out all 100, like I
did that with last week, filled out all 126 questions and uploaded everything. We
didn't have this set up."
What's the process? I lost this idea. So why are we doing? Why are we doing
Menchaca? Banks are gonna come to us and say we want to do diligence. Backups
just a second, so...
Vanta is not necessary for what you're doing. I don't think that you need to be
concerned about Vanta because this is really, all right, great. We want to do business
with Vantage Bank and Hazel. Now we do due diligence on Vantage Bank.
I got it, so we might, I got it, we might show the screen as a step in the, yeah,
authorize the link, say, "Hey, you know, so, so they want to make sure that we are
good, yeah, so, so part of that workflow could be like exactly what Aaron just said,
hey...
Would you like to receive our due diligence package? If so, you know, and so there,
this I don't know, if Vendor has an API that we can automatically go in and have that
request and send that information out. For any pay, we can just have a link.
Yeah, for MVP, we could have a link. You know, maybe, because I don't know how
this will sort out in the future if it's a separate entity, right? We may have our own
SOC report and own data, then we have kind of third, fourth party data that we're
sharing. Well, and if you scroll down, Aaron, we can show that. So we've got our bank
stuff there, insurance, and then you can see.
basal network where we've got those things. We've got something there labeled
platform resources, so that's infinite. We may need.
you know, to just clarify all of that so that people can understand, okay, well, this is,
this is Vantage, this is infinite, this is whatever. We may have to add more things
there that, you know, are our additional third and 4th parties that we're adding.
Joel Olivares 41:44
Yeah, I think we can work on the labeling a little bit better, but Aaron, if you click on
view 15 more, I did add descriptions to all these documents, so it'll make it easy for
the partner to understand what the document actually has. But yes, maybe we can
provide this exact link here, and then instead of just resources, have it named, you
know, Hazel Network, so that all the data that's relevant to the Hazel Network, they
can download.
FortWorth-MuseumPlace-Boardroom 41:44
Dept it back.
Okay.
Joel Olivares 42:08
or request from that one link instead of going into the overall Vantage data
collection.
FortWorth-MuseumPlace-Boardroom 42:15
Yeah, obviously you need to.
Somehow, send the, "Hey, I want this user to be able to access it," and you know, so
that person in the portal will probably have to say, "This is who I want to review this
information, or I have access to this information." You put that in, and maybe MVP is
in the link, but maybe future is just embed the same portal like Jay did right here,
and then they've got it right there in front of them that they can.
Just click download all and send it to someone internally as well. Quick questions on
this. One is, how often does this change? In theory, it's supposed to change on a
quarterly basis for the documents, but in Vendor, there's additional information
shown there, which is real time.
compliance on the network. So Vantage is a big old portal that is scanning what
we're doing on a day-to-day basis. So as we configure, like let's say we turn off multi-
factor authentication on one of the critical platforms, it'll flag it as, hey, I didn't meet
policy. And so this portal will actually
change and show that that's not a check mark anymore. So it's a real-time dashboard
into our compliance with frameworks. So that was the first question. Thank you. The
second question was, we go deep into our onboarding process and then a bank says,
you know what, you guys failed our due diligence. Now what?
Yeah, so I mean, you definitely are going to have to have states and then the back
end is going to need a portal to say, here's the number of banks. So these are where
we're going to get some KPIs and metrics. These are the number of banks that are
currently onboard. These are current banks that are stuck or sitting in this stage gate,
things like that. So that way we can go reach out to those banks and go, oh, what's
going on?
Like, yeah, I mean, wouldn't we do this as pre-NDA activity?
No.
No. Well, I mean, it wouldn't be pre-NDA because we've got to provide this after
NDA. Yeah, this has to be brought after NDA. This is all very confidential, mostly
confidential. Right. And so, so no, I probably, I mean, because essentially this
workflow that we're doing is collecting our due diligence.
And then we're in turn offering our due diligence to them, so...
So, I guess if you really want to be technical, we're going on on two paths. We are
going on a good fit that, yeah, our due diligence right meets meets their
requirements, and so they they may in turn.
It actually brings up a good point. Maybe there in this workflow, there's a process
where we ask, is there any additional due diligence that you require of us that was
not met by this? And gives them an opportunity to, and we can track that
information, like what's being requested of us that isn't met.
And our goal is if we're asked for something by one bank.
We're gonna put it in the the the port the bank of portal, so that it's available to
everybody, because we we don't wanna have these ones, no, ones.
The what concerns me is 2 things: one, they brought up the hey, go fill out this form,
right? So maybe that's a theorem thing where there's an agent that takes this
information and...
Does the bespoke Excel or? In theory, Vanta is supposed to have that option. So
again, that's something that we probably need to spend a little more time with
because Vanta does have a way of answering those.
Third-party questionnaires for us.
If we haven't spent enough time with Vantage, definitely something we gotta look at.
The other thing we're making the assumption, and Jay, tell me, tell me off base for
Shawn.
That this is like a bank opening a checking account, and it feels like that we want to
make it like that, but what about the, hey, I need to my TPRM processes, I need Kerry,
Uvix, and Hazel, and here's my RFI, and you have two weeks, here's my RFP, you have
six weeks.
Like, yeah, what's the realistic, like, is that gonna happen, or we're not considering
that?
Because this is a core. I mean, it's a sidecar core, but you're dealing with ledgers and
customer accounts. And so I think that we...
I think it's a valid, valid, valid question.
But for the scope of what we're talking about today is really more about...
onboarding after we've already done this. And I know that we're hitting some things
as, you know, due diligence and qualifying customers, but that's part of just the
onboarding process. So I think we would still need to have an RFP response team
that would, or agent, or yeah, I was going to say maybe that's something that we.
Design, 'cause that that would kill us, yeah, like if we're doing cohorts of 50 banks,
we like, well, maybe maybe we add that as a tag out, so it's just like, like I said, once
we've been awarded, they just go click, you know, we just go click, yeah, yeah, but
then we have a separate process for if they require an RFP, then maybe it's a we just
split the like, hey, get started.
do you require us to go through an RP process? Yes or no? And then if so, then we
say we assume no, but yeah, I think they will let us know. I think that's a big lift. Yeah.
So I'd say we keep that as a side process. It definitely is something we would
probably want to build. We already basically built the RP. We just.
Yeah, I mean, I feel like we've done a big lift. We've done a big lift, but it's still a lift.
Yeah. And so now we would just need a future agent to say, anytime you submit an
RFI, the agent just takes the RFI and then spits out an RFP based on our information.
But again, I think that could be a side process, not part of onboarding right now.
Yeah, and because that stuff wouldn't touch any of the Databricks stuff, necessarily,
just a big slowdown and something that we gotta, yeah, yeah, no, but I think, yeah.
Hello.
I, I, I think Nathan.
No, I will. I've got, you've got, you know, David David's role, David Gonzalez's role is
AI automation and building agents as well, so like that's he can knock that stuff out
too, and...
OK, yeah, alright.
Yeah.
All right, so that's the reverse due diligence. Number 8, I think this is a manual step.
We want to do some kind of check on consent orders.
I just, I think that's public information, yeah.
So.
Is there a way to automate that? Probably not. I mean, they're website lookups. It's
not a database. And you would have to identify every regulatory body to go look up.
So.
Because, like, if you were looking us up, you'd have to go text the Department of
Banking.
You, if if it's an OCC regulated bank, you gotta go to the OCC and see if there's
enforcement actions over there. American, the ABA had something at some point.
remembers, but I don't know if they kept it up. Yeah, I don't know if there's a
centralized. Yeah, it used to be, but I don't know. I think they dropped it. Well, maybe
that's a side product. Yeah. Well, if we ask who the regulatory body is, and one of our
questions, which I don't think we have here. I know, I mean, we do have a lookup.
When we do the Rafa, ohh yeah, we're ready later, but there's an enforcement action
database from American banks.
Big.
Yes, maybe we use that.
and we're just okay as long as it's relatively up to date.
Okay.
Um...
See that, actually.
See, we're changing as we go. So the cover base will give us a score and you want,
what is that, a one to five or something?
It's a percentage. A percentage of risk. So it'll come up with, you know, this is 60%
risk. I don't know. It doesn't score. So we need a...
Joel Olivares 50:56
Zero to four.
Yeah, so it'll hold on just a sec. It'll score the risk domains by percentage, but
ultimately it gives you a 0 to 2.4 risk rating. So it could be a 3.3 or it could be a 2.1 or
a 2.0, but the risk domains will be scored by percentage. It could be a 60% complete
or accurate, you know, PSA policy review or any other, you know, risk domain, but it's
a percentage there and then it's a number at the end that ultimately risk scores the
partner.
FortWorth-MuseumPlace-Boardroom 51:43
So, with with hearing that, uh, and and Joel, I don't know if this is...
This is something that we would do. Would we, if somebody scores low, like we
determine there's gaps in their BSA program, are we going to then say, we need you
to improve your BSA program and these four things we need you to do?
That's a good question, Matt.
Joel Olivares 52:09
Yeah, so that's already implemented too. That's part of like the residual risk review or
the control set.
FortWorth-MuseumPlace-Boardroom 52:14
I know we can produce that. I know we can produce that. This scheme is something
that we are going to then require of the program.
Joel Olivares 52:18
What's that?
Yeah, the program.
FortWorth-MuseumPlace-Boardroom 52:24
Or is that does that just fall into like, hey, y'all, you know, that's between you and
your regulator.
Joel Olivares 52:31
Right.
FortWorth-MuseumPlace-Boardroom 52:31
Yeah, I think...
to keep the network healthy.
but to admit as many banks as possible and give the network healthy, we can offer.
Remedies, right, like...
But then who's the follower, like who's the authority to, right? And and and if we say,
"Hey, we suggest that you you improve your, yeah, your CIP," and they're like, "Great,
thanks for the suggestion," yeah, and then something comes through.
Is there?
a liability to us or to the network because we said, we made the recommendation,
they didn't follow it, we still accepted them and their transactions.
I think you quit like that. I would go back to what Clearinghouse or Zell or what are
they?
Yeah, and so maybe that that goes back to to our rule making and maybe maybe this
risk assessment that's done instead of doing it doing it across our our risk domains,
we're we're doing that against our rule book, yeah, yeah, basal rule book.
Joel Olivares 53:31
Yes.
FortWorth-MuseumPlace-Boardroom 53:43
That's a good point.
So everything you built in Coverbase, you got to redo Joel.
Joel Olivares 53:51
No.
FortWorth-MuseumPlace-Boardroom 53:53
You did it so fast. It's got to be easy. Well, I mean, we, you know, obviously, as we get
to building the solutions and we start walking through these, I think that's when we
kind of dive into some of these like underlying details of things we may have to
adjust or pivot on.
So...
Joel Olivares 54:09
Yeah, I think, uh, to to Shawn.
FortWorth-MuseumPlace-Boardroom 54:09
Probably don't have to solve all that thing, but...
Joel Olivares 54:12
Sorry, Sean, to Sean's point, I think as we go through this, we're figuring things out
too. So we can always develop a different intake form for trust, credit, and foreign
banks in the future. But the key is to know what we need to ask for and what we
need to verify controls onto. So
The actual back end work is not as difficult as it sounds, but I mean, other than it
being time consuming, it's very possible to adjust questions, add questions, remove,
add control sets, and remove that too. So yeah, the most important thing is to know
what we want to review and what we want to ask and risk rate that.
FortWorth-MuseumPlace-Boardroom 54:54
Shawn, how far along are we on building a network rule book?
It's hot.
No, yeah, I, we, that was the word stream that slipped. Yeah, ohh, I thought, I thought
John didn't finish most of that. Ohh, okay, then I guess I'm out of date. There was,
there was a product at some point, but with a lot of the changes, he he paused and,
okay, that became.
Seven.
Well, yeah, and a lot of that's designed to be...
But banks don't really have a choice. You're joining our network. Yeah. But going to
the point of where we make suggestions that they've got to address deficiencies in
different things, that's going to be part of the rule book that they're going to sign up
for. The rule book will set the terms and which will effectively say if you're not a well-
capitalized highly. Exactly right. You're not going to be able to.
That's where, you know, we can run that assessment, how well are they aligned to the
rule book, and then come back and say, all right, to be accepted into Hazel, you'll
need to address these five, 10 deficiencies in your program.
Yeah, that's something we can definitely explain to them, right? Right. Why are you
rejecting? Well, the rule book says X, Y, and Z. These is where we feel like you have a
deficiency. Please, you know, correct before we apply.
That's a good point.
Hopefully, we we we didn't lose you on all that discussion. No, I'm taking notes,
sorry. Yeah, so that's more of an internal system. So, other than that's like after
Coverabase has done its assessment and now it's a sitting, it's still part of the
onboarding process, assume that the rule book was there.
Then, probably after the automatic score comes out, the next thing immediately to
do in an automated way is, if the rule book existed, it go check against the rule book
or check, do additional checks in the rule book, and then a consolidated information
is then presented in front of.
the BSA team or the risk team. So now what? So that is a human in loop decision
point, right? Yeah, I...
Joel Olivares 57:12
So there's one step that's probably in reverse. The final score won't be received until
if we ask them to verify against, say, the Hazel rule book. So when we do a control
review or run it against the controls,
FortWorth-MuseumPlace-Boardroom 57:27
Play.
Joel Olivares 57:32
If they are non-compliant in some of those, we can always go back to the partner
and say, these controls are not compliant. We suggest you do this based on the
Hazel rule book, for example. Then if they don't do that, then we can close out the
assessment and they get their score. If they do do that, then we enter the data.
then they get their score and then that gets presented to the BSA or the governing
party.
FortWorth-MuseumPlace-Boardroom 57:57
Yeah, so thank you. So then, is that, so then what it feels to me that the rule book is
already there in cover base, right? So that, that for us in cover base, it's just a
different set of controls that it's looking against or integrating against, so.
We may do a risk assessment, and that risk assessment is really checking against that
rule book, and then we can spit back out and say, hey, these are 10 things that you
need to address before you can start transacting on Hazel. We can continue through
the process, but you're going to have to come back and show evidence.
that you've made these modifications.
And then there is the other conversation around Vendor and the other commentary
on rule book is, hey, we don't want to look at the rule book just at the time of
onboarding. Let's say everything was nice and fine, right? You start transacting,
you're part of the Hazel network, and now...
you're monitoring selectively frequency wise and referring and probably testing out
all the participants, right, all using some criteria based on the participation levels,
volume, etc. Let me check against the rule book of that near real-time check.
Again, it's a rulebook outside of the onboarding process. That's correct. And that is
the reason for a...
Let us treat it like a separate component, which can be called both at the time of
onboarding as well as a regular time. And that was a very good conversation. Did I
get it right? Yeah, I think so. I think that makes a lot of sense.
Joel Olivares 59:43
Yeah, that does. And that would be part of, Aaron didn't discuss it and that kind of
goes more into detail, but step 7 would be of the onboarding process would be
ongoing monitoring. So that would be a great example of cross-checking to the rule
book that part of the, they're doing what they're supposed to be doing.
FortWorth-MuseumPlace-Boardroom 59:47
Yeah.
Right.
All right, but...
It's important to understand, though, Joel, the rule book will have stuff that is risk-
based, but then also transaction-based, so that rule book.
Controls, we'll just call them controls, would also have to live outside of cover base
because you're going to have to have this checking against data bricks and the
transactions that are flowing through exactly what Kash just talked about. So
Joel Olivares 1:00:34
Right.
FortWorth-MuseumPlace-Boardroom 1:00:35
Um...
So, the ongoing risk assessment would have that that may.
That may have to be something in scope of the work that that you guys do, but
somebody does, and then maybe just as a, yeah, I mean, is the decision of.
Build versus buy already done. That's what I was trying to figure out. And is it
relevant for the MVP? Yeah.
Oh.
Marie Alonzo 1:01:07
Quick, what happens if a bank?
Through this ongoing monitoring, a bank doesn't meet the rules. What what what
are we doing? What do we what happens to that bank and their transactions?
FortWorth-MuseumPlace-Boardroom 1:01:24
Well, if they're violating the rule book, we would have to have some sort of
procedure saying, yeah, correct this or we will need to be able to stop your ability to
transact. Yeah, depending upon the severity, we need an immediate kill switch or you
may want to warn on that.
Marie Alonzo 1:01:24
It.
FortWorth-MuseumPlace-Boardroom 1:01:44
Cell has like penalties, yeah, I mean, yeah.
Yeah, I forgot to talk about stuff like that. Yeah, there may be penalties, there may be
fines.
Marie Alonzo 1:01:50
Yeah.
FortWorth-MuseumPlace-Boardroom 1:01:56
before we cut them off.
Marie Alonzo 1:01:59
And is there a number of days before we can cut them off?
FortWorth-MuseumPlace-Boardroom 1:02:05
Paper.
Marie Alonzo 1:02:06
There's A requirement.
FortWorth-MuseumPlace-Boardroom 1:02:10
Yeah, we'll define all that in the rowbook, which...
Need to go with Jonathan on the work stream, because I think that's gonna take a.
Chris makes a good point too. What if they're not a bank and do we have any ways
to detect or prevent, you know, bots and other things signing up, trying to set up our
network? So good thought on the security side. Yeah, I feel that there would be
some sort of off process where, hey, put in your e-mail address.
Then we're gonna verify that it's a bank domain, a bank domain, um, and then...
Give them a link to to click to come back and.
Multi-factor, basically, that is also one thing, and then if somebody just wants to
attack the network.
And uh, wherever application, yes, all application security, exactly, I will everything to
do that, like the external reporter will be a well-known people won't wanna do that.
We can put a banner across the top that says, "Don't do that." Well, and you know,
we probably want to stick it behind Cloudflare or something like that, yeah, it will be,
yeah.
So, that'll probably solve some of the, yeah, like, is it coming from Russia type of a
thing, but, but to to, yeah, and so we will need to restrict countries initially.
Um, and we can talk, you know, on a risk level, if if that includes time.
So on the next stage, we just need to define kind of what our decision criteria is. We
have a few things listed here to answer your earlier question, Marie, on what would
trigger deeper reviews by our subject matter experts. So it could be one of those
Rafa scores we're watching.
We noted low liquidity, but we don't have a definition of what low liquidity would be.
But a prohibited business type in Wallaceburg, a consent enforcement action found,
and then whatever our approved threshold is with the cover base score, if something
was below that.
And so that's where we would go to a new stage of a deeper due diligence where we
may pull in the credit, BSA, ML, IT, cyber, legal finance to do a deeper review. So
that's where I assume all that would be manual if something happens.
But over time, we might be able to automate some of that, so...
Um...
And then at the end, we'll have some kind of approval package with the cover-based
score. And again, we haven't written the auto-approval criteria, but that'll be part of
this.
We should finish the due diligence.
Marie Alonzo 1:05:13
Would a bank merger or acquisition also trigger an event for a manual review?
FortWorth-MuseumPlace-Boardroom 1:05:13
Thank you.
What do we have? What do we bring to you all? Something about the what's
happened in the past three years or your Navil Bank or?
Joel Olivares 1:05:29
Yep, that's correct. I think it has to be minimum three years of being at BIC. Also,
there's a feature in CoverBase called Radar that tracks lawsuits, litigations, mergers,
acquisitions, all that stuff. So if a partner that we've already onboarded to the Hazel
Network gets
triggered through one of these searches, the daily searches, you know, we would get
notified. So then we could approach that from a different, that would be part of the
ongoing monitoring from the due diligence perspective, not so much the.
The other side.
FortWorth-MuseumPlace-Boardroom 1:06:06
Joe, did I hear you right that you said that we won't?
that it's not going to allow or it asks if you've merged or you're in Tenovo Bank and
you got to be at least three years. I mean.
Some, some of these.
Trust companies that that we're talking about partnering with, like Ripple, won't be.
Charter financial institutions for three years, so they'll be.
Joel Olivares 1:06:31
Oh yeah, but we haven't gone into that part of the intake, Jay. I think we're just, the
only intake that I've configured is for FDIC banks. So definitely if that needs to
change from startups like Ripple, then the intake or questionnaire process would
probably be a little different than it would be for a standard FDIC.
FortWorth-MuseumPlace-Boardroom 1:06:37
The.
Joel Olivares 1:06:53
So that's probably something we can discuss on what the minimal requirements
would be. Or to check against, right? It's part of one of the controls.
FortWorth-MuseumPlace-Boardroom 1:07:03
Thanks.
And Marie, I owe you and Sandra, a response you sent me that CIP document, the
key questions you asked there, and we worked those into the cover base questions
that you all created. And so I'll send that over to you guys just so you can see what
we did there.
Marie Alonzo 1:07:24
Thank you.
FortWorth-MuseumPlace-Boardroom 1:07:28
So again, we want to automate approval. We needed to find the correct criteria
exactly, but kind of walk through many things that we're looking at. Aaron, can you
pause for a second? Yeah. So what? Let me share something.
When we do.
based portals, depending on how they're configured, there is the ability to AI auto
fill.
The information that's being requested, the questionnaire with with the documents,
so...
As we're talking about things that the applicant's gonna want to fill in.
It would be great if we give them the option of uploading a document that answers
those particular questions.
Um, because I will speed up time, so if...
I don't know exactly everything that's on the questionnaire, but if they've got
something that's already prepared, why are we gonna make them retype that in? So,
just, you know, think about ways that those are all AI-enabled, you know, product
integration, yeah, how to be discussed, 'cause like...
Those might not be available out-of-the-box if you're trying to make it as a portal or
API outside. But definitely, if that's something which we are trying to stick around as
a port, like cover base, we are saying like, hey, that is going to be my port, then we
can discuss with those guys, checking like can the AI.
Be exposed to the, yeah, well, and and so even if it...
Even if it can't be exposed, then we can build it. Right. If you can build it part of the
application process, you know, maybe they've got, you know, a PowerPoint
presentation that already did this for something else, and they just say, well, all the
answers are in this document. Upload the document, auto-fill in.
Does this look correct to you? Because as I've been onboarding programs into our
fintech, into our embedded banking program.
All of them have commented that they appreciated and loved the ability to just say,
oh, crap, you're asking me 120 questions. Well, here's 3 documents that have all
those answers. Here's 3 documents, and then hit the button, AI autocomplete. It's
nowadays easy. The only thought process is.
I will have to.
Now that AI calls to the data fix layer, we want to make sure that we want to make
sure that.
Make sure.
Ohh.
Cost implications of that a little bit, but you are not onboarding. We're not talking
about hundreds of thousands. I, I don't see much issue. I mean, cover bases, we can
upload it from our side, they can do AI on their side, or we can, yeah, and then you
bring it back, or we can, we can actually extract out.
bulk of the information. So instead of just saying, hey, add this bank, here's the meta
information, and here are the documents, you do the magic, or we simply do the
magic on this side.
convert that response into a JSON payload which matches exactly to their API.
OK, and Coverbase has been really, really good in the fact that...
When so when they do their assessments or their questionnaires and they collect it,
they have they generate a spreadsheet that maps the question to the answers to the
control set, and then they throw that as a file in their document list. So now I have
those answers to that.
That questionnaire sitting there, and then I can re-injust that into new questionnaires
that I put together, and so it gives me the ability to constantly use whatever they've
provided over and over and over again. Yeah.
I'm not worried about that, yeah.
Marie Alonzo 1:11:48
What?
But in Jay, to your point, that would be the expectation for us is to automate as much
as possible to have those questions answered and then reduced to whatever is left
based on the documentation not being able to provide. So that would be the
intention.
FortWorth-MuseumPlace-Boardroom 1:12:10
Yeah, and I started thinking about that as you spoke, Marie, because then you were
saying, well, these are the things that we ask in the CIP doc or whatever, you know, as
much as.
They don't have to fill in information, I mean.
Do that for them.
Marie Alonzo 1:12:24
Right, right, right. On board with that.
FortWorth-MuseumPlace-Boardroom 1:12:30
Adam, these are the only four phases we have it, or we have few more? Dom, he's
got more. This is two of two of four, we're on page two of four.
I feel like we've gone through most of the heavy.
Have your stuff.
But on approvals, what do we need, Joel? Like a...
just a report from this portal of here are the banks that were on boarded this week
and just so you can show it to the Burke committee or just kind of a list. This
awareness score. Yeah, with their score and maybe if there are details.
Joel Olivares 1:13:08
Yeah, that could that could be arranged.
FortWorth-MuseumPlace-Boardroom 1:13:11
Yeah. So that will be something for... Well, are we going to continue that process? I
mean...
across the board, because I mean, it's going to be out of Vantage at this point. Oh, I
mean, yeah, they're going to make some governance somewhere, right? Yeah.
I, I would say the process continues, but it just has to work.
Yeah, I mean, I don't think Hazel would be taking that too forward for every single
bank for hundreds of banks. I think if they're within the operating rules, yeah, yeah,
yeah, this would be retrospective, like, use someone said earlier, pipeline, yeah, I
think it's more of a dashboard.
Here's where everybody's at, here's the stages, your banks were rejected, your banks
were accepted.
Joel Olivares 1:13:56
Yep.
FortWorth-MuseumPlace-Boardroom 1:13:56
Of.
Okay.
Well, that would be handy just for our onboarding specialist or whatever the role is
to go and be like, oh, hey, I've got three banks and I've been sitting in due diligence
for two weeks, so I'm going to reach out. So that kind of dashboard view, yeah,
would be.
Joel Olivares 1:14:09
Right.
And that will happen, Aaron. I mean, I know that will happen. So I think so far, the
one thing that I think we need to hone in on is what that score is going to be before I
can say, well, this was rejected because it was a two or this was, and keep in mind
that a two would be like a percentage of 50%, right?
FortWorth-MuseumPlace-Boardroom 1:14:13
Yeah.
Joel Olivares 1:14:32
So if we can identify that number, then it'd be easier to say these are, you know,
technically automatic approvals and these are, you know, review, additional review
required or these are automatic rejections.
FortWorth-MuseumPlace-Boardroom 1:14:42
****.
Well, but I mean, here's the point, you know, we talked about it's going to be less
than 1% that will be automatic rechecks. Everything else, in theory, we're going to
have either...
rule book requirements that they need to meet before they can transact, or two
capital requirements that we may impose on them for reserves or whatever it is. So I
don't think that there's ever going to be a, like, just a, you know, a group of people
that were like on the fence, like, well, I don't know, maybe, maybe.
I mean, the tool, the AI should be able to say either, you know, these are the hard
and fasting rules of they didn't meet that. You need to correct these to start
transacting. We can create your account, but you can't do anything yet.
Joel Olivares 1:15:38
No, yeah, I agree. That's correct, Jay. That's exactly the process.
FortWorth-MuseumPlace-Boardroom 1:15:38
And then go through and talk about capital or whatever those other criteria are.
So, throughout this process, let's assume this is automated, but there would be
humans in the group, and the human in the group may have an SLA which, so this is
just at a surface level, it feels like this is not like a shopping cart kind of a thing, right?
You upload something and voila, you have it, it's not, right? It's not like setting up a
recipient, a recipient in a cell.
right when you start transacting. Exactly. So is there any servicing expectation? Is
there a call center, calls that will come more or less? Do we need to send some
updates so that you don't want to take calls?
That is a really good point, and we we we don't have that today, but we we've gotta
set that up.
So then we'll have to figure out.
a state machine or a journey map which is internal versus a summarized journey map
which is external. We don't tell everything. Right. So maybe that's where you've got
your Teams app, Teams agent that sends a notification to that.
that team that says, hey, this prospect is, you know, you know, is lacking these things,
reach out, you know, get this squared away.
Yeah, and then they can work the internal portion, internal companion of the external
app. Got you.
Okay, yeah, I mean, because then at that point, you...
Exactly what Sean mentioned, you have dashboards that you can see that pipeline.
Yeah, you'd be able to see what those exceptions are.
And if you've got to reach out and say, oh yeah, I see that, you know, you ran into
this issue with, you know, 3 exceptions. We can solve those really easily with this or
this. We can send you a sample document here to address this, or we need a board
resolution. Here's an outline of what you need.
Shives.
Are you OK?
Diana Plata 1:17:55
And that's during the approval process or before they're approved, Jane, is what
you're saying.
FortWorth-MuseumPlace-Boardroom 1:18:00
Yes, get this document so that we can read offline. Yes, that will make the.
I'm assuming everything that is being shared over here, we get to see, yes, yeah,
yeah, copies of everything, ohh, yeah, yeah, that is true, but right now, yeah, ohh,
yeah.
And so your question, Diana, you're like, would there be any scenarios where a bank
may not meet the criteria and their approval is still granted? I think that there would
be, but we wouldn't allow them to transact until those exceptions are cleared and
accepted.
So again, it goes back to the, I think it's going to be less than 1% that we're rejecting.
Everybody else is going to be approved, but there may be some that are approved
with conditions. It's like a new status. Yeah, approved with condition.
Diana Plata 1:19:01
Yeah, and I was I was honing in on on your question related to Ripple, right? I mean,
there, Joel started talking about the three-year mark and things like that. So there
may be some some of those situations, mainly versus, you know, they're on the
watch list or whatever the case is. I'm thinking about those situations.
FortWorth-MuseumPlace-Boardroom 1:19:08
Okay.
Yeah.
Diana Plata 1:19:21
where they're a good candidate, but our criteria shows A, B, and C, and they might
not meet that.
Joel Olivares 1:19:30
I think we should clarify a little on the three years. The 3 years is for mergers,
acquisitions, or material restrictions in the past three years. It doesn't mean that the
bank has been in existence for more than three years.
FortWorth-MuseumPlace-Boardroom 1:19:44
And that's fine. I mean, we know there's going to be different different questions or
different things, just using that as an example. So, and again, too, I would also
preface this with, you know, this will have its own governance process within Hazel.
Joel Olivares 1:19:50
Okay, got it.
FortWorth-MuseumPlace-Boardroom 1:20:03
may not exactly reflect what Vantage is doing today. So, you know, let's try to keep
that in mind too. Vantage will, you know, effectively, you know, potentially just
become a, you know, a sponsor bank to Hazel. And so you'll be doing your due
diligence will only be on Hazel itself. Hazel will have its own governance.
processes outside of that. So I don't want to lock us to too much what we're doing
today.
Not that we won't replicate some of that. So maybe we have it, maybe we don't have
it, but so at the macro level, these four phases thus far look fairly straightforward,
common sensical to many other banking processes. Is there...
like a tech table saying, hey, in phase one, these are the departments or the functions
from Vantage that would be involved. Is there a kind of a stakeholder mapping?
Yeah, I think we need to do that stakeholder mapping as well as integration touch
points.
So...
And then we know, okay, which human integration and system integration sets
where.
Okay, so Aaron, so you just walked us through the approval phase.
Yep, so now we're set up. So right now, Infinite requires a, I call it a configuration
workbook, it's just a spreadsheet, some details that we send them to create a new
tenant for the member bank. And so at this point, there's nothing unique about this
for.
basic banks in our pilot. So we just, basically we tell them, hey, just copy the last
tenant and create a new one for us. So we're trying to simplify it. They told us this
takes 2 weeks. And Aaron, I'm sorry. So you're jumping to phase five, right? I mean.
No, 15, 15, 15, yeah, OK, so...
So yeah, I was explaining the process now. So at this point, if we have a new bank
boarding before due diligence is complete, I think we can send this to Infinite, have
them create the tenant for us. Their tool, their software is called Interlace. And
And again, there's no specific setup for this. In the future, we have been told from
their CEO that we will have API access so that we can do this ourselves. So whether
that will be ready for MDP or not. We don't know.
And I think this is what I was talking about as a technical setup. You know, we're
finally there. Yeah. And I've got a few things here listed and we're, again, we're still
kind of refining the setup. But yeah, which users will be accessing it? We have a basic
list of operating accounts that each bank will give. They may want to add to it.
do that. We only have a few rails that are live. We'll be adding that. So in the future,
they might be able to pick and choose on.
And then Participate is a part of with ours that can automate payments for people.
So they have a network of about 600 banks that they already do this with. And so
they are going to be a service provider inside of Infinite and will also be a referral
source. So they will come to us and say,
Hey, one of our banks wants to join Hazel, and we will be their partner with inside of
Infinite to help to automate those payments. And then we'll have other banks in here
who don't know what participate is and participate will have. But they do have loans,
right, tokenize loans only, right? So they have, so in this particular...
In this particular setup, there are rails provided.
Now, this is more of a technical setup, so if if a bank is a users participate, we can set
them up to so that they can settle their their transactions with with participate
through Hazel, so it's just a an option. I call you.
Diana Plata 1:24:23
Yeah.
FortWorth-MuseumPlace-Boardroom 1:24:38
Just so that, hey, this is participating, so we are we are working on this participate as
well as part of Hazel. Well, you're using, yes.
Diana Plata 1:24:45
Participate is a service provider, not a console, not does not have an account
established within the Hazel. They're basically a service provider and we receive
authorization from the member bank that wants to go ahead and join participate. So
participate can basically debit or credit accounts.
FortWorth-MuseumPlace-Boardroom 1:24:48
I.
No.
Diana Plata 1:25:05
And then Hazel.
FortWorth-MuseumPlace-Boardroom 1:25:05
Okay, yeah, it's just you're saying I have one new integration. That one integration is
participate and we can pre-configure that integration for them. Basically, participate
refers the bank to us. We set them up the exact same. The only difference is
participate then now needs to know, okay, what?
Accounts are we allowed to use?
Diana Plata 1:25:27
Yes.
FortWorth-MuseumPlace-Boardroom 1:25:29
So it's just a small, it's a flag in the configuration.
I do have a question overall here. So, Shawn, is the assumption that they sign up for
Hazel, they're going to get all of our payment rails or all the payment rails are
included with that?
Yes. Or do they check off, I want this, I want that, I want that.
We would provide all options, but I think the bank would make the choice, be my
assumptions or anything. I only want to...
wires and so is that something on the onboarding that they? I would think so,
because we also have to like figure out limits. So the thing that, you know, Diana is
doing right now or we're doing is there's this whole spreadsheet configuration thing
that we send to Infinite. We would have to give you guys that. Infinite would have to
work with us to figure out.
How do we even configure this? But we're setting, here's the product you're going to
have, here's the limits you're going to have, here's right, Jan, maybe you can kind of.
Diana Plata 1:26:35
That's right. That's right. There is an overall program limit and then at the account
level and things like that, we would work with the bank to go ahead and establish
those, not to exceed that.
FortWorth-MuseumPlace-Boardroom 1:26:46
Yeah, the program, as an example, is something that Bank Vantage or Hazel would
set and say, this bank is this risk profile, this is the limit that we set for their initial
onboarding. And then the bank would set their own limits within their own products
and so forth.
Diana Plata 1:26:46
Up.
Question real quickly, Shawn, on this, because we said Hazel refers some banks to us,
right? Do those banks that are referred by Haze, but not by Hazel, by participate,
they would still go through the whole process that we just talked about regarding
onboarding and things like that, right?
FortWorth-MuseumPlace-Boardroom 1:27:14
Summer.
Yep, everything is the same for that bank. The only thing is, is that it's, you know,
what we would probably want is participate would be, hey, pay by Hazel, and it's
maybe grayed out in their system. It says, oh, you're not set up yet. Click a button to
onboard it, just send it to our onboarding portal that they get going. And then
there'd be some, I'm assuming this is future.
Diana Plata 1:27:21
Yeah.
Yep.
FortWorth-MuseumPlace-Boardroom 1:27:40
right? There'd be some web hook back to participate that says, hey, by the way,
they're done onboarding. You can now enable them. And here's the information you
need. So really, once that bank onboard and we know that they came from
participate, we just need to eventually inform them through some process. So we
don't have to do that MVP. It's just
So, but I'm thinking like kind of anticipating future partnerships like this, that it
probably need to be a screen in the onboarding process where they could, you know,
re-show, you know, are you a member of participate? You know, and then they can
check the box to enable that.
And then we can have some sort of little. Oh, it could be directional. And then we
found them and then there, like, you also participate. Right. And then there could be
other networks or groups that we integrate. So if, so, so, so there is a chance that you
could have a bank coming to you.
Who is also a participant member, right? A participant has not yet referred them,
exactly right. Yeah, and it doesn't make a difference to us. I mean, we're not, yeah,
the participant doesn't get a, you know, a referral fee, so to speak. It's just we want to
be able to integrate, and then they can settle their payments.
If it is a slight tangent, so my understanding was participant is able to do what
they're able to do because they're sitting on top of Hazel. Yes. Yeah. They're just
basically sending us payment instructions. And all participant needs to know is, are
they in Hazel enabled? Yes. And if they are, then what are the accounts that are
authorized?
Find that bank. Does participant have a business model which does not use? No,
today it's just us.
This is the way I would think about it, right? But then if that's the case, so what is the
referral agreement all about?
So, if, if...
That's just to get us banks onboarded. So the network has to grow and we need
someone to, they're basically our sales team effectively.
What is your question? My question is, if participate as a business model is only
possible because Hazel is underneath it, then by that logic.
Well, so that is not, if you're a participant member, you're automatically a Hazel
onboarded, but yeah, but that's not not the scenario, so participate does loan
participations without Hazel. That's what I was trying to get to. Ohh, now I get, they
have an existing business model, they're they're in production, they're doing that, but
I, that's what the question was.
I got, so, so yeah, I get, I get it.
Yeah, and so we may have other partnerships later, yeah, where we say, "Hey, you
know, we already have a pre-integration with so-and-so and so-and-so and so, so
they can say, 'Yes, integrate that, and now I can I can settle between these two
parties, so I can, anyway, there's settlement needed, yeah, yeah, I'm just gonna use
the...
Yup.
Broecke you example.
You sign up for Road Go, it's like, okay, open your account. What do you want to do?
And do you have any of these other like TV partners or providers and you check the
box? All right. I want HBO Go and I want Netflix. I'm just going to click those. Yep, I
participate. Okay, I want that. So that's kind of the marketplace idea down the road
where they go, yes, I want to be a part of these things.
or integrate or turn these things on. Again, it doesn't have to be their day one. I think
it's just something we add as like optionality in the future for how that flow works.
Yeah, we're trying to make a very fintech kind of like experience, even though banks
are not used to this. It's going to be very foreign, foreign to them, but I think that will
also add a lot of novelty to what we're doing. Are we going to offer an ad-free
experience? The right price, yeah.
Basil plus. Basil plus. I like it. Love it.
Just before we go on, I know we've been on for about two hours now. Do we need
any, maybe a 5 minute break? Five minute? Let's take a 5 minute. All right,
everybody, let's take a little 5 minute, you know, bio break, drink break, whatever that
might be, and then we'll come back and then kind of move on to the rest of the
technical provisioning. Does that sound okay?
Yes.
Check out my full slides here, your full slides.
Yeah, I'm gonna, I'm gonna send it to you. Yeah, you figured it out. I saw him do that.
I was trying to use my AI to send it to you, but I don't have a good one on my phone.
You may already have this, but I sent you a link. I was just like, well, maybe it'll be
more visual if you know, instead of the word doc. Oh, you created a...
Hey, thanks.
I think did a pretty good job, actually.
Got the substated between one with the stakeholders you muted.
Just so the AI reporting is.
Okay, everybody should be back started. It took a little bit longer than we thought,
but Aaron's going to get us rolling again. So Shawn created a deck of the Word doc
while we were meeting, so this is a lot prettier. See all our steps. We've already gone
through some of these.
Claude, huh, Claude? Oh, yeah, yeah, Claude's getting pretty good at that stuff. It's
not me, I have nowhere anywhere good at putting these kind of cool presentations.
So.
You converted it into a skill? Not yet, no. Yeah.
So, and I did, Jay was writing, I did kind of jump the gun a little bit on this, collecting
the setup for the config workbook. In the beginning, we thought that was going to
be questions we were going to need to ask the banks, but really, I think we know
what we need to know. We just need to send it to Infinite at this stage. So the other
two pieces are similar, but it's basically
We need signatures. So account opening package is similar to what we've done with
correspondent banking partners in the past. We've tried to trim that down so we
have kind of five PDFs that we need signatures from. Some of them are...
Just an acknowledgement, but we we haven't had to do this yet, so initially I think
we're probably gonna send it manually, or we're gonna use eDocs to get those
signatures, potentially prelim, that's and prelim would be, yeah, the other option. So,
well, in that case, I I mean, we we obviously sat through the...
the demo with DocuSign as far as how they have that workflow for the e-signatures. I
don't know what prelim would get us over just using DocuSign at this point. I mean,
because if we're building the app, where are we going to bring in another third
party? Yeah, well, yeah, it would only be more around.
They've got multiple branching, beneficial ownership questionnaires. They've got a
lot of things that we've already built to ask those things. But that's a good question.
Yeah. Johnner probably sees that more than anybody. So I mean, I think that. Yeah,
so. Is Diana back? She might have more contact on.
Diana Plata 1:49:26
I'm here. I'm here. Marie is here as well, because she's the one that has been helping
me open them up through.
FortWorth-MuseumPlace-Boardroom 1:49:30
Yeah.
Diana Plata 1:49:36
So going back to just step one real quickly, so that we wouldn't need to go out there
and send it to the member banks. I do think we need to go ahead and get some
feedback from them, because we would hate to go about opening a bunch of
operating accounts, like, for example, we did for custodia, when if the intention of
the bank is to, in essence, hold
FortWorth-MuseumPlace-Boardroom 1:49:36
It's very much like opening a business account, you know.
Diana Plata 1:49:57
I don't know, just an operating account for business, things like that. We want to
avoid opening a lot of accounts that they have to manage on the back end, that
those operating accounts would then tie into consumer products and things like that
that are not necessarily needed at this stage. So we would have to identify some type
of communication from that bank.
of what type of products they're looking to open. So we can go ahead and set those
operating accounts up for those specific products and not additional accounts that
are not going to be needed. So that's the only thing I would change on this, Aaron,
on the collect setup and configuration workbook.
just at that ask from the member banks.
FortWorth-MuseumPlace-Boardroom 1:50:41
So if we're talking about the basic tier, the quote un quote turnkey solution, I mean,
isn't it, isn't there just like a set of accounts that will be created and operating at a
reserve or whatever it is?
Diana Plata 1:50:55
Well, that's what you think, but if they're cloning the tenants that we have today,
which is what they're sort of doing, they're basically cloning it with everything that
was already established. So we would just need to make sure that Infinite doesn't
continue just clone what we have out there and added it, you know, because that's
what we're seeing with just like the setup for custodian, right?
Marie Alonzo 1:50:56
Okay.
FortWorth-MuseumPlace-Boardroom 1:51:10
All right.
Diana Plata 1:51:15
And then as a member bank, because those accounts are open, they have to go out
there and disclose that and manage that and things like that, even though there's
not transactional. So we want to ensure that we don't give those member banks
additional work.
Marie Alonzo 1:51:28
Right.
FortWorth-MuseumPlace-Boardroom 1:51:33
Okay, so what is the minimum number of accounts?
Diana Plata 1:51:37
It's one USD reserve, and then again, if you're going to go out there and process,
open an operating account for a business and transact under a business, in essence,
that's all you would need, the USD reserve and the business operating account.
FortWorth-MuseumPlace-Boardroom 1:51:38
Basic.
But for their, the business operating account is for the bank or for an end user.
Diana Plata 1:51:58
No, we're not doing end user accounts. It's for the bank.
FortWorth-MuseumPlace-Boardroom 1:52:00
Right, I know that. So, that's what I just wanted to clarify. So, at a minimum, they
need two accounts. They need an operating account and a reserve account.
Diana Plata 1:52:08
Hmm.
FortWorth-MuseumPlace-Boardroom 1:52:09
So to me, that should just be part of this workflow and then any other accounts we
do outside of this workflow.
Diana Plata 1:52:19
Yeah, the only thing that we need to figure out though, Jay, and confirm with Infinite
is that member bank, once they have access to the console and things like that,
they're going to have the ability on their end to open additional operating accounts
if needed, which is fine.
The configuration that Infinite is doing in the back end, would all those accounts that
they're opening tie back to that USD reserve account, or do they need the additional
operating accounts that they're setting up today to go ahead and tie with those? So
those products, we would need to look at what products we're going to go ahead
and make available to that member bank on the front end.
to have the ability to open or not to open.
Because there's a lot of configuration on the back end, and there's a lot of accounts
that are open by Infinite on their end, which they they that we need to understand.
reason for them? If I may, like, is there a reason for them to open, I don't know,
commercial non-interest bearing? Does that tie to the product of, you know,
operating account non-interest bearing? And if so, then they would have to set it up
from the get-go in the event that the member bank does decide to go out there and
open operating accounts of those nature in the past.
FortWorth-MuseumPlace-Boardroom 1:53:37
Chad.
What was the second account you said, operating account and kind of reserve?
Diana Plata 1:53:43
And a USD reserve.
Marie Alonzo 1:53:47
And just for a little bit of clarity, what I guess maybe what I'm not understanding is...
Today we open up the account in BPM for Diana. So where would that, what would
that platform be or where would that automation be to set up that account and the
account number?
FortWorth-MuseumPlace-Boardroom 1:54:11
Go, Sam.
Diana Plata 1:54:12
Yeah, so it would no longer be BPM, Marie. It would have to be on infinite.
FortWorth-MuseumPlace-Boardroom 1:54:13
That, that would be somebody.
Marie Alonzo 1:54:14
That.
Right, right, right. So, but you know, we, I guess you talked about Jay, you said
something about DocuSign, but what would, what would be the platform to open up
the account?
FortWorth-MuseumPlace-Boardroom 1:54:28
No, that's what we're going to configure to do that automatically. So through an API,
they'll be on infinite. That's the goal. But what Shawn just shared was that infinite's
not quite there yet for us to set up the whole, well, actually, no, no, no. At this point,
we've already set up the.
a tenant and so these are just the accounts. So these we can open up with an API.
Diana Plata 1:54:56
No, at this point, the slide that you're saying, we haven't set up the tenant. We're
gathering the information so we can set up the tenant and the accounts.
FortWorth-MuseumPlace-Boardroom 1:55:00
Of.
So then we're setting up the tenant and the two operating accounts, Marie, and
that's all done on Infinite. So Infinite would be doing that for us initially, and then
we'll do API once that's fully available.
Diana Plata 1:55:19
Yeah, but I think what Maria is asking is because we don't have those documents that
the, like, for example, prelim or BPM spit out today regarding signature cards,
disclaimers, agreements, right? And correct me if I'm wrong, Marie, what would she
have to do on her end to ensure that the system auto-generates that and we would
have them available to send them?
to that member bank to sign and return, or is our ask not to use prelim and have that
documentation fillable and have to fill that out and send it to the member bank via
DocuSign.
FortWorth-MuseumPlace-Boardroom 1:55:52
See that.
Marie Alonzo 1:55:53
Yes and no. Yes and no, Diana. Jay was right in answering the question that I had. But
to your point, what is that triggering event that is going to open up that account? So
today, it's a manual collection process.
we ensure that we have all the required documentation, and then that's our
triggering event to go into BPM and open up the account. What would be that
triggering event from, and forgive me because I'm just learning all the needs, but
cover base then going to Infinite and opening up that account? Because it has to be
a triggering event or something that says,
FortWorth-MuseumPlace-Boardroom 1:56:25
But that.
Marie Alonzo 1:56:33
We've gotten everything we needed, now we can open up the account.
FortWorth-MuseumPlace-Boardroom 1:56:38
Right, so that's part of this workflow that we're designing. So we're collecting the
documents, we've done the risk assessment. And I'm sorry? And approves. And yeah,
all of that's taken care of otherwise. Yeah. And so at that point, we're confirming
through that electronic workflow that everything has been collected and ready to go.
We can fire off, you know, an inline signature capture and e-signature capture, and
then once that's submitted and accepted by the app, then it can create the accounts.
Part of the reason I mentioned use of prelim is, we've already spent a lot of time, you
know, building out those journeys, those collection processes, those documents,
main thing is just, where does, you know, where does it actually put up the account
once it's done? So, you know, we either, I think, use what prelim is we built for prelim
today for the business side, and because there's a lot of branching logic, you still
have to do...
beneficial ownership checks and all these other little things. As far as opening that
account, it's already presenting the documentation, it's already doing a lot of these
things. It's got multi-stage capabilities where it says, hey, you know, Shantanu is one
of the signers, Jay is one of the signers, I need to send it to him and send it to him
and get it signed. So there's a lot of those little nuanced details that I think
Marie Alonzo 1:57:44
Mhm.
Mmh.
FortWorth-MuseumPlace-Boardroom 1:58:00
we would spend a lot of time on it if we rebuilt it ourselves. Doesn't mean AI is not
possible to do that because it could totally probably just walk itself through the flow
and do it. But the question is, should we? I mean, I think that's the bigger question.
Marie Alonzo 1:58:15
Yeah, and that's to Diana's point about the deploying of, you know, after the account
is open, how are we going to capture those signatures?
FortWorth-MuseumPlace-Boardroom 1:58:24
And is prelim be able to do your own UI, keep the same look and feel, or would it be
is having an SDK?
Diana Plata 1:58:24
Well, and not only that, Marie, not only that, the
The documentation that we've collected is more to approve the member bank to join
the network. So we would need to identify what actual documents we need from the
company to identify who signers are, like the documents we were talking about
earlier today.
FortWorth-MuseumPlace-Boardroom 1:58:35
Bing.
Marie Alonzo 1:58:37
Okay.
FortWorth-MuseumPlace-Boardroom 1:58:38
I got it.
Marie Alonzo 1:58:47
Sure. Yep. No, you're absolutely right. That what we get from the operating
agreement or company agreement or even some bylaws, who is authorized to sign
on the account, who is authorized to open up the account?
Diana Plata 1:59:04
If we would need that, we would need that information on some type of infinite
configuration workbook that we send out to the member banks. They return and
then from that, we open the account either on prelim or infinite or whatever the case
is, we open the account and then it spits out the correct signature card with the
correct signers, the correct agreement.
all that information already consumed by those documents that we can go out there
and send.
FortWorth-MuseumPlace-Boardroom 1:59:32
Yeah, well, and I would also say, you know, this process may be useful to the
embedded finance team.
Not specific to Hazel Bank, right, but you got one.
Diana Plata 1:59:42
100%, yeah.
FortWorth-MuseumPlace-Boardroom 1:59:44
So you may want to keep that a little bit separate, and then we're just kind of
consuming one of those flows inside the system for Hazel-specific onboarding versus
FinTech-specific onboarding.
You may end up wanting to use this for fintech prospects too. I don't know. I mean,
in the back of my mind, that's the idea is that what we're doing here could be
repurposed for embedded banking and onboarding fintech programs. So they can,
we can.
You know, onboard them quickly.
But then is interlacing world even in that flow? Yes, it's the exact same thing. It's the
same platform.
So the step of creating a separate tenant and based on some additional instructions
up front, you're deciding to create X number of account types and there is some sort
of a correlation around, hey, this account type is based on the products. So the
product.
I didn't quite connect what is the product orientation here. Yeah, so product types.
And I think Diana can explain this really well. I think so right now each tenant has a
template of available product types that can be available to that tenant.
Correct, prototype and account types are same idea or different idea? Well, initially
separate. Okay. And so you would say, hey, I have the ability to create a checking
account with interest. And so then now they can go create an account based off that
template that would create an actual.
Diana Plata 2:01:09
Different.
FortWorth-MuseumPlace-Boardroom 2:01:24
Checking account with interest.
So product type drives the account configuration. Yes.
Diana Plata 2:01:33
And product type also drives the setup at the bank level of operating accounts, right?
Because those transactions in that product, in that account, are going to have to
trickle up to sort of that operating account, reserve account, right?
FortWorth-MuseumPlace-Boardroom 2:01:51
Yeah.
So I do think we probably one of our next internal meetings is to talk through prelim
versus DocuSign and just firm up, you know, the final list of.
The final package here, where we need signatures.
Diana Plata 2:02:14
Yeah, and in addition to that, Aaron, once we actually see the list of products, what
type of documents we would need from that member bank for that specific product,
right? It may be the same across the board for all, but we can go out there and
define these are the products that are going to be available. And if a member bank is
onboarding to this product, these are the documentations we would need from
them.
FortWorth-MuseumPlace-Boardroom 2:02:25
No.
But I don't even know what the different products would be for basic hazel banks.
Marie Alonzo 2:02:38
Yeah.
Diana Plata 2:02:43
We have a list of products that are currently offered, right? So we can start with that,
the list of products that, you know, your simple FI business account, interest account,
so on and so forth.
FortWorth-MuseumPlace-Boardroom 2:03:00
And Aaron, just a point of clarification, it's not a question of prelim versus DocuSign,
because prelim uses DocuSign to do the e-signature process. It's a matter of building
this all out within this application that we're talking about and just adding the
DocuSign.
workflow to that or using what prelim's already created with their workflows and
then DocuSign signing at the end. So it still results in a DocuSign document at the
end. And so there's just, you know, just the, you know, and I think some of the points
that are being made that, you know, prelim already has all this built out, so it would
take us a while to recreate.
Marie Alonzo 2:03:26
Yeah.
And.
FortWorth-MuseumPlace-Boardroom 2:03:40
that in this application. But I do have that question of, you know, long term, should
we look at eliminating that additional third party coming into this mix?
Marie Alonzo 2:03:53
Yeah.
Diana Plata 2:03:54
No.
FortWorth-MuseumPlace-Boardroom 2:03:54
Yeah, and I would say for MVP, yeah, if it's not a heavy lift, use prelim, make the small
adjustments and configurations. Because effectively in prelim, what you do is you just
take an existing flow, you can copy it, and you can modify all the screens and what
things connect to it. You can even
configure which APIs it talks to. We can technically do all that ourselves. Normally we
rely on prelim to do some of those things, but so I would say we kind of treat those
as slightly separate. We let prelim, we, you know, we use prelim to configure it all, we
just kind of expose it up, you know, in the, you know.
In the portal.
Diana Plata 2:04:32
Shawn question. So, let's say we go through that option right with that option where
we use, we establish A workflow, prelim gathers all the information, so on and so
forth, it creates it right. Is the thought that after all that information is gathered and
all the proper documentation delivered to all parties?
for that information to come via API and to...
FortWorth-MuseumPlace-Boardroom 2:04:56
Infinance.
Diana Plata 2:04:57
Infinite to open, like to actually open the accounts, or is that still a manual process on
our end?
FortWorth-MuseumPlace-Boardroom 2:05:01
Yes.
No, no, we would we we have prelim or us, we either one can do it, set up the APIs to
push that data into infinite.
So, effectively, the...
You are, after the approval is done, you are actually on 2 parallel tracks, right? It's not
sequential, right? On one side, you are very clear that, hey, now I have the approval, I
have enough information to kickstart the internet side of the world, but I'm also
doing additional process through prelim.
To secure the DocuSign, so in theory.
Unless the unless the documents are signed.
You cannot create dot counts. Is that a? That's right, and prelim would control that
flow. Yeah, it'd be 1 workflow. Yeah, one workflow. So under that state, at that point
of that stage gate, that sub-stage gate, it's just waiting on prelim to do its job, and
then once it's done in the workflow.
Accounts.
Yeah.
Prelim then is the workflow engine at that point, yeah, yeah, yeah, so, so the
experience and the workflow we talked about is after approvals.
We have to trigger prelim first, and then probably in time. So, no, so you would get
your approval. You'd say, "Congratulations, you know your application to join Hazel
is approved."
The next screen would be, let's get you, let's get some accounts set up. And so there
has to be that first step where we've got to now create the tenant.
to create the shell of this inside infinite. And then the step after that would then be,
all right, now here are the individual contracts for each account that you're creating.
And so we're saying that there's a minimum of two. So there's going to be two sets
of contracts for those
All right, those things, and then so, as soon, so they're gonna collect all this
information in prelim.
Then it's gonna produce a document that they'll sign. Yeah, they they sign it, and
now we're gonna kick off, create those two accounts that they just signed the
paperwork for. Yeah, so basically two is contingent upon success of one, right? One is
one is the shell, one is the one is the shell.
which is a tenant creation. It seems like an engineering activity which is manually, I
mean, it's done fast. It's done fast, but it doesn't have an API. Like Amazon API is
where you say, for Kubernetes, we don't have that. But somebody manually will do it
and the shell is created. The moment the shell is created, step 2 is not really account
opening package. Step 2 is.
Choose the account, choose the product types, right? And, in this case, the default
will be you're gonna need an operational account and a USDA reserve account. Yeah,
maybe 2 required ones.
Yeah, theoretically, to Diana's point, there are other account types that they could
also agree to to set up, and then you, once that part is done, you again go back to...
Again, you go back, will have to go back to Enterprise and say, hey.
go do the tail piece of the actually create these accounts. Actually create the
accounts in the shell that you just created. Right, and there might be some functional
role in interface which will actually now use some interface studio or something. They
will actually create the accounts since the tenant is created.
Right.
Well, there is going to be a configuration recipe that Infinite would have to give us.
So like how do they do it, what information they need? So there's going to be a lot of
details we'd have to collect there. But right now, I'll kind of just put it as, you know,
integration point exists here. And so, Shawn, so I think an important question
Diana Plata 2:08:48
But.
FortWorth-MuseumPlace-Boardroom 2:09:07
Would be, are we going to...
For the actual account creation.
Are we asking prelim to do like prelim calls the APIs to do that on interlace or are we
going to have prelim send that information back to the this application and then this
application instead making the call to create the accounts? I know I mean.
Yeah, I mean, I guess you could do either. It might make sense to send it back to the
Hazel onboarding app, just so you can do the status update at the same time and
kind of. I don't know if there's data.
there that we want to capture in the data lake? There probably is. That would, I don't
know. Well, we're going to want the documents. We're going to want some of the
data out of the onboarding and signers and all those kind of things. So we'll want
some of that data. So yeah, it's probably best to send it back to the Hazel app
instead of, you know, and Hazel will be effectively the.
The middleware or the proxy between all the different systems, yeah, it is, you know,
where we can, and and and prelim supports that, you can send it to anywhere, they
don't care, it's just, here's the data, here's the API call, and really, I'm just trying to
brainstorm here, because we don't have the integration today between prelim and...
And interlace.
And so that is going to have to be built some, you know, either by them or I think it
would be better to be built in Hazel. That way we have optionality in the future if we
need to do other things. Yeah, so there's going to be other interactions we're going
to want to automate within.
Right, being a headless core, so ongoing monitoring, or maybe we have to close an
account or off board an account or whatever, we're going to want to automate all
that, so it'd be better to have some people to talk to. Sure, and then here's, I'm going
to now let the other side of the coin internally as Vantage Bank.
I mean, we're using prelab.
We're going to need to build an integration into Interlace anyway, if we have our
own customers, our end users, who want a tokenized deposit account, and we're
going to need to have a workflow to create these accounts.
Diana Plata 2:11:24
I have a question. I have a question real quickly, because this can serve an initial
setup. But once the tenant, the member bank has access to their tenant, the widget
out there allows for them to open as many accounts as they want, of many operating
accounts, and at some point, end user accounts, without us even finding out.
FortWorth-MuseumPlace-Boardroom 2:11:24
So, yeah.
Yes.
Diana Plata 2:11:44
So, there's not going to be any communication back to prelim on will now produce
documents and things like that for those additional operating accounts at that.
They decide to open.
FortWorth-MuseumPlace-Boardroom 2:11:59
Well, yeah, I mean, yeah, I think those are some of the things we're going to have to
flesh out. I like the idea of let's just get them to bare minimums and then, and then,
you know, maybe they add on future accounts and then, you know, change or, you
know, modify accounts in the future. Those are going to have to be separate
workflows, I think, you know, so. Yeah, but I hear what you're asking, Diana, because
she's asking.
Marie Alonzo 2:12:00
Yes.
Diana Plata 2:12:19
Yeah.
FortWorth-MuseumPlace-Boardroom 2:12:20
more about the compliance side of this with today, they will be able to open
additional accounts themselves without triggering any required documentation that
we might have to provide. Because it typically interlace is not. Oh, you're talking
about when they're in the console directly at the end? Yes.
Diana Plata 2:12:37
Yeah.
Mhm.
FortWorth-MuseumPlace-Boardroom 2:12:43
Oh, well, yeah, I don't think we care if they open up tons of accounts that are on their
balance sheet, right? I know we don't care, but compliance as far as any kind of
actual exposure doc. So we're going to need to make sure that whatever original
documents we collect or
Diana Plata 2:12:44
Hello.
Documents.
FortWorth-MuseumPlace-Boardroom 2:13:02
or have them sign account for additional accounts that they can self-provision. And
are you talking about self-provisioning the like operating accounts, Diana? Yeah.
Diana Plata 2:13:08
Yeah.
Yeah.
And then at some point, even end user accounts, when that widget is created, the
member bank's going to have that control to go out there and open as many
operating accounts as they want, right? And then at the customer level and business
level, end user accounts. So at that.
FortWorth-MuseumPlace-Boardroom 2:13:25
That she.
Yeah, we shouldn't care about them opening up accounts for their own customers or
on their balance sheet. We're just the ledgering platform at that point. So there's no
due diligence, no requirements. That's not our customer. Right.
Diana Plata 2:13:39
So...
So if that's not our customer, what's the purpose of us providing them or having
them go through the prelim process when we're onboarding them?
FortWorth-MuseumPlace-Boardroom 2:13:50
They're opening an account with Vantage. Yeah, that's that's a bank account for the
bank versus an end user. So, yeah, I mean, let's not get those.
Diana Plata 2:13:58
Well, let's go back to the operating operating accounts and let's forget end users,
but if they go about opening additional operating accounts, right?
Wouldn't that basically mimic the same thing that we're doing at account
onboarding, where we're asking for them to fill out all this documentation for those
operating accounts that they're opening?
FortWorth-MuseumPlace-Boardroom 2:14:18
Agreed, Diana. And so this is where I think we just need to make sure that the
original agreements that they sign include whatever provisions that say you're
allowed to open additional operating accounts, but they're going to have all the
same beneficial ownership. They're going to be styled exactly like
your original operating account.
Yeah, well, and again, we probably won't solve it today. We probably should move on
from here, but I think in the end...
We need to think about what operating accounts mean, and if they're on Vantage's
balance sheet and they're opening them on behalf of Vantage, what do we want
from a compliance and documentation perspective for every account? And how do
we simplify that process with the information we already know since they've already
gone to the bigger onboarding piece? But I think we'll maybe have to figure that out.
But I think that's a good call out on if they can provision them themselves and those
end up on Vantage balance sheet, does anything change on our side? Or do we, like
Jay said, it's always the same owners. They can't really change that minus some
change process that they kick over to us.
So I think it's a good call out though.
Okay, well yeah, we'll definitely keep that conversation going.
Later. Later. Well, yeah, it's just a lot of detail. Because again, we want to get to MVP.
And I think on the MVP side, like, we just needed to find what is that initial thing to
get the both bare bones, minimum to get them going and online and actually using
the platform. Obviously, they need the cash reserve and operating account.
Diana Plata 2:15:39
Yes.
FortWorth-MuseumPlace-Boardroom 2:15:56
Um, at a minimum, so...
App.
So #2 are the five, 6 documents that we will use prelim for. And then #3 is the Hazel
membership agreement that links to an MSA and a correspondent agreement as well
that we'll have hosted online at some point.
Point, and then we've added a security procedures document recently, which is
something that we'll need to.
I don't know how much input that requires from the banker.
Off.
If they're with participate, we have a little AI.
Acknowledgement from at this level, too, so...
These legal agreements are not negotiable.
Not for basic, they're not negotiable. Yeah, not for basic.
An account with us is operating.
Hi.
Yeah, and we, we, our goal on that agreement is not to create a bunch of one-off
legal exceptions.
If we're trying to make the non-negotiable, there's probably going to be sections
where we say that we understand some things are gone.
want to negotiate capture liability or something like that.
But again, we can solve that later today, just consider the docs, and then those
probably could be settled separately with a on an agenda, yeah.
And Shawn, I think, I mean, Tate sent over the MSA and corresponding agreement.
So are we ready to put that online?
I mean, I don't know if it's 100% finalized. The goal was, yeah, but I mean, we should
be close.
I can tell you to get that out. Yeah, well, I want to, yeah, and I...
I'll take a look at it because Tate has been going back and forth on certain things I
want to make sure.
Rosalba, what the?
MSA includes, as compared to the embedded bank, making sure that they're aligned,
yeah, so I'll do that at reconciliation, Juliana, don't let me forget.
Marie Alonzo 2:18:12
So just.
FortWorth-MuseumPlace-Boardroom 2:18:12
Yeah, Eliana, do you need your AI? Yeah, Ileana is my AI agent. AI and human, but
she's real intelligence, not artificial.
Marie Alonzo 2:18:22
So just FYI, today, it still requires a person to open up account in prelim. And in that
workflow process, we may have a potential duplication of process. So a new
workflow would have to be built out because today's workflow starts with asking for
documents.
So we would still need to build out a workflow for it just to be skinny down to open
the account.
FortWorth-MuseumPlace-Boardroom 2:18:45
Yes.
Absolutely, there will be a customized workflow just for this Angel bank.
Okay.
Provisioning. So after we collected information, we send it to Infinite to set up. That's
the current two-week process. Again, this is where we'll have API access in the future.
And we have the roles that we need from them. And right now, like, we're asking for
some of the roles in CoverBase. So that might be something we pull out to later. We
could separate that.
Um...
I actually don't fully know what we do with KYB.
At this step, so I guess I mean with setting up through sardine.
Diana Plata 2:19:50
That is only done at the end user level.
Aaron, there's no KYBKYC done when we're opening member banks or operating
accounts.
FortWorth-MuseumPlace-Boardroom 2:20:02
Yeah. Okay, so we'll remove that step. Right, but I mean, there's still...
We have to provision them access to sardine.
Are they looking, are they managing their?
Their fraud stuff directly inserting.
Okay.
Each member bank, yeah, each member bank. Well, the basic, then you're saying
they'll have access then to Sardine for the.
So I think they just have, you know, I was thinking they would just see that in infinite.
I don't, is that where the sardine cases are worked? I don't, yeah, you're right. It's
sardine, but they don't have a contract with sardine, right?
Diana Plata 2:20:42
Third.
FortWorth-MuseumPlace-Boardroom 2:20:46
Well, they're not, yeah, the bank is not working cases we are.
Third week, Paul.
Diana Plata 2:20:52
Yeah.
But...
FortWorth-MuseumPlace-Boardroom 2:20:55
We have to figure that out; we can't handle that kind of volume.
respect.
We talked about compliance as a service.
To figure out the model, we handle it and step up.
Diana Plata 2:21:11
Yeah.
FortWorth-MuseumPlace-Boardroom 2:21:11
Okay.
And how do they handle it? How do they get access?
Diana Plata 2:21:16
I agree with your point, Joe. So right now, obviously, we're doing it for custodian and
the pseudo member banks, but once it's a member bank onboarded, we would give
them access to their tenant, their accounts, and at some point, their sardine for them
to be able to go ahead and manage that, wouldn't we?
FortWorth-MuseumPlace-Boardroom 2:21:22
Like.
Yes, but how can't we and how? That's...
When it be, when it be inside, just like a fintech, they go in and have their own tenant
in Sardi, and they would, no, I, yeah, all of that, that's true, but...
I think there may be another contract.
Involved that with sardine.
Pintax.
So with sardine, the way that we're doing it right now is we're using sardine for
ourselves.
So it's our backstop, our choice. Theoretically, we don't have to have Sardine installed
for all of our fintechs. We're absorbing the cost of that today. And so, but we still
require, so all of our other programs, all of our payment facilitators.
Diana Plata 2:22:15
Yep.
FortWorth-MuseumPlace-Boardroom 2:22:30
They have their own KYC, KYB, and fraud tooling that they're using.
We're the backstop, you know, that that sardine is the backstop, so yeah, if that could
be the same type of model that we're gonna have here, if that's the case, then it's
what Joel's saying, we'll need to staff up to be able to to monitor and view while
we're this stuff, like, you're almost gonna be like little T.Y.
Right, yeah, that that's an option, but a lot of banks won't want that; they're not
going to go to.
Go, yeah, I always kind of thought there was maybe 3 models, maybe we just haven't
talked about it, but it was like, we're we're we are the compliance service, we're doing
the screening, monitoring, and dispositions, etcetera, and we can just give them a
report and then you know, you can on us, then there's the, yeah, yeah, I want to do
my own and I'll use sardine natively in the system.
to this position and manage my own with my own team. And then you have the, I'm
integrating my own provider. I don't want that.
Yeah, and so...
In that, in the basic mode, it's always us monitoring, it's our accounts, yeah, alright,
but so, so, but back to the the...
Diana Plata 2:23:36
But...
FortWorth-MuseumPlace-Boardroom 2:23:40
that scenario. So if you do give them the option, they opt to use their own stuff. We
stop.
viewing those transactions.
Yeah, yeah, it's not our customer, it's not our bank, we're not responsible for them,
so, but it is our network.
Yeah, but that that we're not responsible for all network activity. We're responsible
for Vantage activity. I get that, but what responsibilities does the network have to
monitor? And now as well as screening.
So, we're required because it's, well, not technically the actual tokenized deposit, the
stable coin itself are required to monitor all that.
Custody is responsible for that, so it has deposits.
Technically, each bank is responsible for their own customer's own transactions, so
we're not responsible for that. However, right now, it is monitoring all, doesn't matter
what token it is. OK, so that that's just for this group, but yeah, but it sounds like we
need, I would say, just put a pin in that, we need to figure that out. I mean, it sounds
like we have to...
So, so what is the the the conclusion that?
At the do we integrate with sardine, and is this sardine integration? So, so with what
we're talking about, no, no, yeah, because the basic model is they're outsourcing that
to us, so we don't need to give them direct access to the sardine to to view the
information, we'll communicate, you know, and so...
We'll have a way of doing E.D.D. all that, but we are outsourcing it to us, which
means we have to integrate, right?
Right, but there is an infinite already provisions starting with with these, so they've
already done it. Yes, I mean, okay, I...
Okay, so, but Aaron, what I would say as far as other integrated services, so what
we're in the process of finishing the build of is our SharePoint and ticket integration.
And so, you know, so that's going to be
Done through SSO, so that'll be.
We'll need to basically do the, what is that called, OAuth configuration so that they
can log in and then we've got to provision a SharePoint. Well, we may not need the
SharePoint.
for Hazel Banks if everything's living in Databricks. Because why we're provisioning
SharePoint and a ticket platform, those are both kind of Microsoft stuff, so that they
can open up tickets with us. Yeah, as in who interlace or the end users or the
member banks can open up.
Problem tickets with us saying, "Hey, you know, why did this transaction post, or, or if
if we're doing those, so that's a service monitor capability, yeah, so, so that that'll use
OAuth to to come in, they can create tickets, and then there's a...
a web portal that we're doing for our embedded banking customers that we're able
to have a share file, a file sharing capability, so that when the BSA or compliance
teams have to escalate a case that they're investigating in sardine, for example, hey, I
need additional documentation, they've got to be able to
We want a closed system to be able to chat and send files back in. So are they talking
to Hazel or are they talking to Vantage? So yeah, I would always treat this as Hazel is
a separate company. They are now Vantage whatever systems he has.
Is now we're talking to them almost like...
So, Infinite's one of the providers that we're talking to. The ticket system might be
something we're talking about. I want to build a pay list completely independent.
We're not relying on his ticket system or whatnot.
Yeah, so we can, if I need to send in a support request, then we facilitate the
communication back to Infinite and the team and whatever technology he's using. So
we decouple ourselves from that.
We need a, like, a work stream fraud, and...
Just, just want to figure out the starting, because I'm...
CIP, KYC, KYB, that's easy if we can give the banks that data when they need it, the
regulator request, whatever.
Blockchain monitoring those that.
those screenings should be, the hits on the screening should be few and far between.
So custodia works on our behalf. Fraud monitoring, that's going to generate a lot of
alerts.
That's going to put pressure on staffing, and then the communication with the banks,
that's going to take a lot of resources, so CAS blockchain screening and customer
screening, but from a transaction monitoring perspective, that's...
Thank you for that. So a lot of, just a little bit of idea of how I've been thinking about
some of that. It is, in all cases, I want to log all that data into Databricks, whatever
that is. And then from there, we will provide these data sets in real time, or batch,
doesn't matter.
Two banks correctly. Dashboards or data streams. They can consume them however
they need to. We will have pre-configured dashboards and data sets and exports and
things like that. But for the bigger banks, they're going to want that as a live feed
directly into their systems. And so Databricks supports all of those capabilities, both.
Batch streaming delivery, but I want to be able to capture as much of that
information as possible, so that Hazel can deliver it, not infinite, not, yeah, whatever, I
get it, I get it, but from an MVP perspective, I'm still struggling with the question that
does...
Hazel the network.
Is live is is on the network liable for?
KYB and with the CIP activities on the member banks customer. Hazel's a technology
platform. I'm not a bank, so we're not liable for that. The bank will be responsible for
the KYCKYB. Then why are we integrating this already?
Sardine, because we're providing this as a service, we could we they can outsource it
to us for the monitoring of the transactions. Member banks can, member banks can
contact with us, so there's a separate charge of charge for doing that, yeah, yeah,
there's an offering, well, I mean, well, with the basic, it's included, so it's a...
It'll be a different charge if they want to manage it internally. Yeah, so they think right
now, I would say we don't know. We always haven't thought through that one well
enough. So I'm going to say we put an ash trick on, like, do you actually integrate
with Rd. or is it part of a backing process that Infinite does? We don't know that yet,
because it could just be a state.
Yeah, you're selecting this that you want CAS. OK, then great. Then it's something
else that has to have an advantage. They have to automate it, right? I don't know the
answer to that.
Up.
But for MVP, I don't think we worry about that because in the basic model, there is
literally no, it is just an account advantage. They're just using us as a correspondent.
So we're setting up an account advantage. We're always doing, Vantage is always
doing the screening. It's only when they get into the more advanced scenarios that
we start to see this.
But it does bring up a good point. You need to flush all that out. Yeah, you know,
pursue because it impacts contracts. Yep.
Well, and and again, looking at how we would want to deliver.
a holistic solution.
We would need to talk about ticketing and so that the tickets are there within the
application itself. They don't have to click out to a third party application. No, yeah,
we don't want them to click out. I mean, and we would want all that service ticket
data and customer, you know, issues, blah blah, sort as data in Databricks. That's
going to be key to our CRM.
How we track all that, but I think that, yeah.
Vantage could choose to.
Use what we have, and that's, you know, and that helps you, or, like, by integrating
the ticket and y'all doing your own thing, I think, 'cause again, I think we have to
think about it as two separate entities that are decoupled, no, I know, and that's the
rub is trying to think of it as, okay, and Vantage is a customer of, because you're
gonna have your own.
You're going to have your own internal tickets for things you're doing versus the
Hazel banks and their specific stuff. So you're going to have embedded finance
tickets. You're going to have Hazel tickets. It's going to be very different. So I almost
have to just push data to you guys to say, you work with the tools you need.
I don't know, again, we maybe have to think about that. Sounds like we have another
integration point, so, so that Hazel Bank console.
Is is that the same?
Uhh...
Should be the infinite console. There's one on the left hand side, but that is a bank
console, is that the complement, internal complement to the external border thing
that we are talking about? I think in this particular PowerPoint presentation, no, that's
different. What this would be is the actual.
portal where the banker can view, it's the ledger, the actual ledger. So that's the
console. So there are two pills over the Laser Bank console and that's what I was
referring to.
Yeah, I know you're referencing. I don't know why.
All that in there, and he's giving up on your PowerPoint, so I, so I, I don't, there are
two, it's a loose, there are two, I don't, there are, yeah, that's right, oh yeah, there are
two, it's all, yeah, it's one, but yeah, I mean, so there, there's the interlaced console
where they they will be able to.
That what I get to do stuff, yeah, but then yeah, there's gonna have to be a separate
app where all the data that Databricks is collecting is gonna, that's the internal one,
that's the internal one, yeah, I, at some point, we'll have to come up with some
business names for both these internal and external apps, yeah, and then the fiber.
Fiverr, what's the bad guy? No, the big guy, big, ohh, big work.
Don't do we want that one. Well, and so yeah, I mean, you can refresh the slide if you
need to, but yeah, obviously they're going to, the bank is going to be automatically
provisioned into the Hazel app, so you can see the status of their, you know,
onboarding and then probably tickets and other things would be the external side,
internal side.
Probably the same app, but you know, the internal side is what can the bank see
that's, you know, more more expansive than what the bank can see from a
permissioning perspective, so there will be traditional IM and all those kind of things
and group provisioning and security and so forth.
Then you're saying the access to the tickets will be a separate? Well, to Sean's point,
because that's what we're going to do with our embedded banking, I mean,
embedded finance programs, because we don't have a centralized database like
Databricks to manage that. So we're using the OAuth.
to go pull to be able to use these two applications. So to me, it sounds like it makes
infinitely, no pun, more sense to build a lightweight ticketing system within
Databricks and service it within the application.
So, that everything's there, then what is the difference? That's part of the what will be
the customer relationship management platform, so I can look at the customer and
say, "Here are all their tickets, here's all the interactions, whatever. So, the only
functional part I am slightly confused is the computer here, hey, there are...
network tickets, check different Vantage Bank tickets, so that's the only part I'm not
able to connect to. Just assume that Hazel Banks are going to be communicating
with Hazel for support and requests and whatever, and then we may have to push
those down from, let's say, the Hazel team to the Vantage team. Oh, so...
Yeah, yeah, so suddenly your existing Hazel bank corresponding bank program has
other banks. So what he's saying is, maybe we build this Databricks ticketing
platform. Yeah. Today, existing work groups are using a different ticketing platform.
So we may have to.
Send those tickets from Databricks into the third party. I got it, I got it, so that these
guys continue working the way they've always worked. Yeah, versus introducing
them a new tool, so then who will use the Databricks ticketing system? Yeah, I think
that would make a cleaner and...
more future-ready.
The Hazel operating team or the team that's running Hazel, it could be Diana, but
just assume it's just like any other business, it's a group that's operating and running
in. They would be managing those tickets inside the application. The bank should
have visibility into the tickets they've submitted and so forth. But again,
We are focused on onboarding right now. So that would be, again, kind of future
state. What else was this app going to support? Yes, it's, you can see your tickets.
You now have ongoing, you know, support and convenience and those types of
questions. So.
It is noon. I wanted to let everybody kind of take some time to get lunch. It looks like
it's probably here. We can work through lunch if y'all want, or take maybe 15, 20
minutes and I'll eat our sandwiches and then maybe finish out the rest while, you
know, while we're still eating, but at least kind of take. Well, but I mean, we have your
stuff for the folks that are on the board. Yeah, that's right. Yeah. I wanted to say
something. You've got to go somewhere. So
I would say, you know, let's stop here, break for an hour, you know, and then
obviously we'll meet back here at 1:00. And, you know, we shouldn't have much more
to get through. I do think we'll probably, we won't need much on the next few slides,
it seems like.
Yeah, and so at 1:00, then we'll, you know, what might be good when we come back
from lunch, finish a little bit of this technical side, so we have good understanding for
for Theorem Labs, and then maybe Theorem Lab, y'all can kind of walk us through
like what you foresee as next steps and how your teams might operate and, you
know, and where we kind of go from.
Here, maybe that'd be good. Yeah, yeah, sounds good. Great. So, everybody OK with
that? An hour, and I know it's we're a little it's not perfect, but sound good.
Okay, all right, we'll see everybody here in an hour.
Diana Plata 2:39:11
Yes, sir. Thank you.
Aaron McWilliams stopped transcription
