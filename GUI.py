import pytesseract
from PIL import Image


img = Image.open('C:/Users/Jonathan/Desktop/1.png')
s = pytesseract.image_to_string(img)
print(s)
