---
title: "Daily HOP Standup"
document_type: "transcript"
source: "meeting"
client: "Hazel"
date: "2026-07-23"
status: "parsed"
version: "1.0"
tags:
  - "daily-standup"
  - "hop"
  - "project-status"
confidentiality: "client-confidential"
source_file: "../raw/2026-07-23-daily-hop-standup.docx"
content_sha256: "c87d6d87fce4fcf6b622290cd1f2377bbf61572a4488148559cbc9a4396173a8"
---

# Daily HOP Standup

## Transcript

Daily HOP Standup-20260723_165945UTC-Meeting Recording
July 23, 2026, 4:59PM
1h 31m 24s

Smital Lunawat   0:05
Yeah.

Shardul Patki   0:11
Hello!

chris colson   0:12
Hello.

Prashant Sarode   0:14
Hello, Chris, how are you?

chris colson   0:15
Hello, good. How are you guys today?

Prashant Sarode   0:18
Playing a bridge, nice and cold.

Aaron McWilliams   0:26
Hey guys, hey guys.
Ah.

Pallavi Bichpuriya   0:30
Hmm?

Prashant Sarode   0:35
Which are you based out of?

chris colson   0:39
Atlanta, Georgia, for the time being.

Prashant Sarode   0:41
Ahh.

chris colson   0:42
The.

Prashant Sarode   0:43
nearby.

chris colson   0:45
Yes.

Prashant Sarode   0:46
Cat.

Aaron McWilliams   0:53
Did any of you all invite fireflies to this meeting?

Robert Ramirez   0:59
That's fine. It's coming up. I don't know. I saw a meeting from somebody and now it's coming up on everything. I denied it.

Aaron McWilliams   1:02
Okay.
Yeah.
Well, I think I saw that on town hall yesterday, and the pop-up just keeps coming up right now. So somebody else is using Fireflies on another Hazel call, and we have not been able to kill it yet. We've been working on it for a couple months. So I wish you the best of luck.

Robert Ramirez   1:26
I know I've been trying to kill a friend, where I can honestly I can't find anything.

Aaron McWilliams   1:30
Oh, I'm sorry, man. All right.
Well, let's jump in.

Shantanu   1:35
Oops.

Aaron McWilliams   1:38
Chris, thanks for joining. That was really last minute. I didn't think you'd make it today. So Chris is doing double duty, so he's going to make it when he can. But this next month is mainly him kind of onboarding, and then he'll eventually take over a lot of what I've been doing here. But
Well, we've got a few weeks for that transition. And then we've got Beto today with us from our analytics team, and I think Maruthi will probably join pretty soon too. So Prashant or Shantanu, I don't know if you guys want to start kind of on the data needs or data brick questions since we have these guys here.
There was something else you wanted to begin with.

Shantanu   2:21
Yeah, I think if we have a databricks team, maybe first, can we have a little bit of introduction? Maybe we can introduce ourselves too. Who is from the databricks? I'm sorry, I did not get it. Is it Beto?

Aaron McWilliams   2:36
It's Beto Espinoza, yeah.

Shantanu   2:39
What is that?

Beto Espinoza   2:39
Yeah.
I'm doing fine, thank you.

Shantanu   2:40
All right.

Robert Ramirez   2:41
But he's for vantage; he's invented it, but...

Beto Espinoza   2:43
Yes, yeah, so I'm not, I'm on the Databricks team on the vantage side. Thank you, Robert. Yeah, I'm an analytics director on the shared services team, but yeah, Maruthi Dantu, like I said, he should be joining in just a bit, but he's a data architect on the Databricks side. Maruthi has worked primarily in a lot of the integrations, like...

Aaron McWilliams   2:44
Yes.

Beto Espinoza   3:04
Cross application, cross product, so he's been a lot of the primary, you know, points of contact, especially when we're, you know, integrating on the ETL processes. We, my team, and a lot of what we do, we work in alongside with the data architect team, so we do a lot of the validation, you know, the transformation, the visualization of the data once it's established.

Shantanu   3:26
Thank you.

Beto Espinoza   3:28
But yeah, we also kind of help assess some of the customer needs to just make sure that we have everything staged. But yeah, a pleasure meeting you all. On the data bricks end, like I said, we do have a tenant of data bricks with multiple workspaces.
Presence, but we do have the availability to do share and integration via some other means, but yeah, pleasure to meet Shawn and kind of get some scope of what you guys are looking into doing.

Shantanu   4:02
Nice. So, so the hazel is new for you. Is that the right statement?

Beto Espinoza   4:07
I mean, we're familiar with Hazel. I mean, we know the concept, we know the pieces, we've been we've been part of those conversations. Shawn, so we report to Shawn, so Sean's been able to kind of give us all the context of what we have. So, from a project standpoint, we understand it's just, you know, where we can kind of fit in on the next steps to help kind of...

Shantanu   4:16
Okay, okay, okay.

Beto Espinoza   4:28
you know, integrate or pass the torch or anything like that. That's kind of what we're trying to do.

Shantanu   4:30
Yeah, OK. So, you know, if I hear that you are, you know, you were part of the Sean's team from last, you know, for us, we are into 10 days into the discussion. You probably have more history of what has been concluded.
on a database. Like, hey, this is where it, you know, this is where the database should be. This is what database should do. I need this integration, should have integration and all the stuff. So in reality, instead of we telling this is what we want, we probably want to hear from you if you have some notes documented stuff.
Okay, this is a...
virtual design you are anticipating for Hazel, we want to see that.

Beto Espinoza   5:19
Yeah, and that's pretty much fresh. I know Maruthi just joined too, Aaron, and I know, like I said, we've been kind of working through, but Maruthi, just to kind of reiterate the question, I mean, we did a couple of introductions. I don't know if you want to just do a quick introduction. I did a broad one across us and the team. Oh, okay, then you guys are fine.

Shantanu   5:35
I think we know Maruthi for sure, yes.

Maruthi Dantu   5:36
Yeah, I think the...

Beto Espinoza   5:39
Yeah, so I think that, yeah, the question was just like really disappointed to us, like from what we know on the Hazel architecture, like what our needs might be from the Databricks and from either like the data that we'll need staged or some of the other tables and things like that that we'll need to kind of have in place.

Maruthi Dantu   5:39
Did him last night.

Beto Espinoza   5:58
like to help execute, at least to start off with. I think that was the general question from our perspective since we've been a little bit more aware of implementation with Hazel.

Shantanu   6:07
Even from the databricks perspective, we were talking about the complete new tenant, right, or complete new domain for Hazel.
So, so.

Maruthi Dantu   6:19
Yeah, I believe so. I think it's going to be not in the same tenant. I'm not quite sure. Robert and David can.

Robert Ramirez   6:27
Yeah, yeah, we're we're setting up a different tenant, Maruthi, and then it there, we're gonna set up a data breaks on the dev, a dev data breaks right, David, on that tenant by itself.

Maruthi Dantu   6:32
Hey.

Shantanu   6:39
Yeah.

Maruthi Dantu   6:42
Yeah, and the Enterprise groups and everything will be completely independent of Vantage.

David Gonzalez   6:48
Yes, that's correct.

Shantanu   6:50
So if the separate new tenant for Hazel from a database side, how then the data which is currently a Vantage data sitting in a Vantage space, if you want to expose that data or API through Hazel, is that it?
Easy plug and play or this needs.

Maruthi Dantu   7:11
Yeah, yeah, so Databricks has something called Delta Share through Private Link, and you all can, it's a publicly open document documents that are available, so that can be set up through Private Share. Private private sharing is possible through Delta Share in Databricks.

Beto Espinoza   7:13
Yeah.

Maruthi Dantu   7:33
So that is something that we can be leveraged in terms of data share is concerned. Of course, you know, we have to make sure that a proper data contract is set and what is being shared. And but yeah, it's possible through delta share private.
Not sure.

Beto Espinoza   7:53
Yeah, and I think from what I remember, the conversation with it with Shawn is like the restriction piece on exactly what we're sharing, because we're trying to keep the entities independent of the, and it's, I think the Databricks did some rebranding on this one. It's called, I think, Open Share now, because they're trying to make it more broad, but they...
It really is meant to be only the needed data that needs to be sourced from our tenant into that one. So that's where we'll have to identify what exactly the primary needs are going to be so that way we can have that exposed. But for the most part, we should be able to.

Maruthi Dantu   8:19
Right.

Beto Espinoza   8:32
at least diagnosed that, you know, there is independence between the both, with the exception of, like I said, this connection.

