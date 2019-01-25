"""
Automates Minecraft fishing by watching a portion of the screen for the subtitle
text "Fishing Bobber splashes", and double clicking the right mouse button when it
is found, allowing it to reel in and recast the line every time a fish appears.
"""

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
        screenText (str)
            The text to search for a match in
        targetText (`string`, optional)
            The text to search for, defaults to "Fishing Bobber"
        threshold: (`int`, optional)
            The maximum acceptable Levenshtein distance to
            be considered a match, defaults to 5
    
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

def start(bbox, allowed_error=5, tesspath=""):
    """Takes in bounding box coordinates and begins watching
    that section of the screen for the text "Fishing Bobber splashes",
    double clicking the right mouse button when it sees it to reel in
    the fish and recast the line. Press enter to quit.

    Arguments:
        bbox (list)
            A list of 4 numbers (x1, y1, x2, y2) obtained from the screengrabber
            program, where (x1, y1) is the top left corner of the bounding box
            and (x2, y2) is the lower right corner
        allowed_error (`int`, optional)
            The margin of error (measured in Levenshtein distance) allowed for
            text matching, i.e. 'Fishing Gobber splashes' has an error of 1
        tesspath (`str`, optional)
            The path to your Tesseract installation, leave blank to use default
    """
    if tesspath != "":
        pt.pytesseract.tesseract_path = tesspath

    mouse = Controller()
    listener = Listener(on_press=_keyDown)
    listener.start()

    timeout = 45 # Fish always appears within 45 seconds, if we wait longer than this then recast the line
    cast_time = time.monotonic()
    while listener.is_alive():
        # Grab portion of screen defined in config file & send it to tesseract
        screen = ig.grab(bbox=bbox)
        screen_text = pt.image_to_string(screen)
        if match(screen_text, threshold=allowed_error) or time.monotonic() - cast_time > timeout:
            # Either fish was found or timeout was exceeded, reel in the line and cast it again
            mouse.click(Button.right, 2)
            cast_time = time.monotonic()
        time.sleep(0.25)

    listener.join()
