from PIL import Image
from pathlib import Path
import os

def png_jpg_jpeg__to_webp(file):
    if "webps" not in os.listdir("."):
        os.mkdir("webps")
    
    webp_name = Path(file).stem + ".webp"
    image = Image.open(file)
    image.save("webps\\" + webp_name, format="webp")
    
    return webp_name


if __name__ == "__main__":
    files = os.listdir("png_jpg_jpeg")
    for file in files:
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
            converted_file_name = png_jpg_jpeg__to_webp("png_jpg_jpeg\\" + file)
            print(converted_file_name)