Shantanu   8:40
Okay, I think this is nice. So at least we understand the, you know, the basic, you know, where team is, home to contacts. From, you know, needs perspective, what we need when, I think we are not there yet. We know, we just into the discussion, we just started talking. We are driving it.
From top to bottom, you know, initial discussions are on, so we know the functional workflow and all, everybody understands, but for, you know, data level discussion, API, and then we are gonna talk about, we said, let's go with the front layer to be designed 1st and move forward.
So we are kind of thinking that maybe in three, four days from today, we will have a HTML wireframe data.
for the external users. At very high level, we are thinking we will have mapping available to just give you some, maybe share some.
Might not be the complete document, but it'll give you the kind of a context what we were thinking of.
Yeah, so this is what we started. You know, all the discussions started from Monday. You know, initially we were at this stage like, hey, you know what, let's start focusing on the UI or workflow will be something like this. At least some of the pages, some of the UI will be exposed as a public, then we'll have a...
You know, user, and then we'll have a dashboard and workflow as well. Maybe yesterday's discussion inspired or, you know, took us to this level wherein we are saying, oh, you know what, these will be 7, eight kind of the steps in a workflow. Some of the workflows will have.
e-mail, you know, back end workflow integrated. Some will have a security, some will have a DocuSign integration. These will be, you know, the data forms from our space, Rafa, and all. Some of these questions will go back.
to those, you know, what is that window? Yeah, so that is what we are looking for and what we are anticipating by maybe by Monday. We will have these UI reviewed by the entire team. And then we should be in a position to come up with.
the backend component.
something like we need XYZ APIs, some configurations from the security perspective e-mail, and that list should be ready by maybe Monday or Tuesday.
That's what we are thinking up till now. Is this sounds okay with everyone?

Beto Espinoza   11:43
Yes, I, I have one question, Aaron. You might, you might have got this one too. The public page right there that's listed on there, that's the website page for the inquiry form, right? On on when on the Hazel site, whenever they're trying to do like a connect with us.

Aaron McWilliams   11:57
Yeah, hazelnetwork.com.

Beto Espinoza   12:00
Okay, that the public page is still in the vantage tenant. I think the way that is current, I think that the domain itself is still in the vantage tenant. I just don't know if that also has to be sponsored off at some point.

Aaron McWilliams   12:11
I mean, at some point, but that doesn't seem like a priority. I think the main thing was the data bricks foundation.

Beto Espinoza   12:15
Yeah, it's another.

Shantanu   12:15
So...

Beto Espinoza   12:18
Okay, okay. And then the connection, I'm sorry, go ahead, go ahead.

Shantanu   12:20
Salt, salt.
Well, I mean, we have every day we are iterating through the wires what we are building. We can go through that as well, just to get a sense, like, are we there yet? Is it 60% ready, 50%, 20 or 90? I think Smital or Pallavi, someone have that ready.
Yeah.
Is it?

Smital Lunawat   12:47
No, we have it, yeah.

Beto Espinoza   12:48
Sam.

Shantanu   12:51
Yeah, so maybe 10, next 10, 15 minutes we can go through that one more time today.

Aaron McWilliams   12:59
Yeah, I think, I mean, probably when a lot of the Databricks questions are going to come up is when we actually get that tenant created and get you all access and start kind of seeing what's needed to be built. So, so Beto and Maruthi, what I might do is just invite you guys to the, this is a daily meeting.

Shantanu   13:05
Mitch.
Yes.

Aaron McWilliams   13:18
I'll just put it on your calendar, but then you guys can kind of see what the next day is about and decide whether you need to come each time. That's kind of what David and Robert are doing too.

Beto Espinoza   13:30
Okay.

Maruthi Dantu   13:32
Sounds good.

Aaron McWilliams   13:32
I know you guys have a lot, so I'm not trying to add another daily meeting.

Beto Espinoza   13:35
No, that's fine.

Robert Ramirez   13:40
I know David and I will work on still the Hazel tenant today in the afternoon. We had an issue with trying to create the cloud PCs, but I think we got over it. There was a ticket open with it, but we were able to change the...

Pallavi Bichpuriya   13:40
Yeah.

Aaron McWilliams   13:55
Oh, good.

Robert Ramirez   13:59
To Enterprise, and we got those. I mean, we got at least to buy the five licenses, so we'll work on that this week.

Aaron McWilliams   14:08
Awesome. And then I think we got everybody from Theorem set up in Teams. I added you to the Hop channel where we can share files. So any files that you want us to see or vice versa, you can pull up in the Teams shared folder.
So let me know if you have any difficulties with that, but I think Smiddle's been set up already, so...

Smital Lunawat   14:35
Yeah.

Aaron McWilliams   14:37
And.

Shantanu   14:38
So who is going to share the wires on? We don't want to discuss that today.
Did I miss anything?

Aaron McWilliams   14:46
Now we can we can look at the wireframe he had up. Shawn is here now, so it'll be good for him to see kind of what we discussed yesterday and just offer any feedback.

Shantanu   14:49
Yeah.
Yeah, OK, so.
Yeah, probably, do you want to open that PPT so that Shawn gets the sense what we are trying to do just in a snapshot on a one day or so, you know.

Pallavi Bichpuriya   15:00
I.
Oh yeah.
Yeah, is my screen visible? I'm sharing. OK.

Shantanu   15:08
Yes.

Aaron McWilliams   15:09
Yeah.

Pallavi Bichpuriya   15:12
So.
We have revamped the page and now if we have if somebody wants to express their interest, we'll fetch their FDIC and then Rafa will run at the back when somebody submits their interest.
And accordingly, they will be contacted to contacted via Vantage, and once they're eligible.
They'll get an invite to continue joining the Haze network and we will be giving them an expiry date that till this time you can join our network and we can accept and continue. They will all these fields will be pre-filled by us except the password.
They'll have to set up the password and create their account.
Go to the next page and every member bank will have their personalized dashboard which will show their onboarding journey. So we are done with eligibility, we are done with registration and now we are here at the NDA part. So the NDA will be joined, will be signed by both the parties.
Here we can see their institution profile, their recent activities.
So let me go to the NDA signing. And since NDA signing will also take us to DocuSign, as in we want the DocuSign to be embedded in our Hazel network. So once we review and sign, we'll get a pop-up with everything.
Sign it, continue next, then sign finished.
So, once all the parties have signed the agreement, then only they'll be taken to due diligence. Now, due diligence, we are not yet sure we we have the fields, but which all fields are required, so we want those confirmation from.
you, but for now we have whatever we had, we just created it with different sections, institution details, primary contacts, the documents required, and submission.
And then they will get the summary of what all things have changed and the documents, whatever the summary of everything we've done till here. And they can, if they need a teammate who can help them in providing some other details, they can invite them as well.

Aaron McWilliams   17:49
Mm.

Pallavi Bichpuriya   17:52
And then once due diligence is signed, they'll go to the risk questions that were provided by Coverbase. So there are different different sections for that as well. We added those questions over here. Financial condition, the compliance, AML related part.
and the documents that they have to provide, the insurance related details. And once they have provided everything, they'll get to review and then again, they'll get the summary of everything, if everything is completed or not. And once that is done.
they'll get, okay, you have, your part is done and now Hazel will be reviewing your documents. And if Hazel needs additional details, they'll reach out to them. They will ask them to provide more information, upload any more documents.
And here we have the document center where they can upload all the documents that they want to. So this is still the cover base part, till the Hazel review part. Once this is done, we can move forward with the account creation with interface and prelims. Yeah.

Aaron McWilliams   19:00
Wow.

Shawn Main   19:02
Right.

Aaron McWilliams   19:02
Yeah, yeah, some good work done yesterday. Looks looking good.

Shawn Main   19:05
Yeah, yeah, look, looking, looking really nice. Yeah, I like, I like it, obviously. Yeah, we just need to validate some of the inputs and data and titles and things, but yeah, I like the like the thought process and the flow.

Aaron McWilliams   19:21
Yeah, so the biggest change is just that you've created a login portal now. And so, so it looks like after that, yeah, they express interest and then they get the code, then that's when they create their account. Is that the next screen there?

Shawn Main   19:22
Yeah.

Pallavi Bichpuriya   19:40
Yeah.

Aaron McWilliams   19:40
And.
Okay, so yeah, Shawn, you like that kind of that process?

Shawn Main   19:48
Yeah, yeah, I think I think that makes a lot of sense. That way, you know, they can just track it because this is going to be very asynchronous. They're going to come in one day and put in some docs and then they're going to, you know, we're not going to hear from them for a week and they're going to come back and like, what the heck's happening? So it might as well have it to where they can just go check on things.

Aaron McWilliams   20:00
Yeah.

Pallavi Bichpuriya   20:08
And there was one more thing related to the risk questions that we were discussing yesterday.
Like if somebody wants to, since they have to provide all these details, it might get tedious. So we were thinking if in the, one minute.
Yes.
Okay.
In the risk questions, they have to provide all these details, right? So if we can use some sort of AI and then all these details can be, AI can help them in filling those details. But then again, it will be a cost to the company because again, we'll have to give some API access.

Shawn Main   20:44
Yeah.

Aaron McWilliams   20:55
Well, and even for like that question, we can probably do multiple choice.

Shawn Main   20:55
Yeah.

Pallavi Bichpuriya   20:59
Okay.

Shawn Main   20:59
Yeah, and I guess, yeah, that's the question, like, what would actually be different? Everybody's going to use Hazel for mostly the same reasons.

Prashant Sarode   21:00
Support.

Pallavi Bichpuriya   21:08
Okay.
Okay, that makes sense.

Aaron McWilliams   21:10
So, I...

Prashant Sarode   21:11
Yeah, so, so I think Shawn, you had sent a note to us, right, saying, like, listen, wherever possible, I mean, the nature of this onboarding process, the lesser it feels burden us and less friction, the better it is, so, so I think we were like trying to understand, like, hey, where all we can have AI agents.

