from typing import Optional

from pydantic import BaseModel
from pydantic.schema import datetime


class PostCreate(BaseModel):
    title: str
    text: str


class PostRead(PostCreate):
    created: datetime
    user_id: str


class PostUpdate(BaseModel):
    title: Optional[str]
    str: Optional[str]
