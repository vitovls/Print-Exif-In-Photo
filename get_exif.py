from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS



def get_exif_data(photo_path):
    image = Image.open(photo_path)
    exif = image._getexif()
    for _, value in exif.items():
        return value


def convert_to_degress(value, reference):
    degrees = int(value[0])
    min = int(value[1])
    sec = float(value[2])
    return f"{degrees}° {min}' {sec:.2f}'' {reference}"


def get_lat_long(photo_path):
    exif = get_exif_data(photo_path)
    lat = convert_to_degress(exif[2], exif[1])
    long = convert_to_degress(exif[4], exif[3])
    return f"{lat} {long}"

def get_date(photo_path):
    image = Image.open(photo_path)
    exif = image._getexif()[306]
    date = datetime.strptime(exif, '%Y:%m:%d %H:%M:%S')
    return date.strftime('%d-%m-%Y - %H:%M:%S')
