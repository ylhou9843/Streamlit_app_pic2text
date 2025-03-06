import pytesseract
import platform

def set_tesseract_path():
    if platform.system() == 'Windows':
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\yhou\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    elif platform.system() == 'Linux':
        pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'