Shantanu   21:20
It.

Prashant Sarode   21:33
Of course, running on Databricks Infrastructure, start to help out either in pre-filling.
for the member banks or behind the scenes the agents are doing some work and then the decision making for the users, the market operations users is much more lesser cognitively intense.

Shawn Main   21:57
Yeah, that's right. So that's where I would think, you know.
Why wouldn't we just ask them, like, provide your Wolfsburg questionnaires or whatever, send it to cover base. Cover base isn't going to pull out and extract all that information, and then you're kind of just asking them to confirm, you know, is this all correct? And I know Chris has got his hand here, but, you know, just like, and even for the intended uses, like I said,
Hazel's designed for them to use it for a lot of different purposes. I would question why do we need to even ask that question? But yeah, Chris, go ahead.

Aaron McWilliams   22:30
Yeah.

chris colson   22:34
Yeah, so on the first page where it has express interest and invitation, I noticed there was an expiration date there. If I start to complete this, and to Sean's point, a couple days later I come back, does that expiration then keep me from
Completing the process, or once I begin, that expiration kind of goes away.

Smital Lunawat   22:59
So that is basically just to make sure that usually when emails are sent out or whenever we send an e-mail with a separate link for, you know, that particular user, we'll attach. We were thinking of attaching an expiration per se pertaining to securities.

Shantanu   23:14
Thanks.

Smital Lunawat   23:17
And we also have an option which would say that, Pallavi, can you show the preview invitation states once?

Shantanu   23:30
No.
Yeah, Chris, call this as a process guardrails. You know, these are not like, you know, must and mandatory, but as you know, how do we deal with managing this all the process wise, right? That's where we thought of, and you know, we added that. It's all up to us to decide what we want to do.

Pallavi Bichpuriya   23:34
Mum.

Smital Lunawat   23:35
Then.
Yeah.

chris colson   23:43
Brett.

Shantanu   23:55
The goal is to collect mandatory information. Rest of the thing is how we control that whole process.

Smital Lunawat   24:06
So, yeah.

chris colson   24:07
Okay. I just wanted to make sure it wasn't after so many days, then they have to go back and start and then the frustration begins. My second question was going to be, if somebody doesn't accept and it goes past the expiration date, will that be captured for any kind of reporting? So if they come back later?
Sure, we know that they were issued at least one invitation. Is there any way to track those kind of things?

Shantanu   24:31
Yeah, so Chris, you know, change the question other way. We are ready to do the way you want it. You know, so this is just a presentation of one way. We are not saying this is how it should go.

Smital Lunawat   24:41
Yeah.

chris colson   24:41
Gotcha, okay.
All right.

Shawn Main   24:43
Yes.

Prashant Sarode   24:44
Yeah, yeah, so I think the important idea that the team is trying to say is, like, maybe we will not show the expiration date and confuse the users, whether this is expiration of the process, the process has to finish, but as Shawn said, this is a multi-day, sometimes multi-week process, so we don't want to accidentally confuse people.

Shantanu   24:44
Yeah.

Prashant Sarode   25:03
with expiration of invitation, which is more or less for two reasons. One is security reasons, as well as for the Hazel growth teams to figure out like, hey, I had these many interests out there and only X number of them actually accepted my invitation and actually registered and went forward, right? So there is a security angle to this expiration. I personally believe.

Shawn Main   25:25
Yeah.

Prashant Sarode   25:26
Everybody, we don't need to show the expiration date. I mean, if very frequently we get so many invitations, and those invitations are expired, including DocuSign's forming requests, right? And when you say, "Hey, I generate a new one, I think we'll have to we get a feedback, Shantanu, that, ohh, there is desiring understanding states."

Shawn Main   25:29
Good.

Prashant Sarode   25:46
of invitation, but we probably don't need to show the expiration date. Is that the correct assessment, Chris?

chris colson   25:54
Oh, I'm just asking questions, not making decisions. But that was my interpretation that like I don't want to create additional work where people are going to inquire, right? Because we're trying to automate everything.

Aaron McWilliams   25:57
Yeah.

Shawn Main   25:57
Yeah.
Yeah.

Shantanu   25:59
So...
Agree.
Yeah, sure.

Prashant Sarode   26:07
Yeah, yeah, you don't want to 1-800 phaser network call center bombarded with people calling. That would be a...

Shawn Main   26:08
Yeah.
Yeah.

Shantanu   26:13
Yeah, can you open that one page PPT?

Pallavi Bichpuriya   26:19
Yeah.

Shantanu   26:22
I, you know, we know what we have done. We have tried to do a few things which we know might be easy. Our, you know, go to the slide three. Yeah, what we are looking for, we are looking for making the due diligence.

Pallavi Bichpuriya   26:38
Yeah.

Shantanu   26:44
form and a risk question. These are the two screens which needs to be very correct because that's where functional data is getting captured.
If we can have someone give us more details on those like ask 10 question or this is a PDF manual form I collected today or XYZ needs to provide me one, two, three, 4 data. We are looking for that particular data.
to be discussed, show us something like these are the existing back-end system which needs to be functioned based on this data. So we are more interested in those two screens because that's the core of it.
So if we can get more details on that, maybe, you know, next hour we can have a discussion around that. We can review and we can make this whole workflow functionally, you know, more mature tomorrow.

Aaron McWilliams   27:52
I'm sorry, what? Two screens?

Shantanu   27:54
Due diligence form and risk questions. That is the core of it.

Aaron McWilliams   27:58
Okay.
Yeah.

Shawn Main   28:00
Yep.

Aaron McWilliams   28:00
Yeah, and that's what I was thinking. You know, we're about 90% of the way with deciding on those kind of things, you know, as things are moving pretty quickly. So yeah, we just need to, what would be the easiest way for us to kind of get those screens or at least a list of the fields and.
Or should we just start with the list that we sent you?

Shantanu   28:23
Yeah, whatever you have, we are okay. If you are saying you have 90% ready, that's what we need right now. We are not worried about, you know, rest 10%.

Aaron McWilliams   28:31
Yeah.
Okay.

Shawn Main   28:35
Yeah.

Joel Olivares   28:35
I was just, hey guys, it's Joel. I was just thinking a little bit out loud. As part of that form field or the due diligence part of the intake, I think maybe we should consider taking a more dynamic approach because we don't, like I said, right now we're just doing FDIC, but if we're going to go into different type of intakes in the future, I don't want to have a standard form that's going to
stop us from doing trusts or any other type of partner relationships. I don't know what the solution is. Does it go back to cover base and do the intake in that area and then come back to the dashboard? Or am I thinking out of line here or am I getting too far ahead of myself?

Shawn Main   29:15
No, no, yeah, I would I would put it as I know we're putting in the FDIC number as a part of that kind of initial request, but yeah, I think you're going to need a step that says, you know, you know, in that first form, are you a credit union? Are you a bank? Are you a trust? Are you a fintech? Like, who are you? And in that
defines kind of the next steps for those screens. Like you put an FDIC number, do you put in an NCUA certificate, stuff like that. So I like to kind of keep it open so we're not boxing ourselves in for onboarding to just be a bank because the due diligence will be relatively similar.
And then the last thing I'd say, Prashant, to your point on like bringing in AI, what I really mean by that is, you know, is there a way for us to not have to create a ton of screens to collect information and tailor those screens to every single different use case of information we're trying to collect? Is there a better way?
to more dynamically generate, you know, the information we need out of the documents or, you know, whatever. And again, we don't have to, we don't have to kind of shrink this to just be a chat with the bot and, you know, give me your information and it'll just fill it out. I think that's too much of A behavioral shift, but are there other ways to.
Yep, kind of prepare for that.

Shantanu   30:37
Yeah, I think.

Prashant Sarode   30:37
Yeah, so, so, so, so I, I, since we were at that point, right, so, so the part that we do not really understand collectively, I think, is the information that we are asking.
Should we even ask that information and source that information from somewhere? And is that somewhere? So I think the current mindset of the user experience is, give me member bank this information that I need, right? And then, and Joel asked, and Joel.
put a nuance around it, we'll get to that too. But the model is give me your information and I will verify. But can the model be just give me your identifying information, the number, FDIC number. And if I have that number, I will pre-fill all this information for you. And the reason I'm making you go through the screen is check this, that is sourced from outside.
and the definition of outside is either cover base or some other data source, take this, correct this, and then hit submit. Is that the metaphor? If the metaphor is that, then we, the nature of the conversation in this meeting changes, and we simply start to say, hey,

Robert Ramirez   31:46
Yeah.

Prashant Sarode   31:57
Where should we get these sets of fields for each of these sections? You see where I'm going?

Shawn Main   32:04
Yes, and yeah, Chris, I know you've got something to say too, but my general thesis would be yes, if this is public data or data we can get from a data source, then I'd rather us pre-fill as much as possible.

chris colson   32:17
And, and Mike.

Prashant Sarode   32:17
So you want to prefill this and have them correct it and verify it versus making them go through it. But if it is a possibility, what is the data source? That's the question.

Shawn Main   32:19
Yeah.

