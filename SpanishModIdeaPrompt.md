Make a detailed plan to accomplish this. Think hardest.

How will we implement only the functionality we need right now?
Identify files that need to be changed.
Do not include plans for legacy fallback unless required or explicitly requested.

Write a short overview of what you are about to do.
Write function names and 1–3 sentences about what they do.
Write test names and 5–10 words about behavior to cover.

---

I'm thinking I'll tailor it for Argentine spanish first for proof of concept. So lets come up with a feature branch by feature branch or PR by PR organization plan for this idea. I will be turning this into a SpanishMode.md file to guide gemini CLI coding tool to code this. Keep in mind Open Webui is a platform to use llm's saved vector databases, embeddings, etc. we will make use of this exisitng functionality for our new features.

I want the below functionality:
- A Spanish Learning Tab above the Chats tab. Everything inside the Spanish Tab chats, etc. should be added to a Spanish Knowledge base. With a button to update knowledge base when you want to. The button adds everything to the knowledge base that hasn't already been added. If one of the chats (that had been previously added to the knowledge base) has new messages in it then add the new messages.
- Lesson plan chat tab; When you go to the chat you can click generate new plan checklist. The chat will use all spanish knowledge to generate a new lesson plan for the day. You can choose the aprox time length like 45min, 1hr30min, 3hr. You can choose from checkboxes to have text, video, audio, mic.  options referring to what the user will be expected to use for the lesson plan. Text for classic text reading, typing, video for watching youtube video snippets, audio for listening to audio, mic for using mic for speaking practice or stt + tts chatting with ai. The lesson plan will say whether to use the class chat tab or flashcards tab.
- Flashcards chat tab: this is a chat that will go through flashcards one by one with the user, I want the user to be able to highlight any text in any chat and select "add to flashcards" this will have a model generate a flash card front and back and add it to our flashcard storage, I'm not sure if the best way to store the flashcards is in like a json file seperate from the knowledge but maybe it is, 
- Class tab: chat that goes through the lessons with the user after a lesson plan has been generated from the lesson plan tab.

I think most of these can be done with prompts but the real power will be tying all 3 together so when there is a current lesson plan they are all on the same page and follow the current lesson plan, know the users progress so far, users mistakes, users wins, and can adjust if need be.

---

TASK: Generate a SpanishMode.md for Gemini.md to use as context to code this feature for open webui. https://github.com/open-webui/open-webui

Step 1: Look over the above info about the feature im adding.
Step 2: Look up best practices for context engineering for Gemini CLI or Claude CLI.
Step 3: Analyze the attached GEMINI.md file that is part of my open webui.
Step 4: Generate SpanishMode.md file.
Step 5: Give me tips and a guide on how to best modify/use the SpanishMode.md and Gemini CLI file and Gemini cli terminal together to code the best result. Include a workflow with prompt examples.