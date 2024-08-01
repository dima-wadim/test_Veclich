from pydantic import BaseModel

class Message(BaseModel):
    id: str
    username: str
    content: str
