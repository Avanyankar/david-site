from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

current_dir = Path(__file__).parent
static_dir = current_dir.parent / "static"

app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

from routers.dimburo import router as dimburo_router
app.include_router(dimburo_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