Aaron McWilliams   32:30
Yeah, Shawn, I think that working with Castaneda, we added a handful of questions that probably are not going to be easy to pre-fill. So we just need to walk through those with you and just make sure you're cool with it. And we can do that offline.

Shawn Main   32:38
That's fine. Yeah.
Yeah, Chris, sorry, I know we've all kind of get run a little late.

chris colson   32:45
Yeah, no, no, that's fine. The question I was going to have is what about accordion style? So I know through like payment studies that you have a much better completion percentage rate for credit and other things. If you walk them through the questions that you need them to answer and anything that you can pre-populate, it just happens as they walked their way through.
So you were talking about bank versus trust versus, so you know what I mean? It's almost like a dynamic screen. We call it accordion. And then like understanding what is the maximum, like with buy now, pay later, any more than eight, I think there's like a 57% drop off. The average is like 11 steps. So I don't know if there's behavioral studies related.
into that or accordion style versus just having a form. I don't know if there's any thought put into that at all or not.

Prashant Sarode   33:36
Not yet. At the moment, Chris, we are in parallel. Shankar and I are looking at, hey, if Robin had a Robin Hood had to do this, how would they design this? If A fintech had to do this, how would they design this? So we are doing a little bit of

Shawn Main   33:36
Yep.

chris colson   33:50
Okay.

Prashant Sarode   33:55
So, you can't just do a user experience study, which does not take into account the domain and the users over here, right? So, if you have any resources to point us to, more than happy.

Joel Olivares   34:05
Oh.

Aaron McWilliams   34:08
Yeah, the drop-off was 58%, not 57%, Chris, but maybe I'm wrong.

Shawn Main   34:13
Yeah.

Aaron McWilliams   34:14
No, I think, yeah, I mean, this is this is even this UI is so different than what we looked at just 24 hours ago, so we're kind of doing, I think the team is just doing some rapid prototyping and building requirements as we're going, so, like, these are all great ideas that we wanna we wanna keep, you know, listed out so we don't forget, but really it's just kind of the...

Prashant Sarode   34:15
Yeah.

Shawn Main   34:20
Yeah.
Yep.

Aaron McWilliams   34:35
The big building blocks is kind of what we're trying to figure out at this level, so...

Shantanu   34:40
Yeah, and you know the reference for this was the e-mail Avenue sent with two Excel. One Excel was with, I think that one Excel was more around, I think the questions, risk assessment questions.

Aaron McWilliams   34:50
Mm.

Shantanu   34:59
And then the second was was around due diligence, some of the data content from the form. I think if we really want to have the cover base review, like how we set this up into cover base currently, and then...
you know, have that understanding maybe today, today or you know, later today or tomorrow, we can make this thing better.
I think we were talking about Joel to give a demo for that cover page or no.

Joel Olivares   35:38
Yeah, I'm still working on it. They had to, they just messaged me that they need to reschedule, but they're definitely still on and I'm working on an e-mail to give them context about what we want to achieve. So if I give him a little bit of a preset, then maybe he can bring in, I don't know, development team or somebody more knowledgeable than just.

Shantanu   35:49
Mitch.

Joel Olivares   35:58
standard support so that you guys may be ready for some questions if necessary, but I do want to give them an overall picture of what we're trying to achieve with between Hazel and the intake and cover base. So, go ahead.

Shantanu   35:59
Good.
Yeah, but.
No, no, no, sorry. I was saying if you have access, can we at least see what is coverbase?

Joel Olivares   36:17
Yeah, of course, yeah. Do you want to do that right now or?

Shantanu   36:19
So that can be one hour day or tomorrow. That's what I was saying. Maybe today, later, or tomorrow. See, for us, we just know the name. We have not seen it. What is mean by adding an organization into the cover base, right?

Joel Olivares   36:22
Yeah, absolutely.
Yeah, totally. No problem at all.

Shantanu   36:35
So, so we can have one hour of a session, literally, maybe now or later today.

Joel Olivares   36:42
So I can give one quick tutorial and kind of give you guys an idea of what the UI looks like and what it does. But I also invited you guys to next week's cover-based training class that hopefully I'll tell them to record and then we'll have that available for the future as well. But you guys are also invited to that call.

Shantanu   37:02
That's nice. Thank you.

Aaron McWilliams   37:08
Anything else today we need to touch base on?

Prashant Sarode   37:13
Yeah, I mean, I think this made a very good point and I mean got me thinking. This, if there is a research around dropout rates on an onboarding process, typical of onboardings, et cetera, that you have, share that with us, that can help us.
So I think what we are trying to do, the team is trying to do is, okay, let's figure out the whole workflow. The same workflow can be imagined in multiple ways, but if you send us the research, where is the dropout rate happens? Like there must be some fintech research, onboarding research. And if we look at that, maybe we'll design this slightly differently. So that's one thing.
And the second thing is, either I know somebody from the advantage side, if you can tell us, like, confirm the idea. Well, the goal over here is not to collect the information from the member bank. The goal over here is to verify the information and correct if the pre-filled information is wrong.
If that hypothesis is true, then we need to take that seriously and make mental adjustment from a workflow perspective. The two pieces of input is sharing some research on UX, dropout rates, etc., and we...
Designing the system or by user experience to assume that will be a data source which we will or data source for more than one data source which will which we will use to prepare.
So the model is collect only if we cannot pre-fill, and for every pre-filled field, you have to have a connotation of correct if you if it is not right.

Shawn Main   39:02
Yep.
Yep, I think that's great. Yeah, really appreciate it.

Prashant Sarode   39:14
Anthony is already a bad, bad person for all young Indians. He made them slog very hard yesterday.

Aaron McWilliams   39:24
I didn't catch that, but...

Prashant Sarode   39:27
I said, Shantanu.
Made it a mission to get this thing end-to-end done, so our kudos to Shantu and theorem teams. I will.

Shantanu   39:30
Bill.

Aaron McWilliams   39:34
Huh.
No, I'm impressed again every day.

Shantanu   39:40
I think, yeah, our challenge is we are, you know, we have a lot of missing pieces and to get that out, we are trying to see what we can bring it onto the table so that at least you reject it saying this is wrong, right? So we know we are not going to go that path.

Aaron McWilliams   39:59
Yeah, yeah, well, I think I think the improvements you guys made today are definitely on the right track, and yeah, we're running percent there on the questions, and so we'll kind of work through those on our side next, but anything, yeah, anything else though for for today?

Shantanu   40:16
Any, yeah, anyone, you know, do we have like a user manual or something of a cover base? We'll go through those so that we can try and understand what do you mean by setting up an organization in cover base or or.

Aaron McWilliams   40:30
I think I sent the API documentation a little bit back. I know that's, is that what you're talking about maybe or?

Shantanu   40:37
Maybe that's okay too, but we want to understand from two sides. One is from the API side and one is from the front end side, functionally and technically both.

Aaron McWilliams   40:46
Mm.

Smital Lunawat   40:54
Just a.

Aaron McWilliams   40:55
Yeah, we can look. Maybe Joel can look for that.

Smital Lunawat   40:58
Tate.

Aaron McWilliams   41:00
Some trainings, or, I mean, the demo will hopefully answer all of that, but...
Guess you can't throw that into AI. So yeah, Joel, any ideas on Coverbase user manuals that are something written out there?

Joel Olivares   41:15
Yeah, I think they have a pretty good setup. So if I have a second, I can start downloading some stuff, or when we need to get you guys access to that platform, I can definitely do that as well. Again, I just don't know if I can give you guys access to it with your Theorem Labs e-mail, or do I have to create a cover?
advantage.bank e-mail. So that's kind of still up in the air. I haven't really dug into that part of it, but what I can do is see what I can download as far as PDFs and tutorials and how-tos that we could probably even bring back into an AI to summarize what you guys may be looking for.
But hopefully the training will give you a little insight on what it does and how it operates.

Shantanu   41:57
Yeah.
And you know, like, if you want to have a meeting today so that you can share something, and we would, if you feel we should join, we are open for that too. Yeah, just messaging the grouping.

Joel Olivares   42:11
Yeah, yeah, absolutely. If you guys want to...

Aaron McWilliams   42:13
But...
And actually, I mean, I can do a quick one for those who want to stay on, just because I at least have access to that.
And I could do that now. Just take 5 minutes or something.

Joel Olivares   42:31
Okay.

Aaron McWilliams   42:33
So yeah, if anybody else needs to drop, that's fine, but let me...
and find the link. There it is.
Mm.
I guess, well, not much to see yet. Okay. Lunch o'clock. Well, maybe I do need to go. That made me hungry. Okay. Here is the Hazel Network and I've...
Um...
I've done a few tests here. And actually, Joel, I got a call with Rio Bank tomorrow, so I might go ahead and create.
a form for them in here. So if I go and fill out a new request, actually, yeah, I'll just set up a real bank while we're doing this since I need to do that. So I just go in here and I type in their name.
Thanks, name, and then Coverbase does searches the web to bring in any public information that it needs for that here.
And then...
It asks for here, and I don't know why it asked for the use case here, but...
I just put in, he's a member bank.
See here on the right, you can see it already pulled up some basic, it knows its location and has a description.

Shantanu   44:21
This call is recorded right now.

