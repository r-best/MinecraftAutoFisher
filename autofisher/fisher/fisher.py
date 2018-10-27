import sys
import time
import json
import pyscreenshot as ig
import pytesseract as pt
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
from Levenshtein._levenshtein import distance as levenshtein


def _keyDown(e):
    """Callback for keyboard listener, closes
    the listener if the Enter key is pressed
    """
    if e == Key.enter:
        print('Exiting')
        return False
    return True


def match(screenText, targetText="Fishing Bobber", threshold=5):
    """Takes in some text and iterates through it line by line,
    checking to see if any of the lines contain something similar
    to the target text using Levenshtein distance

    Arguments:
        screenText: string
            The text to search for a match in
        targetText: string="Fishing Bobber"
            The text to search for
        threshold: int=5
            The maximum acceptable Levenshtein distance to
            be considered a match
    
    Returns:
        True if a match was found, False otherwise
    
    Examples:
        >>> match("Fishing Bobber")
        True
        >>> match("Fishing Gobber")
        True
        >>> match("Fishing")
        False 
        >>> match("Some text Fishing Bobber some more text")
        True
    """
    ngram_size = len(targetText.split())
    for line in screenText.splitlines():
        line = line.split()
        for i in range(len(line)-ngram_size+1):
            ngram = " ".join(line[i:i+ngram_size])
            if levenshtein(ngram, targetText) <= threshold:
                return True
    return False


def main(argv):
    CONFIG_FILE = "config.json"
    if len(argv) > 0:
        CONFIG_FILE = argv[0]

    with open(CONFIG_FILE, 'r') as fp:
        data = json.load(fp)
        pt.pytesseract.tesseract_path = data['tesseract_path']
        x1, y1, x2, y2 = data['screengrab_coords']

    mouse = Controller()
    listener = Listener(on_press=_keyDown)
    listener.start()

    timeout = 45 # Fish always appears within 45 seconds, if we wait longer than this then recast the line
    cast_time = time.monotonic()
    while listener.is_alive():
        # Grab portion of screen defined in config file & send it to tesseract
        screen = ig.grab(bbox=(x1, y1, x2, y2))
        screen_text = pt.image_to_string(screen)
        print(screen_text)
        if match(screen_text, 'Fishing Bobber') or time.monotonic() - cast_time > timeout:
            # Either fish was found or timeout was exceeded, reel in the line and cast it again
            mouse.click(Button.right, 2)
            cast_time = time.monotonic()
        time.sleep(0.25)

    listener.join()


if __name__ == '__main__':
    main(sys.argv[1:])
