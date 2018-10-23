import pyscreenshot as ig
import pytesseract as pt
import time
import sys
import pyautogui
from pynput import keyboard

def mouseDown(e):
    print('Exiting')
    return False


def main(argv):
    WIDTH, HEIGHT = pyautogui.size()

    IN_FILE = 'out.txt'
    if len(argv) > 0:
        IN_FILE = argv[0]
    
    with open(IN_FILE, 'r') as fp:
        x1, y1, x2, y2 = fp.read().split()
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

    listener = keyboard.Listener(on_press=mouseDown)
    listener.start()

    timeout = 45 # Fish always appears within 45 seconds, if we wait longer than this then recast the line
    cast_time = time.monotonic()
    while listener.is_alive():
        screen = ig.grab(bbox=(x1, y1, x2, y2))
        screen_text = pt.image_to_string(screen)
        print(screen_text)
        if 'Fishing Bobber splashes' in screen_text or 'Fishing Gobber splashes' in screen_text or 'Fickhina Bokhher splashes' in screen_text:
            # Fish detected, clicking to reel it in & resetting timer
            pyautogui.click(WIDTH/2, HEIGHT/2)
            timeout = 45
        if time.monotonic() - cast_time > timeout:
            # Timer has expired, must have missed the fish
            pyautogui.click(WIDTH/2, HEIGHT/2)
            time.sleep(0.25)
            pyautogui.click(WIDTH/2, HEIGHT/2)
            timeout = 45

        time.sleep(1)
        timeout -= 1

    listener.join()


if __name__ == '__main__':
    main(sys.argv[1:])
