
# Spanish Learning Mode Feature for Open WebUI

This document outlines the plan to implement a "Spanish Learning Mode" feature in Open WebUI. This mode will provide a dedicated environment for users to learn Spanish, with features like a lesson planner, flashcards, and interactive chat sessions.

## High-Level Overview

The Spanish Learning Mode will be a new tab in the Open WebUI interface. This tab will contain three main components: a Lesson Plan tab, a Flashcards tab, and a Class tab. All user interactions within this mode will be stored in a dedicated "Spanish Knowledge Base" in the vector database. This will allow the AI to personalize the learning experience and track the user's progress.

## Feature Breakdown and Implementation Plan

### PR 1: Basic UI and Spanish Knowledge Base

This PR will focus on setting up the basic UI for the Spanish Learning Mode and creating the "Spanish Knowledge Base".

**Files to be changed:**

*   `src/routes/+layout.svelte`: Add a new "Spanish" tab to the main navigation.
*   `src/routes/(app)/+page.svelte`: Create a new layout for the Spanish Learning Mode tab, with sub-tabs for "Lesson Plan", "Flashcards", and "Class".
*   `backend/open_webui/routers/retrieval.py`: Add a new endpoint to create and update the "Spanish Knowledge Base".
*   `backend/open_webui/models/knowledge.py`: Add a new model for the "Spanish Knowledge Base".

**New Functions:**

*   `create_spanish_knowledge_base()`: Creates a new collection in the vector database for the Spanish Knowledge Base.
*   `update_spanish_knowledge_base()`: Adds new chat messages to the Spanish Knowledge Base.

**Tests:**

*   `test_create_spanish_knowledge_base`: Verify that the knowledge base is created correctly.
*   `test_update_spanish_knowledge_base`: Verify that new messages are added to the knowledge base.

### PR 2: Lesson Plan Tab

This PR will implement the "Lesson Plan" tab, which will allow users to generate personalized lesson plans.

**Files to be changed:**

*   `src/routes/(app)/spanish/lesson-plan/+page.svelte`: Create the UI for the Lesson Plan tab.
*   `backend/open_webui/routers/chats.py`: Add a new endpoint to generate lesson plans.

**New Functions:**

*   `generate_lesson_plan(time_length: str, options: list)`: Generates a new lesson plan based on the user's preferences.

**Tests:**

*   `test_generate_lesson_plan`: Verify that the lesson plan is generated correctly based on the given parameters.

### PR 3: Flashcards Tab

This PR will implement the "Flashcards" tab, which will allow users to create and review flashcards.

**Files to be changed:**

*   `src/routes/(app)/spanish/flashcards/+page.svelte`: Create the UI for the Flashcards tab.
*   `src/lib/components/chat/Message.svelte`: Add a "add to flashcards" option to the context menu for chat messages.
*   `backend/open_webui/routers/chats.py`: Add a new endpoint to create flashcards.
*   `backend/open_webui/models/flashcards.py`: Add a new model for flashcards.

**New Functions:**

*   `create_flashcard(text: str)`: Creates a new flashcard from the selected text.
*   `get_flashcards()`: Retrieves all flashcards for the current user.

**Tests:**

*   `test_create_flashcard`: Verify that the flashcard is created correctly.
*   `test_get_flashcards`: Verify that all flashcards are retrieved correctly.

### PR 4: Class Tab and Integration

This PR will implement the "Class" tab and integrate all the features of the Spanish Learning Mode.

**Files to be changed:**

*   `src/routes/(app)/spanish/class/+page.svelte`: Create the UI for the Class tab.
*   `backend/open_webui/routers/chats.py`: Add a new endpoint for the class chat, which will use the current lesson plan and the user's progress to guide the conversation.

**New Functions:**

*   `class_chat(message: str)`: Handles the conversation in the Class tab, following the current lesson plan.

**Tests:**

*   `test_class_chat`: Verify that the class chat follows the lesson plan and adapts to the user's progress.

## How to Use This File with Gemini CLI

This `SpanishMode.md` file is designed to be used as a context file for the Gemini CLI. Here's a recommended workflow for using it to implement the Spanish Learning Mode feature:

1.  **Set the Context:** Start your Gemini CLI session by providing this file as context:

    ```bash
    gemini -c SpanishMode.md
    ```

2.  **Implement PR by PR:** Follow the implementation plan outlined in this document, focusing on one PR at a time. For each PR, you can use prompts like the following:

    *   **For PR 1:**
        > "Implement the basic UI for the Spanish Learning Mode and create the 'Spanish Knowledge Base', as described in PR 1 of the plan."

    *   **For PR 2:**
        > "Implement the 'Lesson Plan' tab, as described in PR 2 of the plan."

    *   **For PR 3:**
        > "Implement the 'Flashcards' tab, as described in PR 3 of the plan."

    *   **For PR 4:**
        > "Implement the 'Class' tab and integrate all the features, as described in PR 4 of the plan."

3.  **Provide Feedback:** After each response from the Gemini CLI, review the suggested code changes and provide feedback. If the CLI misunderstands a requirement or makes a mistake, you can correct it by providing more specific instructions. For example:

    > "In the `src/routes/+layout.svelte` file, you added the 'Spanish' tab, but it should be placed before the 'Chats' tab. Please correct this."

4.  **Run Tests:** After implementing each PR, run the corresponding tests to ensure that the new features are working correctly. If a test fails, you can ask the Gemini CLI to fix the bug. For example:

    > "The `test_generate_lesson_plan` test is failing. Please analyze the code in `backend/open_webui/routers/chats.py` and fix the bug in the `generate_lesson_plan` function."

By following this workflow, you can use the Gemini CLI to efficiently and accurately implement the Spanish Learning Mode feature in Open WebUI.
