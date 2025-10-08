from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from pathlib import Path

app = FastAPI()

current_dir = Path(__file__).parent

static_dir = current_dir.parent / "static"
templates_dir = current_dir.parent / "templates"

app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
templates = Jinja2Templates(directory=str(templates_dir))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/images/icons/favicon.ico")


@app.get("/.well-known/appspecific/com.chrome.devtools.json")
async def chrome_devtools():
    return {"message": "No DevTools configuration"}


@app.post("/postdata")
async def postdata(username = Form(), phonenumber=Form()):
    return RedirectResponse(url="/", status_code=303) # {"username": username, "phonenumber": phonenumber}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
