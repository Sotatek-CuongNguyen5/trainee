from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from fastapi.responses import JSONResponse
import os
import io
import uuid
from core.image_processing import insert_text_on_image, insert_text_on_image_ver2, save_text_image_mapping
from utils.auth import verify_jwt
from utils.config import HOST, PORT

router = APIRouter()

@router.post("/insert_text_on_image/", dependencies=[Depends(verify_jwt)])
async def insert_text_on_image_route(image: UploadFile = File(...), text: str = "", text_color: str = "black", font_size_ratio: float = 0.1):
    try:
        if len(text) > 20:
            raise HTTPException(status_code=400, detail="Text exceeds 20 characters")
        if image.content_type not in ["image/jpeg", "image/png"]:
            raise HTTPException(status_code=400, detail="Unsupported image format")
        image_data = await image.read()
        image_stream = io.BytesIO(image_data)
        output_stream, base64_encoded = insert_text_on_image(image_stream, text, text_color, font_size_ratio)
        
        # Generate a unique ID for the image
        image_id = str(uuid.uuid4())
        image_extension = image.filename.split(".")[-1]
        image_filename = f"{image_id}.{image_extension}"
        
        try:
            os.makedirs("images", exist_ok=True)
            output_path = f"images/{image_filename}"
            with open(output_path, "wb") as f:
                f.write(output_stream.getbuffer())
            image_url = f"http://{HOST}:{PORT}/images/{image_filename}"
        except Exception as e:
            image_url = "N/A"
            print(f"Failed to save image: {str(e)}")
        
        save_text_image_mapping(text, image_filename)
        return JSONResponse(content={"base64_image": base64_encoded, "image_url": image_url})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/insert_text_on_image_v2/", dependencies=[Depends(verify_jwt)])
async def insert_text_on_image_route_v2(image: UploadFile = File(...), text1: str = "", text2: str = "", text1_color: str = "green", text2_color: str = "red", font_size_ratio: float = 0.1):
    try:
        if len(text1) > 20 or len(text2) > 20:
            raise HTTPException(status_code=400, detail="Text exceeds 20 characters")
        if image.content_type not in ["image/jpeg", "image/png"]:
            raise HTTPException(status_code=400, detail="Unsupported image format")
        image_data = await image.read()
        image_stream = io.BytesIO(image_data)
        output_stream, base64_encoded = insert_text_on_image_ver2(image_stream, text1, text2, text1_color, text2_color, font_size_ratio)
        
        # Generate a unique ID for the image
        image_id = str(uuid.uuid4())
        image_extension = image.filename.split(".")[-1]
        image_filename = f"{image_id}.{image_extension}"
        
        try:
            os.makedirs("images", exist_ok=True)
            output_path = f"images/{image_filename}"
            with open(output_path, "wb") as f:
                f.write(output_stream.getbuffer())
            image_url = f"http://{HOST}:{PORT}/images/{image_filename}"
        except Exception as e:
            image_url = "N/A"
            print(f"Failed to save image: {str(e)}")
        
        save_text_image_mapping(f"{text1}_{text2}", image_filename)
        return JSONResponse(content={"base64_image": base64_encoded, "image_url": image_url})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))