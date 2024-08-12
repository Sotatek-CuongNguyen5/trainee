from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes import image_text, text_management, auth, image_display
from utils.config import HOST, PORT

app = FastAPI()

@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url=f"http://{HOST}:{PORT}/docs")

app.include_router(auth.router, tags=["Authentication"])
app.include_router(image_text.router, tags=["Image Text"])
app.include_router(text_management.router, tags=["Text Management"])
app.include_router(image_display.router, tags=["Image Display"])