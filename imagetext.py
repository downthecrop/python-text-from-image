##Requires PIL (Pillow), and pytesseract

from PIL import Image
from pytesseract import image_to_string

img=Image.open('test.png')

print(image_to_string(img))