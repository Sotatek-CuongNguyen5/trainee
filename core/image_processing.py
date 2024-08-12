from PIL import Image, ImageDraw, ImageFont
import io
import base64
import csv

def insert_text_on_image(image_stream, text, text_color="black", font_size_ratio=0.1):
    img = Image.open(image_stream)
    draw = ImageDraw.Draw(img)
    font_size = int(min(img.width, img.height) * font_size_ratio)
    font = ImageFont.load_default()  # Use the default font
    font = font.font_variant(size=font_size)  # Set the font size

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (img.width - text_width) / 2
    y = (img.height - text_height) / 2
    draw.text((x, y), text, font=font, fill=text_color)

    output_stream = io.BytesIO()
    img.save(output_stream, format=img.format)
    output_stream.seek(0)

    base64_encoded = base64.b64encode(output_stream.getvalue()).decode("utf-8")
    return output_stream, base64_encoded

def insert_text_on_image_ver2(image_stream, text1, text2, text1_color="green", text2_color="red", font_size_ratio=0.1):
    img = Image.open(image_stream)
    draw = ImageDraw.Draw(img)
    font_size = int(min(img.width, img.height) * font_size_ratio)
    font = ImageFont.load_default()  # Use the default font
    font = font.font_variant(size=font_size)  # Set the font size

    # Insert text1 at the top left
    bbox1 = draw.textbbox((0, 0), text1, font=font)
    text1_width = bbox1[2] - bbox1[0]
    text1_height = bbox1[3] - bbox1[1]
    x1 = 0
    y1 = 0
    draw.text((x1, y1), text1, font=font, fill=text1_color)

    # Insert text2 at the top right
    bbox2 = draw.textbbox((0, 0), text2, font=font)
    text2_width = bbox2[2] - bbox2[0]
    text2_height = bbox2[3] - bbox2[1]
    x2 = img.width - text2_width
    y2 = 0
    draw.text((x2, y2), text2, font=font, fill=text2_color)

    output_stream = io.BytesIO()
    img.save(output_stream, format=img.format)
    output_stream.seek(0)

    base64_encoded = base64.b64encode(output_stream.getvalue()).decode("utf-8")
    return output_stream, base64_encoded

def save_text_image_mapping(text, image_name):
    with open("text_image_mapping.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([text, image_name])