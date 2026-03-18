from PIL import Image
import os
import argparse

__author__    = "Vicente González"
__version__   = "1.0"
__copyright__ = ("V. González", 2025)
__license__   = "gpl-3.0"
__examples__  = ["image.jpg -w 0.7 -b 0.3"]
__doc__       = """
* Convert images to scanner BW like pictures
"""

BANNER_FONT  = "tombstone"
BANNER_STYLE = {'fgcolor': "lolcat"}

def get_image_files():
    image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")
    files = os.listdir()
    image_files = [file for file in files if file.lower().endswith(image_extensions)]
    return sorted(image_files)

def convert_to_BW(file_name,white,black,counter):
    new_image="BW_"+file_name
    image = Image.open(file_name)
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            try:
                r, g, b = pixels[x, y]  # Attempt to retrieve the pixel's RGB values
            except Exception as e:
                print(f"Incompatible image: {file_name}")
                return None  # S
            brightness = 0.299 * r + 0.587 * g + 0.114 * b
            if brightness >= white*255:
                pixels[x, y] = (255, 255, 255)  # Set to white
            if brightness <= black*255:
                pixels[x, y] = (0, 0, 0)  # Set to black
    image.convert('L').save(new_image)
    if counter == 0:
        os.system(f"sxiv {file_name} & sxiv {new_image} ")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert images to black and white.")
    parser.add_argument("-w", "--white", default=0.7, help="above value convert to white")
    parser.add_argument("-b", "--black", default=0.3, help="below value convert to white")
    args = parser.parse_args()
    counter = 0
    for file in get_image_files():
        convert_to_BW(file,args.white,args.black,counter)
        counter = 1
