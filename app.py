from fastapi import FastAPI
from routes import image_text, text_management

app = FastAPI()

app.include_router(image_text.router, tags=["Image Text"])
app.include_router(text_management.router, tags=["Text Management"])
