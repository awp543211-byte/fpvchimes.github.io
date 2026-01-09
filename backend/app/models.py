from pydantic import BaseModel, Field

class Song(BaseModel):
    name: str = Field(..., max_length=50)
    melody: str = Field(..., max_length=300)
    author: str = Field(..., max_length=30)
    likes: int = 0
