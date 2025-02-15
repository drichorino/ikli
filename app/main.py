from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from .routes import router as api_router
from . import crud

app = FastAPI(title="URL Shortener API (NoSQL)")
templates = Jinja2Templates(directory="app/templates")

# Web Interface Endpoints
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Render the home page with the URL submission form."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/shorten", response_class=HTMLResponse)
async def create_short_url(request: Request, original_url: str = Form(...)):
    """
    Process the URL submitted via the form and display the resulting short URL.
    """
    document = await crud.create_url(original_url)
    return templates.TemplateResponse(
        "result.html",
        {"request": request, "short_code": document["short_code"]}
    )

@app.get("/{short_code}")
async def redirect_to_original_url(short_code: str):
    """
    Redirect the user from the short URL to the original URL.
    """
    document = await crud.get_url_by_short_code(short_code)
    if document is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=document["original_url"])

# API Endpoints under /v1/api
app.include_router(api_router, prefix="/v1/api")

# Custom 404 error handler
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse("404.html", {"request": request, "detail": exc.detail}, status_code=404)
