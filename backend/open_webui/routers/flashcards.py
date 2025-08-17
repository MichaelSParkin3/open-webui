import logging
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from open_webui.models.flashcards import FlashcardForm, Flashcards, FlashcardModel
from open_webui.utils.auth import get_verified_user
from open_webui.constants import ERROR_MESSAGES
from open_webui.models.chats import ChatMessage, ChatResponse, Chats

log = logging.getLogger(__name__)

router = APIRouter()


@router.post("/new", response_model=Optional[FlashcardModel])
async def new_flashcard(
    form_data: FlashcardForm, user=Depends(get_verified_user)
):
    try:
        flashcard = Flashcards.insert_new_flashcard(user.id, form_data)
        return flashcard
    except Exception as e:
        log.exception(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=ERROR_MESSAGES.DEFAULT()
        )


@router.post("/class/chat", response_model=Optional[ChatResponse])
async def class_chat(
    form_data: ChatMessage, user=Depends(get_verified_user)
):
    try:
        chat = Chats.class_chat(user.id, form_data)
        return ChatResponse(**chat.model_dump())
    except Exception as e:
        log.exception(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=ERROR_MESSAGES.DEFAULT()
        )
