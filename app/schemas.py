from pydantic import BaseModel, HttpUrl
from datetime import datetime

class URLBase(BaseModel):
    original_url: HttpUrl

class URLCreate(URLBase):
    pass

class URLInfo(URLBase):
    short_code: str
    created_at: datetime

    class Config:
        orm_mode = True  # This can help with object conversion