Aaron McWilliams   44:23
Yeah, yeah, and I can get you guys the video on this one.
And so, yeah, it's looking for similar vendors. So maybe over time it will.
Can I improve the...
The questions it asks and things and knowing what we're asking for a Hazel member bank, but we do have a workflow already that Joel created in here.

Prashant Sarode   44:55
So, cover base was a quote un quote updated in this idea that he, this, there is a use case called his and his member bank.

Aaron McWilliams   45:04
I...
Joel, does that change? I don't think that changes anything right now. I think when I went in the beginning, I went to the Hazel member bank.
workflow or module and so it's running the one workflow it has in there. So, but it looks like it did a check on financial staining security posture and sanctions.

Prashant Sarode   45:30
Using what information?

Joel Olivares   45:33
Yeah, they go, they go out to they, I mean, they have public information, so they're basing it based on public information that they can gather this. This is not on any kind of due diligence documentation or financials or anything like that just yet.

Prashant Sarode   45:39
The.

Joel Olivares   45:47
Actually, probably not ever for this Hazel Network process, but on a standard Vendor or onboarding, you know, later that would be a more in-depth due diligence approach or risk assessment approach, but for for this process, it's just using public information to gather financial standing and security postures. It's going.

Prashant Sarode   45:56
Yeah.

Joel Olivares   46:09
Coverbase has a module called Radar, so it's scanning different.
sites and negative media, door rogs and IP reputation and patch management, stuff like that. So it can give us a security posture pretty accurately based on what it knows about the IP address.

Prashant Sarode   46:30
Right, so to answer your question, verifying question for a moment, let's ask the user convenience of it. Remember guys who are going to fill the form that we were just looking at earlier, right?
Independent of convenience, right? How the form got filled?
Is the idea that, ohh, OK, Powerbase has access to public information?
And it will, without anything, it just took some real bank thing and it did it did some verification based on the problem data.
Now, this new information that we are collecting.
How will this use this new information?
I assume the user experience was not.

Joel Olivares   47:14
Honestly, I don't know how to answer that just yet. I think that might be a Coverbase question for our next meeting, but yeah, I'm curious to know, I mean, if we had that data that you collected and it was created into a text file, for example, or a Word document, whatever, that could be stored in Coverbase's document storage, and then that gets used in their AI.
verification process as well. So any data that I put into it, although I know there's been questions asked that we may not want to track MPI information in cover base. So I was confused about that part. But yes, if a document was created that was collected from the intake process and dropped in cover base.

Prashant Sarode   47:49
Yeah.

Joel Olivares   47:59
Then, Coverbase is AI can use that data to reanalyze what they know about that partner.

Prashant Sarode   48:06
So, so, so...

Joel Olivares   48:07
Along with what they know, right? So...

Prashant Sarode   48:09
So, Joel, I think I am, so my question is less technical and and mechanical, the question is more around.

Joel Olivares   48:15
Okay.

Prashant Sarode   48:19
On.
Think about it this way, right?
Is cover base a authority?
system which says...
Tell me, who, who are you asking information about?
Member Bank XYZ.
give me information about member bank XYZ, and I'm doing a background check on it. So let's say you are joining a new company, and they say, hey, give me your resume, give me where are you living. Nowadays, nobody does any kind of drug test, et cetera. That's the information that you give.
The moment you give that information, a set of background checks are looked up on federal, civil, county level, credit worthiness, criminal records. That's the background check of an individual. So over here, there would be is information connect. It is a background check service.
Analogically.
That's my understanding.
Is it a is it an information connecting agency or is it a background check issuing agency?

Joel Olivares   49:36
I don't not answer that, but I wouldn't think that it would be a background check issuing agency. It's more of a document verification and then that data that's collected is then reviewed against our controls, right? So I have to tell it what I want to do with that data based on the controls that I put in.
To it.

Prashant Sarode   49:58
Five, so then you are, so and and and I'm so you're so let me, so what you're saying is power base becomes a control point.
That represents.
Hazel Networks Due Diligence Authority. So it becomes Hazel Networks Due Diligence Authority by virtue of you establishing controls over here.

Joel Olivares   50:25
Yes, that's correct.

Prashant Sarode   50:25
And now, and now, whether information comes collected from the member bank or the member bank simply says, here is my FDIC ID. Don't tell me anything more. If you just give me your social security number, I will figure out everything about you.
Right, so, so then the hypothesis is what information that you need that that neither cover base has.
Access to.
And therefore, the member bank has to give.

Joel Olivares   51:06
I'm not sure I understand that question, but I mean, that's kind of part of our intake process, right? So the document that we provided yesterday, the Excel document, that shows the intake process, the intake questions, that's the data that we collect to begin a review process against our controls.

Aaron McWilliams   51:09
Oh.

Prashant Sarode   51:24
Okay, okay.

Joel Olivares   51:24
So there's 40 questions and then there's 52 controls. But the data, I mean, if the data is verifiable and it comes from somewhere else, like say,
Uh...
using the Fiducia account to verify existence and taking data like address and headquarters and phone numbers and all that good stuff and then brought into cover base and that can be used as well. It doesn't, I don't believe that it has to come from the intake form alone.

Prashant Sarode   51:53
Understood, understood.

Joel Olivares   51:54
So if I uploaded documents also that were not required, aside from the Wolfberg and the BSA policy, and I uploaded other documents like the EIN or the W9 or whatever, I don't, you know, whatever policies that they may have given us just because they wanted to, then that data too could be used to assess
The partner.

Prashant Sarode   52:17
Are okay, so I think, I think...
Shantanu and I have probably talk offline.
But what it seems to me at a high level, Joel, that...
You know, this is about a third-party.
Third party background check kind of a scenario. This is like, hey, this is the network operators.
This authority is decision and due diligence.
Today, it is collecting data of.
Darak.
collecting the data, some of it is sourced from the web, some source from the member bands directly.
The product management challenge here is...
looking at what data we are collecting, and that goes back to the dropout rates and the friction that is perceived by member bank. If we can look at that, the data that we are trying to eventually collect, whether we collected automatically from behind,
What I mean by behind meaning searching the rug or we collect that data from the member bank in the form of, hey, we already sourced half of the data, the ones which we could not source, you fill in and verify the one which we refer. All of that data will be evaluated against the controls. And what Coverbase offers is a...
Is like an engine which represents is a networks risk disposition.
Joel, is that that long commentary makes sense to you, or it doesn't?

Joel Olivares   54:06
It does, yes.

Prashant Sarode   54:09
Okay.
So, in itself, is just an engine if you make it.

Shantanu   54:16
Yeah, but let him, yeah, sure. I mean, he can he can continue, right? We can see that.
This is the first screen only, right, Aaron? Do you need to show more screens?

Aaron McWilliams   54:28
Yeah.
Yeah, and I think at this point, I mean, all it's done is really just pull in a website location and probably the SEO description from Google. So I mean, it did some of these checks, but I don't, I think it can do that through the API. So again, I...
I do think that as long as, excuse me, you guys are just asking the main fields and they have API so that you can pass that to Cover Base, it will do this in the background for us. So on this page, the only document I have now is the MDA that they send.
Sign, so I threw that in here. I don't think that's gonna help.
With answering any questions or anything, but, and then...

Shantanu   55:18
So who signed the IND here?

Aaron McWilliams   55:20
So, Rio Bank signed that, and so...

Shantanu   55:23
Oh, so whatever the signed NDA you had it, you uploaded it to them now.

Aaron McWilliams   55:28
Yeah, they sent me this morning, so I just threw it in here. Now, again, in our in our in our workflow, we probably don't need to do that, but...

Shantanu   55:31
Okay. Okay.
We need it, right? We are talking, look, we are looking for India to be sent, yeah.

Aaron McWilliams   55:39
We will need it, yeah, but I don't think we need it in cover base, is my point.

Shantanu   55:43
Correct, correct, correct. OK, so that is once you send the these are the questions. Is that what it is? It is, or this is additional information.

Aaron McWilliams   55:46
Hello.
Yeah, and one thing I've noticed, Joel, is that these questions change a little bit each time, but some of them are standard. So, you know, are they a pilot member bank? I don't know. I cover base needs to know that. What's their primary intended use case?
Okay, so that's one of the questions that we had in there, Aaron, so it's just asking that.

Shantanu   56:13
Yes, Mittal Pallavi, take a screenshot of this, please.

Pallavi Bichpuriya   56:16
Yeah, yeah, I've been.

Shantanu   56:19
Yeah, sure.

Aaron McWilliams   56:19
Yeah, and I'll send you the recording.

Joel Olivares   56:20
Also, I, these questions I don't have control over, and so I believe that they're coming directly from Cover Base's AI intake, but I also believe that they're using this data to develop an inherent risk.

Shantanu   56:32
Which is nice.

Joel Olivares   56:39
on that vendor, before any residual, before any controls, before any data collection or anything. I believe that this data, I don't have control over it, but we can always talk to CoverBase about it. But I believe they're using this data to generate an initial inherent risk for that partner.
And that's probably why it shifts a little bit, right? Because if we'd said it's just a standard member or we left it blank instead of saying pilot member, the next screen may have different questions. I don't know that.
Man, it's starting to sound like I don't know a lot, right?

