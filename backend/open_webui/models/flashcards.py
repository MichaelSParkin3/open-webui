import logging
import time
import uuid
from typing import Optional

from open_webui.internal.db import Base, get_db
from open_webui.env import SRC_LOG_LEVELS

from pydantic import BaseModel, ConfigDict
from sqlalchemy import BigInteger, Column, String, Text, JSON

log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["MODELS"])

####################
# Flashcard DB Schema
####################


class Flashcard(Base):
    __tablename__ = "flashcard"

    id = Column(Text, unique=True, primary_key=True)
    user_id = Column(Text)

    front = Column(Text)
    back = Column(Text)

    created_at = Column(BigInteger)
    updated_at = Column(BigInteger)


class FlashcardModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    user_id: str

    front: str
    back: str

    created_at: int  # timestamp in epoch
    updated_at: int  # timestamp in epoch


class FlashcardForm(BaseModel):
    front: str
    back: str


class FlashcardTable:
    def insert_new_flashcard(
        self, user_id: str, form_data: FlashcardForm
    ) -> Optional[FlashcardModel]:
        with get_db() as db:
            flashcard = FlashcardModel(
                **{
                    **form_data.model_dump(),
                    "id": str(uuid.uuid4()),
                    "user_id": user_id,
                    "created_at": int(time.time()),
                    "updated_at": int(time.time()),
                }
            )

            try:
                result = Flashcard(**flashcard.model_dump())
                db.add(result)
                db.commit()
                db.refresh(result)
                if result:
                    return FlashcardModel.model_validate(result)
                else:
                    return None
            except Exception:
                return None

    def get_flashcards_by_user_id(self, user_id: str) -> list[FlashcardModel]:
        with get_db() as db:
            flashcards = db.query(Flashcard).filter_by(user_id=user_id).all()
            return [FlashcardModel.model_validate(flashcard) for flashcard in flashcards]


Flashcards = FlashcardTable()
