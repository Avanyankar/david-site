from fastapi import APIRouter, Depends, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from schemas.request import RequestCreate
from services.request_service import create_request
from dependencies import get_db
from pathlib import Path

router = APIRouter()

current_dir = Path(__file__).parent
project_root = current_dir.parent 
templates_dir = project_root.parent / "templates"

templates = Jinja2Templates(directory=str(templates_dir))

@router.post("/", response_model=RequestCreate)
def create_new_request(request: RequestCreate, db: Session = Depends(get_db)):
    return create_request(db, request)

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/favicon.ico")
async def favicon():
    return FileResponse("static/images/icons/favicon.ico")

@router.get("/.well-known/appspecific/com.chrome.devtools.json")
async def chrome_devtools():
    return {"message": "No DevTools configuration"}

@router.post("/postdata")
async def postdata(username: str = Form(), phonenumber: str = Form()):
    return RedirectResponse(url="/", status_code=303)
