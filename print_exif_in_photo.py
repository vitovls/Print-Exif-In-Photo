from PIL import ImageDraw, Image, ImageFont

def print_exif_in_photo(photo_path, data):
    photo_name = photo_path.split('/')[-1]
    image = Image.open(photo_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('./fonts/Roboto-Regular.ttf', 120)
    draw.text((10, 30), f"{data[0]}", font=font, fill=(0, 0, 0))
    draw.text((10, 150), f"{data[1]}", font=font, fill=(0, 0, 0))
    image.save(f"./photos_with_data/{photo_name}")