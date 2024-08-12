from fastapi import APIRouter, HTTPException, Depends
from core.load_text import load_texts_from_csv
from utils.auth import verify_jwt

router = APIRouter()

@router.get("/texts/", dependencies=[Depends(verify_jwt)])
async def get_texts():
    try:
        texts = load_texts_from_csv()
        return texts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/text_exists/", dependencies=[Depends(verify_jwt)])
async def text_exists(text: str):
    try:
        texts = load_texts_from_csv()
        if text in texts:
            return {"exists": True, "text": text}
        else:
            return {"exists": False, "text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))