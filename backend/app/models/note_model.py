from typing import Dict

class Note:
    def __init__(self, id: str, content: str):
        self.id = id
        self.content = content

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "content": self.content
        }