from app.firebase_config import db

def create_note(content: str, user_id: str):
    db.collection("notes").add({
        "content": content,
        "userId": user_id
    })
    return {"message": "Note created"}

def get_notes(user_id: str):
    docs = db.collection("notes").where("userId", "==", user_id).stream()
    
    notes = []
    for doc in docs:
        data = doc.to_dict()
        notes.append({
            "id": doc.id,
            "content": data.get("content")
        })

    return notes

def delete_note(note_id: str, user_id: str):
    doc_ref = db.collection("notes").document(note_id)
    doc = doc_ref.get()

    if not doc.exists:
        return {"error": "Note not found"}

    data = doc.to_dict()

    if data.get("userId") != user_id:
        return {"error": "Unauthorized"}

    doc_ref.delete()
    return {"message": "Deleted"}