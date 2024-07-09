from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os
import io
from core.image_processing import insert_text_on_image, save_text_image_mapping

router = APIRouter()

# Mount static files directory
router.mount("/static", StaticFiles(directory="static"), name="static")

@router.post("/insert_text_on_image/")
async def insert_text_on_image_route(
    image: UploadFile = File(...), 
    text: str = "", 
    text_color: str = "black", 
    font_size_ratio: float = 0.1, 
    font_path: str = None
):
    try:
        # Validate input
        if len(text) > 20:
            raise HTTPException(status_code=400, detail="Text exceeds 20 characters")
        if image.content_type not in ["image/jpeg", "image/png"]:
            raise HTTPException(status_code=400, detail="Unsupported image format")
        
        # Read image file
        image_data = await image.read()
        image_stream = io.BytesIO(image_data)
        
        # Use core function to process image
        output_stream, base64_encoded = insert_text_on_image(
            image_stream, text, text_color, font_size_ratio, font_path
        )
        
        # Save to static directory
        os.makedirs("static", exist_ok=True)
        output_path = f"static/{image.filename}"
        with open(output_path, "wb") as f:
            f.write(output_stream.getbuffer())
        
        # Save text and image name mapping
        save_text_image_mapping(text, image.filename)
        
        return JSONResponse(content={
            "base64_image": base64_encoded,
            "static_url": f"/static/{image.filename}"
        })
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))