from fastapi import APIRouter, Header, HTTPException
from app.schemas.note_schema import NoteCreate
from app.services.note_service import create_note, get_notes 
from app.services.auth_service import verify_token
from app.services.note_service import delete_note

router = APIRouter()

def get_user_id(authorization: str):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing token")

    token = authorization.split("Bearer ")[1]
    user_id = verify_token(token)

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")

    return user_id


@router.post("/notes")
def add_note(note: NoteCreate, authorization: str = Header(None)):
    user_id = get_user_id(authorization)
    return create_note(note.content, user_id)


@router.get("/notes")
def read_notes(authorization: str = Header(None)):
    user_id = get_user_id(authorization)
    return get_notes(user_id)

@router.delete("/notes/{note_id}")
def remove_note(note_id: str, authorization: str = Header(None)):

    if not authorization:
        raise HTTPException(401)

    token = authorization.split("Bearer ")[1]
    user_id = verify_token(token)

    return delete_note(note_id, user_id)