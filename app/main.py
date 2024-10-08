from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from app.routes import router

app = FastAPI()

# Configure Jinja2 Templates
templates = Jinja2Templates(directory="frontend/templates")

# Static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