Aaron McWilliams   57:19
Ah.

Prashant Sarode   57:19
No, no, no, I think one thing is what I'm concluding is...
The questions and the question that the the workflow that we showed Shantanu, it feels to me now I understand what Joel was saying, right? Hey, can this be dynamic?
And, and...
Back to yep.

Shantanu   57:46
questions are coming from them, user is pre-filling it and we pass it on to them. Yeah.

Prashant Sarode   57:52
Yep.

Shantanu   57:54
So this is a, yeah, okay, so this is what institution profile and contact. Okay, so we are providing that information as well.

Aaron McWilliams   58:08
And I haven't seen these questions in the screen for Joel. Usually, it's in the next one. So it may have just kind of moved it around because it felt like these are more, these are less kind of, I don't know, risk-based questions and more just set up things.
I'll see if it'll let me skip that one. Okay.

Shantanu   58:32
Okay, insti institution.

Aaron McWilliams   58:34
So now we're in step 3, which is the full questionnaire.
And it's trying to answer them as much as it can beforehand.
Um...
Shouldn't be too much, but...
And so here, so here's we have 32 questions, 4 questions that I need to answer, 21 questions to review. So these are, yeah, like, so it re-asks that one or two team members who access the console. So I need to go and.
Fill that out here.
And these, this should be the list of questions that we sent you all in the spreadsheet. So these, it could not guess at, I think. And then on these 21 other questions, I think it tried to guess at the answer. So this is kind of the feature that Shawn was saying.

Shantanu   59:18
Yeah.
Yeah.

Aaron McWilliams   59:34
But again, like that just makes me question, especially for MVP one, is, is there a reason to just send people to cover base so that you don't have to rebuild all of this? This is a decent, this is a good user experience. So just throwing that out there.

Shantanu   59:50
Yeah, building Aaron, building this user experience is not a big deal as long as we understand what is behind it. So we will dig through what is behind it. And if you ask me what this would be, this would be a concept of setting up a tool.

Aaron McWilliams   1:00:02
Mm.

Shantanu   1:00:09
template in a cover base. So you set up a template in a cover base, you define who you are, what is your interest around the project, you want to drive, you collect the information and all. It might have some basic configuration at the beginning. And then, and that's what I see, you selected a project.
And then it will ask certain questions, and it will take you forward, but let's see, you know, let's see where this whole thing takes us through.

Aaron McWilliams   1:00:40
Well, and and what I'm looking at it is, you know, it somebody's it guessed at, but then it has the reasoning beneath, so that you know, user can kind of go through and understand that. So, probably what I will do tomorrow is I might on the call, if if I have time, you know, I could start.

Shantanu   1:00:48
No.

Aaron McWilliams   1:00:59
Asking.
Rio Bank some of these questions, or the...
The other option is just sending them this link, which...

Shantanu   1:01:13
So, yeah.

Aaron McWilliams   1:01:14
I don't remember where that is.

Prashant Sarode   1:01:17
So, you have a meeting with Coverbiz tomorrow, uh, that is this.

Shantanu   1:01:20
No, Prashant, it is it is next week. That's why I'm trying to, you know, understand this a little more into it.

Aaron McWilliams   1:01:28
So here I can go in and...

Shantanu   1:01:29
Yep.
No, but...
But, Aaron, did you finish that workflow or not yet?

Aaron McWilliams   1:01:33
And get.
No.

Shantanu   1:01:38
Why? I mean...

Aaron McWilliams   1:01:38
But what I did is I came here and now I have a URL. And again, you guys may not use this feature, but I have this URL that I think I can just share with people at Rio Bank. Is that right, Joel? And then they could kind of fill out themselves.

Joel Olivares   1:01:53
That's correct, yes.

Aaron McWilliams   1:01:56
So that may be what I would do tomorrow. But yeah, at some point I would go and answer all these questions and then I would click submit and I haven't been beyond that screen, so.

Shantanu   1:02:06
Yeah, can we do that? Let's see where it takes us. So these are the 20, 32 odd questions.

Joel Olivares   1:02:06
I.
Yeah, Aaron, we can delete that. We can delete the account once, once it.

Aaron McWilliams   1:02:15
Well, I'm just gonna, I'm just gonna pull up one of these other ones.

Shantanu   1:02:22
And this is production or this is a test.

Joel Olivares   1:02:25
Yeah, it's production, but it's fine.
Don't, don't, don't repeat that.

Aaron McWilliams   1:02:29
Aaron.

Prashant Sarode   1:02:32
Thank you.
Mitch.
So, Joel, this question, when you were onboarded on to call this, you provided them the template plus your question template, is that what you did?

Joel Olivares   1:02:50
Yes, so I generated that question based on what we believe would be industry standards for this environment.

Prashant Sarode   1:02:58
Back.
But then it chooses the questions dynamically based on what it knows to.

Joel Olivares   1:03:06
Right, and the response. No, are these questions that we're looking at right now, those are going to be asked no matter what, because those are what I wanted to ask for sure, because that will help us review the vendor and the controls, or the partner and the controls. But before the screen, those questions before this screen,

Prashant Sarode   1:03:06
Sorry.

Joel Olivares   1:03:26
More dynamic work from Coverbase, not from me.

Prashant Sarode   1:03:36
Yeah, you can.

Shantanu   1:03:36
So.

Joel Olivares   1:03:41
I'm sorry, I didn't get that.

Aaron McWilliams   1:03:42
All.

Prashant Sarode   1:03:44
Those are like coming from the Wilburg template.

Joel Olivares   1:03:52
Some of the questions are requesting the Wolfsburg, but the controls are where they're verifying the data for the Wolf from the Wolfsburg. And we can show, once we do this intake, I can definitely show you guys the control set.

Aaron McWilliams   1:04:02
Kassam.

Prashant Sarode   1:04:08
Okay.

Aaron McWilliams   1:04:09
Okay.

Prashant Sarode   1:04:10
Okay.

Aaron McWilliams   1:04:12
My test came out for some reasons.
Maybe.
Oh.

Joel Olivares   1:04:19
It's asking you to review, click on review.

Aaron McWilliams   1:04:23
Oh, I need to click on review. There it is. Okay, so that's a good feature to know.

Joel Olivares   1:04:26
OK, so that's a good feature now, and then that'll that'll timestamp that Aaron was the one that reviewed that question.

Shantanu   1:04:29
And these are all.
Yeah, this is all new AI standards by the way. Okay, so reasoning and reviewed, these are the new standards coming up onto the digital because of the AI populating certain data.

Joel Olivares   1:04:50
Excellent.

Shantanu   1:04:52
We will have this as well. Yeah.

Aaron McWilliams   1:04:56
Okay, so I tried to submit it. It sent me back and had me fill out the things I hadn't done yet. So I did that and...
Now, we'll see if we can fill this out and not notify Bank of America that we're doing this.

Joel Olivares   1:05:11
Yeah.

Aaron McWilliams   1:05:20
You submitted the questionnaire successfully. There are the documents.

Prashant Sarode   1:05:20
Thanks.

Aaron McWilliams   1:05:26
And then, yeah, start, I mean, that's...
That's it.

Joel Olivares   1:05:29
Yeah, so it's done. So now it comes into our end on the back.

Shantanu   1:05:29
Okay.

Prashant Sarode   1:05:29
The.

Shantanu   1:05:36
How will you know back in this is what?

Aaron McWilliams   1:05:36
So, here, there's a now it's a pending review.

Shantanu   1:05:40
Oh, okay. So now it's with the internal folks doing the work. Nice, nice, nice.

Joel Olivares   1:05:43
Right, right.

Aaron McWilliams   1:05:44
Yeah.
So that, yeah, so that.
That would finish the the process that we that you guys should be building here, so OK, thanks.

Joel Olivares   1:06:02
Uh, Aaron, if you want to bring it back up real quick, or I can do it on my end. Let me, let me just share my screen. Are we everybody okay with time? I don't know what the time look like, but let me show you.

Shantanu   1:06:02
Yeah, I think.

Aaron McWilliams   1:06:13
I need to drop in a second.

Shantanu   1:06:13
Beautiful.

Joel Olivares   1:06:15
Okay, let me just show you guys a little bit of what the back end looks like here.
Okay, so it's saying we have two partners, right? So intake, we saw that this is pending review.
Um...
So submitted by Aaron. Right now, the overall risk of this vendor is, you know, 79% critical. It does an analysis on what it sees. Question reviews, it answers that, document, the document attached. So what I want to do now is, this is ready for review, and if I see everything that I like here,
I can approve it.
And then what I'd want to do now is instead of onboarding, I want to onboard the vendor and then launch an assessment for this vendor. So the assessment is.
are going to control, is going to verify the responses in the documents attached against these Hazel partner bank controls. So each of these questions are category based.
And...
Each quest, each category has.
a domain risk, right? So governance authority, there's a team or a person behind this. So when an available question or questions come up for review, the people behind this domain risk are going to get notified saying, go look at these questions and let us know what you think, right, for approval. So also.
Each question.
Each question has a weight, right? So this is a control, this is what the guidance is for that question. And then...
This is a question that was asked to the partner. So that weight eventually gives us a...
You can't see it here, but once I approve it, it gives us a residual score based on what it analyzed. So right now it's just inherent score for all these categories. And then once the questions are approved or rejected or partially complete, then we get a residual score. Then I can go on and export a full assessment of that partner.
and what risk rating they have, which is something that we can present to somebody else like the approving committee.
So one more thing I want to show you from the back end is our scales. These are the levels of scales, which if it scored a 25, then it would be low, so on and so on. Going back to...
Risk domains, these are the different risk domains in the categories that we just talked about. I think the first one that we saw was...
Uhh...
I don't remember.

