import pyscreenshot as ig
import pytesseract as pt
from PIL import Image
import tkinter as tk
import time
import sys

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


def main(argv):
    IN_FILE = 'out.txt'
    if len(argv) > 0:
        IN_FILE = argv[0]
    
    with open(IN_FILE, 'r') as fp:
        x1, y1, x2, y2 = fp.read().split()
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

    while True:
        screen = ig.grab(bbox=(x1, y1, x2, y2))
        screen_text = pt.image_to_string(screen)
        print(screen_text)
        if 'Fishing Bobber splashes' in screen_text or 'Fishing Gobber splashes' in screen_text or 'Fickhina Bokhher splashes' in screen_text:
            print('nice!')
        else:
            print('no!')
        time.sleep(1)


if __name__ == '__main__':
    main(sys.argv[1:])
