import string
import random
from datetime import datetime
from .database import db

def generate_short_code(length: int = 6) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

async def generate_unique_short_code(length: int = 6) -> str:
    """
    Generate a unique short code by checking the database.
    """
    while True:
        short_code = generate_short_code(length)
        exists = await db.urls.find_one({"short_code": short_code})
        if not exists:
            return short_code

async def create_url(original_url: str) -> dict:
    short_code = await generate_unique_short_code()
    document = {
        "original_url": str(original_url),  # Convert to string
        "short_code": short_code,
        "created_at": datetime.utcnow()
    }
    await db.urls.insert_one(document)
    return document

async def get_url_by_short_code(short_code: str) -> dict:
    return await db.urls.find_one({"short_code": short_code})