Prashant Sarode   1:09:18
So, the questions falling into a into a category, and the category itself is a domain category, right?
Yes.

Joel Olivares   1:09:43
it or disapprove it, then they have to, they can then go back to the partner and say, please provide more information.
But typically I don't see that happening with the Hazel network because the data is going to come directly from the Wolfsburg or if they're FDIC in this case, then we can get data from public information.

Prashant Sarode   1:10:04
And when you say the data is going to come from, do they fill the whole bug questionnaire on their own privately, or they they get?
I get to fill that either through our experience or through a URL that I was talking about.

Joel Olivares   1:10:22
No, so based on the initial intake questions and the controls.
It will also verify that the Wolfberg was attached, and it'll use that to answer different category questions that we have preset, like anything governance coming out of the Wolfberg.

Prashant Sarode   1:10:43
Accounts.

Joel Olivares   1:10:43
You know any gates compliance?

Prashant Sarode   1:10:45
What I was...
Right, the is a standard stuff, right?

Joel Olivares   1:10:51
Right.

Prashant Sarode   1:10:53
So...
My question was...
Our work questionnaire gets presented to the member bank inside cover base.
Auto.
The member bank does that independent of our base or our experience and does it on the side. It just uploads the answers to the rules for the questionnaire.

Joel Olivares   1:11:23
I don't understand. I don't understand. So the Wolfberg will be, you know, a standard intake document. It's not going to be dynamic. It won't be inputted by anybody. It'll just be the document provided.

Prashant Sarode   1:11:34
Find the Member Bank.

Joel Olivares   1:11:36
By the member bank, yes.

Prashant Sarode   1:11:38
But I got an answer to my question, so basically...

Joel Olivares   1:11:40
Or by us, or by us if they gave it to us in an e-mail, but theoretically it's data that was given to us by the member bank.

Prashant Sarode   1:11:48
Right, so, so, yeah, so they, they may need it for 10 other teams, and that is attached. OK.

Joel Olivares   1:11:56
Current, yes.

Shantanu   1:11:56
So, so that, so in the process, like after NDA, when we were talking about upload some document, that is where we should ask them to upload those documents.

Prashant Sarode   1:11:57
Yeah.

Joel Olivares   1:12:07
Yes, and that'll be a mandatory document that so without the.
policy or AML policy and the Wolfberg document without those two documents, the intake process cannot continue.

Shantanu   1:12:20
OK, Pallavi, and can you can you make a note of it? We want to make sure this this goes into our work.

Pallavi Bichpuriya   1:12:24
Yeah.
Yes.
So what are the documents required? Can you please tell us again what are the documents, Wolfsburg and the rest too?

Joel Olivares   1:12:29
Now, I don't know if we want to...
The.

Smital Lunawat   1:12:37
Beats.

Joel Olivares   1:12:38
There's only two documents, so it's going to be the Wolfer document and the BSA policy for that partner bank.

Pallavi Bichpuriya   1:12:44
Okay, okay, cool.

Joel Olivares   1:12:45
But the BSA policy, I think it has a few different names. You could call it BSA policy, BSL, AML. I don't know. Money laundering. Oh, ****.

Shantanu   1:12:50
Yeah.

Smital Lunawat   1:12:54
It.

Aaron McWilliams   1:12:54
OFAC is part of that.

Smital Lunawat   1:12:55
I think those the names were there present in the risk and the Vendor ID, so I think it.

Pallavi Bichpuriya   1:13:02
Yeah, yeah.

Aaron McWilliams   1:13:02
Yeah, it should be what we sent you.

Joel Olivares   1:13:02
Right.

Smital Lunawat   1:13:04
Yeah, but I'm just a little curious because if we plan to go ahead using the direct, because I feel that Corbase already covers a lot of, I mean, at least in terms of form filling, it provides a lot of support. So we'll have to see how do we.

Joel Olivares   1:13:04
Right.

Smital Lunawat   1:13:23
Incorporated.

Aaron McWilliams   1:13:23
Yeah.

Shantanu   1:13:26
So, so what I what I see as a need for us for Louis Mittal is get, you know, understand this work, like whatever we are seeing right now, then focus on the API and see what are all the APIs are available, uploading the document.

Pallavi Bichpuriya   1:13:36
You.
Mhm.

Shantanu   1:13:46
and pushing it to the cover base, the initial push, like the Wolfberg document in a question on, should be there as part of API. And the response from the cover base should be like, hey, set of 20 questions.
As a response from the API, then we...
Make another call with the API with the question and answer. So that's how the workflow should be there, all in the API as well in a code base. So verify what we have there.

Pallavi Bichpuriya   1:14:24
Yep, yeah.

Joel Olivares   1:14:25
Nice.

Shantanu   1:14:26
Yes, sorry, Joel, go ahead.

Joel Olivares   1:14:28
No, I just said nice. Yeah, that sounds right.

Shantanu   1:14:35
Okay, anything else then you want to show up?

Joel Olivares   1:14:40
Ohh, I don't know. I, I, you know, I can't, you know what? Let's approve, we can, if we have time, I can approve this vendor.
To approve it.
Start the onboarding.
We don't have an e-mail address in intake enabled in.
In this partner right, my Aaron.

Aaron McWilliams   1:15:11
I don't know. I mean, this is beyond what I've seen before anyway, but I mean, my understanding is that really all Ethereum is doing is just the intake of the documents and the questions, and then you do everything on cover base, but then at some point, there's going to be some, you know, web hookers communication back to the hot platform that says.

Joel Olivares   1:15:15
Okay.
Right, right.

Aaron McWilliams   1:15:32
Approved, ready to go, or...

Joel Olivares   1:15:34
I think what may still stay manual guys is this whole thing that I'm showing you then.
Adding a control, this is a 52 controls. And then...
Oops.
Um...
Adding the control manually and then telling it how I want it to verify this data. Import existing documents, which is these two that were uploaded, the Wolfberg and the PSA.
So then I have those two documents and then I start the assessment, right? So right now the inherent risk was 79. It's starting an assessment against my 52 controls and it's analyzing the controls and it's going to give me a result. Once I have a result and that's approved, then I can generate a
an executive summary type or in deep detail exec summary, then I think that with the overall score of that partner, and I think that's probably the best thing I can give you back.
So that you can say approve or not approved or automatically approved or automatically denied based on that score.

Shantanu   1:16:50
Yeah.
Yes.

Joel Olivares   1:16:55
Does that make any sense?

Shantanu   1:16:56
Oh yeah, definitely, yes.

Joel Olivares   1:16:58
Okay, so let's see if it does it pretty quickly so that we can at least see what the assessment would. So right now it's just analyzing it. Sometimes it's pretty fast, sometimes depending on the amount of data, it could take a minute, but...

Prashant Sarode   1:16:59
It was.

Joel Olivares   1:17:16
So at this point, if it wants more information, it can still go to, say, bankofamerica.com and get public information to help us better analyze that assessment, right, from the controls that asset. So I'm just moving things around here, but I wanted to see. When it's done giving us the reviews and
and compared against our controls, it'll give us a score here. For example, CoverBase, which is not a partner, came back as fully compliant. And this is what it found. It found five issues, and then they're not compliant because there's no data on this. But.
Again, these are not relevant to a partner questions, right? And these were the controls that it compared against.
The summary. So once it, again, nobody reviewed the questions. This is just an overall summary. Once that's done, then I can export to PDF and I can say I want an executive summary, standard or full. In this case, I believe that our best bet will be just a standard export. And I'm going to export the documents so you can see what that looks like.

Prashant Sarode   1:18:29
We have a big question, the control set that you are uploading. Why do you upload for every different member bank? Isn't it the same for all the member banks?

Joel Olivares   1:18:31
Chad.
Yes, that's correct. So this is just an example. So these controls are not what we're asking it. This is, I'm just doing like a CFS control review for another company called Cover Base, which is obviously the same company that we're using. But I only have one control set for partner banks.
So, let's just see kind of what, what...

Prashant Sarode   1:19:02
So then, then I, I'm slightly confused. What is this additional? What is this report? What is this additional control set per member bank?

Joel Olivares   1:19:12
Yeah, so the...

Prashant Sarode   1:19:13
Yeah.
Thank you, but we can't hear you.

Smital Lunawat   1:19:22
I think your voice got muted.

Joel Olivares   1:19:25
Oh my god, I just, I was on mute for the last 20 minutes. I was just talking out loud and I'm so sorry. Okay, so let me start over. So, okay, so we did the intake and we approved it and I...

Prashant Sarode   1:19:29
No, no, no, no, no.

Joel Olivares   1:19:45
Yeah.

