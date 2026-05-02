from pydantic import BaseModel
from typing import Optional

class NoteCreate(BaseModel):
    content: str

class NoteResponse(BaseModel):
    id: str
    content: str