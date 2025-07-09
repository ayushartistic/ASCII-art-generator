import os
from PIL import Image, ImageOps
import numpy as np

# Force script to run from its own directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def image_to_ascii(image_path, width=100, height=60):
    try:
        img = ImageOps.exif_transpose(Image.open(image_path)).convert("L")
    except FileNotFoundError:
        print("❌ File not found. Please check the image path:", image_path)
        return ""
    except Exception as e:
        print("❌ Some error occurred:", e)
        return ""

    # Auto-invert the image for better CMD visibility
    img = ImageOps.invert(img)

     

    img = img.resize((width,height))
    img_array = np.array(img)

    ascii_art = ""
    for row in img_array:
        for pixel in row:
            if pixel < 64:
                ascii_art += "*"
            elif pixel < 128:
                ascii_art += "+"
            elif pixel < 192:
                ascii_art += "."
            else:
                ascii_art += " "
        ascii_art += "\n"

    return ascii_art


# 🎯 Take image filename input from user
file_name = input("📷 Enter the image filename (must be in this folder): ")

ascii_result = image_to_ascii(file_name)

if ascii_result:
    
    print("\n🔍 Preview:\n")
    print(ascii_result) 