Prashant Sarode   1:19:45
for less than 30 seconds.

Joel Olivares   1:19:47
I don't know how that happened, I'm sorry. So let me, so it reviewed against the controls and these are.
Oh, I'm sorry.
So this is the only controls that I have for the Hazel network. So if you notice I'm in the Hazel network now, these are the only controls that we're ever going to review as long as they're FDIC, right? Later when they're trusts or credit unions and I'll have different controls potentially if those questions need to be different. So what I was showing you guys was that we were doing an assessment and I'm just showing you

Prashant Sarode   1:20:01
Fine.
Yeah, yeah, yeah.

Joel Olivares   1:20:20
the cover base assessment because it's not done analyzing the Bank of America one, right? So once it gives us a score, then I came back and exported the document and this is the score that it gave us hypothetically again for cover base out of.
the 106 controls, which were, this doesn't apply because it'll say 52 controls. It'll give us key strengths, key weaknesses, and recommended actions if we want to continue a partner relationship with that. Then it breaks down all the categories of what was compliant and what was not compliant based on, again, this is
is just NCIST or NIST. In our case, it would say Hazel Partner Bank Controls, right? And then what was the score from that each category that we reviewed? Going back to controls.
What I just showed you in a breakdown would look like these breakdowns. So for each of these breakdowns, it's going to give us a score. It could be a three, it could be a two, it could be a one, depending on the document reviewed and the questions answered or how they were answered. So then.

Prashant Sarode   1:21:20
Sometimes, yeah.

Joel Olivares   1:21:36
These categories here will essentially be...
Ah.
I froze.
Sorry, guys, I froze here.
Yeah, I froze. Is that Victoria?

Victoria Santiago   1:22:10
I'm trying to...
Get rid of this, we want me.

Joel Olivares   1:22:15
Okay, let me stop sharing and then I'll come back.

Victoria Santiago   1:22:19
Yeah.

Joel Olivares   1:22:21
There it is. Okay, so what I just showed you here.

Victoria Santiago   1:22:21
Yeah.

Joel Olivares   1:22:26
They're gonna be in here, so it'll say partially compliant for.
governance and authority or security and operation verification. Ah, you're not sharing again. Dang it.

Victoria Santiago   1:22:34
Josh.
Are you sharing your screen?

Pallavi Bichpuriya   1:22:37
We.

Victoria Santiago   1:22:39
Yeah.

Joel Olivares   1:22:42
I'm having issues on my own over here. Okay, so we were talking about these different categories, say security and operation and governments and authority. Those will show up here, right? And it'll show fully compliant 3.5 or partially compliant 3.0 or not compliant at all. And it'll be a two or a one. And all these numbers here give us the ultimate average of this.
So I feel like this PDF document can be given back to you guys and you can use that to analyze an automatic approval or not. I don't know what that would be.
What do you guys think?

Shantanu   1:23:33
I don't think our application has any.
What do you call it? Intelligence build, because there is nothing we have it, right? Yes, so we have to think who has the authority to declare that this is approved or not. If this is a manual, then we push it on to the, you know, person.

Joel Olivares   1:23:45
No, that's fine.

Shantanu   1:24:00
If we are talking of writing some module or, you know, have some API from code base or some, you know, some authority, we can pull that through as well.

Joel Olivares   1:24:12
And so what that sounds great. And what I was thinking was this would be the document or not what I this will be the document that I present to the approving body. So if that's a.
Hazel Network approving committee where this gets presented and saying, Bank of America came back with a 3.5, they're fully compliant. You know, it's up to you to decide whether you want to move forward with them or not as a partner bank.

Shantanu   1:24:28
You.

Joel Olivares   1:24:43
or it came back with the two, you know, even after reviewing the Wolfberg and even after reviewing their BSA policy and their online public presence and the controls that we reviewed it against, it came back with the two, even though those documents were provided, it's still not fully compliant and the risk is higher than it would be if it was a 3.5.
So I think, and I'm just speaking out loud here, Aaron, I don't know what the details are from that step, but that step would be that the Hazel Network Committee would make the decision whether they want to follow through with that partner.

Shantanu   1:25:21
I agree.

Joel Olivares   1:25:24
Okay, so Aaron is saying that our approach should be automatic. So then this number, this document would go back to you and then that would make it an automatic approval.

Shantanu   1:25:38
Okay.

Smital Lunawat   1:25:43
So will there someone in the team who will review this document after the whole summary is being generated and then manually, you know, based on reading this document, approve it or will it be like...
Automation of even going through the document.

Joel Olivares   1:26:00
I it may it may be me, I don't know that yet, but it may be me to generate this document and then.
Once the document is generated, then I think maybe an API can pick it up.

Smital Lunawat   1:26:17
Yeah, sounds good.

Joel Olivares   1:26:21
But this step does have to be manual, unfortunately, because I believe that the owners of these domain risks still need to review it or look at it, or even if it's me that looks at them and approve them, or an SME, after all that's done, I still need to come in here. So now look, this Bank of America is back.
which is great. So it says it's minimally compliant at 46. So the inherent risk is critical. The residual risk is moderate. So then I can go look at the issues, and then the issues are all this stuff, right? So remember the domain risks that we talked about?

Shantanu   1:27:00
Mhm.

Joel Olivares   1:27:00
So none of these were compliant. So based on the data that was provided, none of these were answered. So what I could do is...
I can flag all these and then say create a follow up and then I can reply to Bank of America and say please provide responses to these controls. And if they do, then it automatically gets updated and says compliant, compliant or partially compliant or whatever. And that's automatically changing the overall.
residual risk. So let's say nothing happens and all these controls are left the way they are, then I just come in and export this document, keep it standard.
And then this document is what I'm assuming that we're going to use as a baseline to approve or not approve that partner. So it's saying, okay, it's minimum compliant at a 1.9, which is.
You know, 52 controls, it's less than 50%, right? So then it says, related to governance and authority, it's minimally compliant. Instead of a four, it's a 1.4. All these are ones, which does not look good for this partner. So honestly, in this very case, without follow-ups and responses to these controls.
then we would deny this partner.
I believe we would deny this partner because it is a below average. And I don't know what the average is going to be to say automatically approve or automatically reject. So I don't know if it's going to be a 3.0 or 2.8 or I don't know what that number is going to be.

Shantanu   1:28:21
So it.
So, there is a twin.

Aaron McWilliams   1:28:37
Yeah, we need to define that, but I think...
Once we have the score, it will tell us what to what to automatically do, yeah.

Joel Olivares   1:28:42
Mm.
But it sounds to me based on just this rough, you're right, Aaron, and it sounds to me that based on this rough step-by-step process, we're going to definitely have to follow up on some of these questions to our partner, potential partners and say, can you please give us more context on where your funding source is, you know, or something.

Shantanu   1:29:05
So that means, Joel, there is a to and fro happening right between the bank and Hazel.
To to and for communication, like we send some question, we reviewed it, we are asking to, you know, work on some more questions, right?

Joel Olivares   1:29:15
Yes.
Right.

Shantanu   1:29:24
Okay.

Joel Olivares   1:29:24
So, I'm...
A little bit concerned about these controls because it's telling me that the submitted the BSA OFAC document that Aaron provided is not compliant, which means it found some things in the document, but not enough for it to make a decision that this is a good Wolfberg document.

Shantanu   1:29:44
Mm.

Joel Olivares   1:29:44
Is this a real Wolfberg document, Aaron?

Aaron McWilliams   1:29:48
I had AI produced.

Joel Olivares   1:29:51
Oh, okay, got it. That's great then. That means that it's working.

Aaron McWilliams   1:29:52
Okay.
Yeah, yeah.

Joel Olivares   1:29:58
Sweet, sweet, sweet. OK, that's.

Aaron McWilliams   1:30:00
So I think I think two things that are interesting you identified is one is the your, and we're going to assign it to you for now, but your manual process and cover base after the bank submits it. And then on the second one is even if we can automatically approve them and move them to the next step based on score,
You still may have some controls you want to follow up on, which we just need to decide is that outside of the onboarding process or does it need to be done before we finish onboarding? So that's the internal decision.

Joel Olivares   1:30:25
That's correct.
School.

Aaron McWilliams   1:30:44
Then, as well, I need to drop for the next call, but I think we covered a lot, covered base. Thanks, guys.

Shantanu   1:30:52
Yeah, I think we have too many things to review here. One is the code base API and then all the UI workflow we have seen today.

Joel Olivares   1:31:04
Okay, in the meantime, if you guys want to set up calls with me for questions around CoverBase, I'd be happy to help.

Shantanu   1:31:05
Singh.
Nice, thank you very much, Joel.

Smital Lunawat   1:31:13
And click.

Shantanu   1:31:15
Thank you. Have a good day. Bye bye.

Joel Olivares   1:31:16
That's it? Okay, talk to you all later. Bye.

Aaron McWilliams   1:31:18
Thanks, everybody.

Shantanu   1:31:18
Thank you. Thank you very much.

Smital Lunawat   1:31:19
My, thank you.

Shardul Patki   1:31:20
Thank you, bye-bye.

Pallavi Bichpuriya   1:31:20
Thank you.

Aaron McWilliams stopped transcription
