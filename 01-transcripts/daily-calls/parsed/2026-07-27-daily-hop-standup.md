---
title: "Daily HOP Standup"
document_type: "transcript"
source: "meeting"
client: "Hazel"
date: "2026-07-27"
status: "parsed"
version: "1.0"
tags:
  - "daily-standup"
  - "hop"
  - "project-status"
confidentiality: "client-confidential"
source_file: "../raw/2026-07-27-daily-hop-standup.txt"
---

# Daily HOP Standup

## Transcript

Daily HOP Standup — Meeting Transcript
Date: Monday, July 27, 2026
Time: 12:00 PM – 12:30 PM CDT
Organizer: Aaron McWilliams

------------------------------------------------------------

[00:00:13] Joel Olivares: Hey guys, how's everybody doing today?
[00:00:47] Smital Lunawat: Hey, hi, Jameel.
[00:00:48] Pallavi Bichpuriya: Good.
[00:00:50] Joel Olivares: Uh, I know you, I don't know if you guys remember, but uh... Aaron's out this week, so I'll run point and see what we can discuss and what kind of progress we're at.
[00:01:09] Smital Lunawat: Are we?
[00:01:12] Joel Olivares: Yeah, just give it a few more minutes, see who else shows up.
[00:02:26] Prashant Sarode: Well, that's a nice watch. Is it a tag?
[00:02:29] Joel Olivares: It's not, no, it's called VAR. It's a micro brand out of California. I'm big on collecting watches from minority owned businesses and this particular company is owned by minorities in California. But they make really good watches. Most of their mechanics are Japanese.
[00:02:55] Prashant Sarode: Nice. No, no, I'm a watch collector myself, but unfortunately with the blood pressure and all this stuff, yeah, I...
[00:03:03] Joel Olivares: Oh yeah. You know, I got to tell you guys a story before we get started. My first cousin was admitted to the hospital because his watch was telling him he had a 165 heart rate — 165 beats per minute resting heart rate for him. And they thought his watch was acting up. He went to the cardiologist and it turned out he had a flutter or an inconsistent rhythm beat. He just got out of surgery yesterday morning. And it was because the watch told him — otherwise he just thought he was out of shape and tired. He had had it for a long time. It's obviously very dangerous to continue to have; even when you wake up from rest at 160, that's very high. And the watches are what really told him that he needed to go see a doctor.
[00:04:08] Prashant Sarode: Yeah, I mean, I heard lots of stories, that's why I started wearing one, but I hate this. I don't like it. I like the watches.
[00:04:08] Joel Olivares: Yeah, more traditional, too.
[00:04:20] Prashant Sarode: Yeah, I mean, it's — yeah.
[00:04:27] Joel Olivares: Okay, I think we're all here. We're just going to go through what we need to discuss and I'll take notes if I have to, but the goal is just to keep things moving while Aaron is out.
[00:04:46] Smital Lunawat: Yeah, so just starting off with a very quick talk over the infra setup. I think Shardul has some issues with the Teams setup yet. So if Robert or David could help him with that.
[00:05:15] Shardul Patki: Yeah, I tried to access the SharePoint, but I didn't get an e-mail address. I was provisioned an e-mail address for Vantage earlier this year. So I tried that out, but that is again not letting me log in.
[00:05:39] Joel Olivares: Shardul, can you drop your e-mail in the chat and hopefully Robert or David can take a look at that?
[00:05:48] Shardul Patki: My e-mail.
[00:05:50] Joel Olivares: Yes, I...
[00:05:51] Robert Ramirez: Sorry, no, what was the question?
[00:05:54] Joel Olivares: Oh, he's just having issues accessing Teams and SharePoint. And I was hoping we can verify his e-mail address because he said he never received an e-mail.
[00:06:03] Robert Ramirez: Okay, that was created by Homer and Hector. Send me the emails and I'll get with them.
[00:06:12] Shardul Patki: I'll paste it in the chat.
[00:06:15] Smital Lunawat: Yeah, so after that I believe the next step would be — I mean, we're still not there yet, but just wanted to bring it up about the later parts of the infrastructure setup, maybe the tools that we'd be using, the sandbox or the AI setup and all. So just wanted to check if we have any updates on it.
[00:06:44] Joel Olivares: I don't have updates on... Oh, sorry.
[00:06:44] Robert Ramirez: Yeah, we're currently working on — we were actually working this morning on finishing up the Azure tenant and all that. We do have the cloud PCs, but there's no use of using the cloud PC if the tenant is not completely set up. So that's still in process.
[00:07:05] Robert Ramirez: Since this is such a new tenant, Microsoft is asking for verification on setting up some of these. So that's what we're working on right now. I'm actually talking to legal right now to see what we can send them, what we're authorized for. We're working for Vantage Bank and then we're using a credit card pay-as-you-go from my boss. So they're just wanting verification, and that's what we're waiting on right now.
[00:07:36] Shantanu Wadodkar: I think this will be one time, but once we do that, the rest of the thing will fall in line, right? Including the OAuth and all this stuff.
[00:07:51] Robert Ramirez: I'm hoping for that, yes.
[00:07:55] Smital Lunawat: Yeah, and is anyone recording this meeting by any chance, just since Aaron is not here?
[00:08:04] Joel Olivares: I don't know how to do that. Victoria, do you know? The meeting's recorded.
[00:08:06] Shantanu Wadodkar: Yeah, it's saying it is. I believe the recording and transcript — yeah, it's already on, probably.
[00:08:10] Robert Ramirez: Yeah, it's already recording.
[00:08:12] Smital Lunawat: It's recording. And Joel, can you just try to see if, by the end of the meeting, you can send us the transcript?
[00:08:22] Joel Olivares: Yeah, of course.
[00:08:23] Smital Lunawat: Perfect. And then for the updates part, we have a few more UI things that we have built up, and if Pallavi you can walk through that quickly.
[00:08:46] Pallavi Bichpuriya: So we updated — all these parts were already logged in, expressing the interest and NDA signing. And after NDA sign-in, last time we talked about it, it was mentioned that first we need to have these two documents in place, and then only the member bank can continue to the due diligence part. So we made that change. Upload the document — and once these are accepted; if they are not accepted, we'll ask them to again upload the required document. Once it is accepted, we'll continue to the due diligence part, and the bank can now complete the form. The existing questions and visual design have still not changed. Hazel will preserve the bank's progress locally so the user can save and return to the form whenever they want. The risk questions remain locked until the due diligence part is completed. Once this is completed, they'll go to the risk questions and the bank will review, correct, or certify the prepared answers that are returned by Cover Base. Here we will be suggesting: okay, we are taking this information from the documents that you have already provided. Similarly, we saw that in Cover Base they were suggesting some answers. The member bank can confirm, or if they are not able to provide the answer, they will say "I'm unable to confirm," or they can correct their answers. From this point forward, the member bank only sees the appropriate general status. They will never get to know about the internal Cover Base scoring in the member portal. Once they have submitted their Hazel review, there are two parts after the submission. Either the internal Hazel operator can open the Cover assessment section and they will get the internal-only review where they will get the risk assessment score, risk band, findings, and related details. And if they find some information is missing, they'll come back to the HOP portal and ask the member bank to provide whatever information is required. Once the member bank submits and it is accepted, then — sorry, my screen share stopped. Is my screen visible? Once it is completed, they can now continue to the preliminary Interlace account opening. And here we have just whatever fields we thought are okay. We'll continue to the document preparation part. Now the thing is, we were not sure about whether the account number has to be provided before the signature or after the signature. So there are parts that we simulated: what if the member bank first completes the existing account setup information, and then we prepare the account number, so the account number is provided to them? All the details, the agreements, and everything — the DocuSign part is not yet integrated, but we will be integrating it, and once it is signed and accepted... If we are providing it after submitting all the documents, then the account number will be prepared accordingly. Once this is done, we can again go to the internal portal that is available to employees, and then go on to the next step from here.
[00:13:35] Joel Olivares: Pallavi, can I interrupt you for a second? I was thinking, before we go into the step of creating the account, the Infinite account — maybe put the opportunity for them to enter an account without having to go to the signup, in the event that they already have an Infinite account.
[00:13:56] Pallavi Bichpuriya: Okay, got it. Yeah.
[00:13:59] Joel Olivares: Does that make sense? If they don't have it, then they go to sign up now, kind of a standard flow. And then before I forget, I wanted to bring up another topic. If you go all the way back to the required documents, I spoke to the BSA team and they expressed — and so did Aaron — that there's potential that not all banks know what the Wolfsberg document is. So we need to strategically come up with a workaround on what other information we can gather in the event that they don't have a Wolfsberg document, because apparently not all banks have that, even if they're FDIC. So what I can do on my end is make an attempt to generate intake questions that could help answer some of the questions that we need from the Wolfsberg without mandatorily requiring the document. So that's something to keep in mind. I don't know what our next steps will be — if we want to remove the requirement of the Wolfsberg document but still ask for it, or if we want to ask questions around what it would require to get that information out of a partner. So let's keep that in mind for now. I'll talk to Shawn — you're on the call, do you have any intake on that?
[00:15:32] Shantanu Wadodkar: You're asking Shawn, right?
[00:15:34] Joel Olivares: Yeah.
[00:15:47] Diana Plata: So he's saying it's just a questionnaire, Joel. So if they don't have that Wolfsberg document, are we thinking that those same questions are going to be part of the onboarding process?
[00:16:02] Joel Olivares: Yeah, I think that would be our best approach. Now, I can incorporate some of those questions into Cover Base, but I believe it's better if they come from the Hazel onboarding that the team is working on.
[00:16:19] Prashant Sarode: So, Joel, while you were on that topic — that was also mentioned in Adam's meeting this morning — I did not understand the Trust Center connection. I understood that for certain member banks you already have an NDA established, but is the conversation the Trust Center? For non-FDIC members, the center already secures the NDA, so why ask for an NDA, right? The workflow.
[00:16:48] Joel Olivares: Yeah, sorry for interrupting there, but we do have a bit of an issue there that we're trying to wrap our heads around — what would be best practice. I do see the NDA, the Hazel Network NDA here, and that's great. But we also have to ask for it when they request our due diligence documents through Vanta or the Trust Center. And I know it's redundant, but I have to ask for it there to prove to the examining process that we are being compliant and requiring an NDA before we share our information. So I don't know how to work around that because I have to have it in Vanta as part of an NDA. And I know that it's better here too, so that we could start providing or gathering information from them. So I don't know how to approach that one.
[00:17:47] Prashant Sarode: Yeah, that's fine. But from a clarification perspective, there are two things I'm trying to understand. One is the Trust Center. Is the Trust Center nothing but a Vantage skin on top of Vanta?
[00:18:11] Joel Olivares: Yeah, so it's Vantage due diligence data, financials, policies, and also Custodia's risk assessment. And that includes reviews of the SOC report and all that, and also Infinite's financial SOC and all the other risk assessment data that we as Vantage completed, and we're showing our assessment there at the Trust Center. So it's really Infinite, Custodia, and Vantage providing what would be considered the Hazel Network due diligence package. That's where, when a partner wants to see that information, they'll get it from that Trust Center. But in order for me to provide that, I have to have proof in Vanta that they did provide an NDA so that the data could be provided to them.
[00:19:09] Prashant Sarode: Yeah, I'm slightly confused. The member bank wants to do their due diligence on Hazel and on Vantage. So they go over there. But during the onboarding process, it's the Hazel Network and Vantage trying to do due diligence on the member bank. So what I'm trying to understand is, in the flow — why or what NDA do we want them to upload? Why would they upload the NDAs that we make and present to the member banks again?
[00:19:54] Joel Olivares: Right, that's the part we don't understand just yet. Unless the NDA that you do in the intake process gets provided to Vanta, so they don't have to redo it.
[00:20:06] Prashant Sarode: Shawn is on a plane, but let us know what Shawn is saying.
[00:20:15] Joel Olivares: Okay, great. He's right, that would work out perfect. He's saying that if you sign the NDA through the Hazel onboarding or intake, then the NDA for Vanta would be automatic.
[00:20:21] Prashant Sarode: And when that would be automatic, okay. So then the NDA that we do with the member banks is the one that we need to upload, and we're good over there. Okay, so I think I'm good over there. The second question was: if a member bank is already on Hazel — in the offsite we had discussed, if you are already on Hazel, we have to automatically detect that and pull your account number. So in the short term, do we suggest, hey, give your Hazel account number to us? We're trying to do yet another integration with Interlace, which may or may not have easy integration for that from an MVP perspective. You see what I'm saying, Shantanu? Am I making sense?
[00:21:44] Shantanu Wadodkar: I lost you.
[00:21:44] Prashant Sarode: I'm just trying to refresh my notes from the offsite. In the offsite, some of the member banks would have an already existing relationship with Interlace. I think Interlace or... am I getting confused?
[00:22:06] Shantanu Wadodkar: Participate, participate.
[00:22:07] Joel Olivares: Participate.
[00:22:09] Prashant Sarode: Okay, sorry, Participate. So are we talking Participate or are we talking Infinite? Why would you have an Infinite account if you are not on the Hazel network? So my understanding was, if you are on Participate, then you may have some relationship with underlying infrastructure.
[00:22:28] Joel Olivares: I'm sorry guys, I don't know that. Diana, do you have any...
[00:22:30] Diana Plata: You're absolutely right. In order for you to be on the Participate network and Participate to debit your account, you would have to be a Hazel Bank Network member and have a Hazel Bank account already established. You're right.
[00:22:33] Prashant Sarode: For an Interlace account, not necessarily Hazel.
[00:22:48] Diana Plata: Well, I say Hazel because Participate is working for Hazel at this point, not for BaaS. So the account would have to be an account established under a Hazel Bank Network or member bank.
[00:23:08] Prashant Sarode: So from a user experience perspective — and maybe I'm just not following the functional side — Diana, I am a member bank and I already have a relationship with Participate and I'm part of the Openize loans program, which means I am already an onboarded customer, so why am I onboarding again?
[00:23:24] Diana Plata: Yeah, and that's, I think, where I was going with Joel. We would have already onboarded that account, that member bank and that operating account. What would be the need for them to provide the existing account number at onboarding if that already occurred?
[00:23:54] Diana Plata: That's to you, Joel.
[00:23:56] Joel Olivares: I'm thinking, if they had a Participate account — does that mean the only way to get a Participate account is if you're already part of the Hazel Network?
[00:24:07] Diana Plata: Right now, the only way — not a Participate account, you have your account established already under the Hazel member bank, right? The agreement with Participate is so Participate can come and pull or debit funds, or credit funds, whatever the case is, but the account is already established under Hazel. There's no such thing as a Participate account. Participate is only going to debit or credit the member banks' accounts that are already established.
[00:24:37] Joel Olivares: Yeah, so then, Pallavi, what that means is we won't — let's scratch the opportunity for them to enter an account number, because if they're going through the initial intake, then they don't have accounts with us. So they have to create them. So we do not give them the option to enter an account number, because they don't have an account number to enter to begin with, or they wouldn't be following those steps of onboarding.
[00:24:59] Diana Plata: That's right.
[00:25:09] Joel Olivares: So never mind on that first one. But we do have to still go back to the idea of getting the data for the Wolfsberg questionnaire in case they don't have a Wolfsberg document.
[00:25:34] Smital Lunawat: So would it be dynamic questions, or would that part be like an optional field to either upload the document or answer the questions? It can be either way, right?
[00:25:47] Joel Olivares: I think probably dynamic would be best and then just push that data. Well, I don't know if that's my decision.
[00:26:02] Shantanu Wadodkar: So Joel, what I would recommend: send the questions. If you have questions listed and those are like 4 or 5, we'll see how we want to deal with it — like a pop-up or a page. Another option is, the way we are saying "this is a Wolfsberg question, you want to upload, you upload" — or we can just provide a template. We can say, hey, this is our template, download a template, upload it as Excel. We can figure it out once we see the number of questions and type of questions.
[00:26:41] Diana Plata: Yeah, I agree with you. The only thing is that Wolfsberg is like a bunch of questions. So you're right — the first few questions, if you have the contract or the agreement uploaded, to avoid having to go in and answer 50, 60 questions, whatever number of questions are out there.
[00:27:02] Joel Olivares: Okay, so what I could do is ask BSA — I can run it by Fred and see if I can get him to send me a sample of a Wolfsberg document. And then I can forward that to you guys so that you can see what's provided in the report so that we can ask those questions.
[00:27:18] Shantanu Wadodkar: Yeah, but Joel, what I was trying to understand — you are looking for a sample of mandatory questions which are must-needed, right? And if a bank or an organization doesn't have Wolfsberg question-answers ready, then this is the set. Am I right?
[00:27:38] Joel Olivares: Right. Yeah. If they have a Wolfsberg, keep going. If they don't have a Wolfsberg, answer these questions.
[00:27:44] Shantanu Wadodkar: So these questions will be a smaller set, right?
[00:27:48] Joel Olivares: I think so. Let me look at the Wolfsberg document first and find out what's in it.
[00:27:51] Shantanu Wadodkar: Okay, sounds good.
[00:27:54] Diana Plata: I just sent it to you, Joel.
[00:27:56] Joel Olivares: Oh, okay. If it's in the chat, then — Santiago, you can get that from there and see what we can get out of it.
[00:28:04] Shantanu Wadodkar: Sure. I think Shawn is mentioning that — we will ask them, do you have that? And if not, then we'll ask those questions.
[00:28:07] Joel Olivares: Perfect.
[00:28:22] Smital Lunawat: I think Chris has a follow-up question: if the bank enters the name, then is there some automatic way to check what Wolfsberg report they have?
[00:28:37] Joel Olivares: I mean, that's a good idea, but I don't know how to do that. I don't know if we can tap into the Wolfsberg. It's a good question, Chris. I think that's going to have to be a takeaway, because I don't know if there would be a way to verify that just by the bank name.
[00:29:47] Smital Lunawat: Well then, do you think it is a good point to summarize today's meeting? We all have our work in place — you have research on your end, we have work on our end.
[00:30:00] Joel Olivares: We do have a couple of key points here. Let's see some of these bullets and see if we missed anything. And I'm sorry if I pronounced some of these names wrong, but Shardul — he still needs access to Teams and SharePoint, right?
[00:30:18] Shardul Patki: Yes, yes.
[00:30:22] Joel Olivares: I already got the Wolfsberg document from Diana, so I'll forward that to you guys, and then we'll see if we can investigate whether a bank name is enough to verify whether they're in the Wolfsberg program or have a Wolfsberg report. That was a suggestion by Chris. So we'll look into that. What else do we have that we just discussed?
[00:30:54] Diana Plata: No selection of the account number to enter.
[00:30:57] Joel Olivares: Yeah, that wasn't going to be there. That's not there right now, Diana. It was just an initial "should we do that," and now, with your help, we decided no. So she's going to continue the way she had it, Pallavi. And then this week, we also have the Cover Base employee training that I've invited Theorem Labs to join, so that we can get a better understanding of how it's navigated and how to enter intake and offboard and all that. Then the next day — I think Thursday, or maybe Thursday afternoon — we have another meeting just between Cover Base and Theorem Labs to discuss API connections and back-end data fields, or the possibilities of that. So that Theorem Labs can identify a way to push the data that they gather from the intake back into Cover Base for the residual risk assessment questionnaire. Did I miss anything?
[00:32:16] Shantanu Wadodkar: Sounds good, yeah.
[00:32:17] Prashant Sarode: No — and Shawn, I think we still have to figure out if we have to store the intake process documents into Databricks. So let's lock that piece down as well, Joel. And is there any update from the GitHub side in terms of readiness, etc.?
[00:33:04] Shantanu Wadodkar: I think Robert is tracking that — getting the access and all. Maybe in the next call we can discuss.
[00:33:10] Prashant Sarode: Maybe you talk to Maruthi, I think, so you might have listened.
[00:33:14] Shantanu Wadodkar: Thanks, guys. Thank you.
[00:33:22] Joel Olivares: Okay guys, we'll catch up tomorrow.
[00:33:26] Shantanu Wadodkar: Thank you.
[00:33:27] Smital Lunawat: Yep, bye.
