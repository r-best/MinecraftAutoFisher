import pyscreenshot as ig
import pytesseract as pt
from PIL import Image
import tkinter as tk
import time

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

while True:
    screen = ig.grab(bbox=(screen_width/2, screen_height/2, screen_width, screen_height))
    screen_text = pt.image_to_string(screen, config='--psm 7')
    if 'hello' in screen_text:
        print('nice!')
    else:
        print('no!')
    time.sleep(1)
