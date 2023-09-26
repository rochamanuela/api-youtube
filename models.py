from typing import Optional
from pydantic import BaseModel

class Music(BaseModel):
    id: Optional[int] = None
    name: str
    artist: str
    year: int
    album: str
    genre: str