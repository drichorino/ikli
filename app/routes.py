from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from .schemas import URLCreate, URLInfo
from . import crud

router = APIRouter()

@router.post("/shorten", response_model=URLInfo)
async def create_short_url(url: URLCreate):
    document = await crud.create_url(url.original_url)
    return document

@router.get("/{short_code}")
async def redirect_to_original_url(short_code: str):
    document = await crud.get_url_by_short_code(short_code)
    if document is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=document["original_url"])
