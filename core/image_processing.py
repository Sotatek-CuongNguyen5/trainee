from PIL import Image, ImageDraw, ImageFont
import io
import base64
import csv

def insert_text_on_image(image_stream, text, text_color="black", font_size_ratio=0.1, font_path=None):
    img = Image.open(image_stream)
    draw = ImageDraw.Draw(img)
    # Calculate font size based on image dimensions
    font_size = int(min(img.width, img.height) * font_size_ratio)
    # Use the specified font or default if not provided
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default(size=font_size)
    
    # Use textbbox to get the bounding box of the text
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (img.width - text_width) / 2
    y = (img.height - text_height) / 2
    draw.text((x, y), text, font=font, fill=text_color)
    
    output_stream = io.BytesIO()
    img.save(output_stream, format=img.format)
    output_stream.seek(0)
    
    base64_encoded = base64.b64encode(output_stream.getvalue()).decode('utf-8')
    return output_stream, base64_encoded

def save_text_image_mapping(text, image_name):
    with open('text_image_mapping.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([text, image_name])