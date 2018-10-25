import pyscreenshot as ig
import pytesseract as pt
import time
import sys
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller


def keyDown(e):
    if e == Key.esc:
        print('Exiting')
        return False
    return True


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

    mouse = Controller()
    listener = Listener(on_press=keyDown)
    listener.start()

    timeout = 45 # Fish always appears within 45 seconds, if we wait longer than this then recast the line
    cast_time = time.monotonic()
    while listener.is_alive():
        screen = ig.grab(bbox=(x1, y1, x2, y2))
        screen_text = pt.image_to_string(screen)
        print(screen_text)
        if 'Fishing Bobber' in screen_text or 'Fishing Gobber' in screen_text or time.monotonic() - cast_time > timeout:
            # Timer has expired, must have missed the fish
            mouse.click(Button.right)
            time.sleep(0.25)
            mouse.click(Button.right)
            cast_time = time.monotonic()

        time.sleep(0.25)

    listener.join()


if __name__ == '__main__':
    main(sys.argv[1:])
