from get_exif import get_lat_long, get_date
from print_exif_in_photo import print_exif_in_photo
import os

photos_path = os.listdir('./photos')

photos_data = []

for index, value in enumerate(photos_path):
    photo_path = f"./photos/{value}"
    data = [get_lat_long(photo_path), get_date(photo_path)]
    photos_data.append(data)
    print_exif_in_photo(photo_path, data)
    print(f"{index + 1}/{len(photos_path)}")