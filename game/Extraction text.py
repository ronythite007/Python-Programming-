from PIL import Image
from pytesseract import pytesseract

path_to_tesseract=r"C:\Users\Rohan\AppData\Local\Programs\Python\Python37\Lib\site-packages\pytesseract.exe"
image_path=r"C:\Users\Rohan\Downloads\text.jpg"
img=Image.open(image_path)

pytesseract.tesseract_cmd=path_to_tesseract

text=pytesseract.image_to_string(img)
print(text[:-1])