"""
Allows the user to select an area of the screen that the autofisher
will watch for subtitles. When the `grab()` method is called, it will
open a Tkinter window where the user can click and drag a rectangular
area whose coordinates will then be returned
"""
import os
import sys
import json
import tkinter as tk


def _mouseMove(c, rect, x, y):
    """Moves the lower right corner of a rectangle on
    a Tkinter Canvas to the given (x, y)-coordinates,
    effectively stretching the rectangle

    Arguments:
        c (Tkinter.Canvas)
            Any Tkinter Canvas object
        rect (int)
            The identifier of a rectangle on the canvas,
            returned by canvas.create_rectangle
        x (int)
            Destination x-coordinate
        y (int)
            Destination y-coordinate
    """
    x1, y1, _, _ = c.coords(rect)
    c.coords(rect, x1, y1, x, y)


def grab():
    """Opens a Tkinter window and allows the user to
    click and drag a rectangular selection, then returns
    the coordinates of the selection
    
    Returns:
        list:
            A list of 4 numbers (x1, y1, x2, y2), where
            (x1, y1) is the top left corner and (x2, y2)
            is the lower right corner
    """
    # If running on Windows, need to let it know this is a "DPI-aware program"
    # so that the bbox coordinates aren't scaled and messed up
    if os.name == 'nt':
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(ctypes.c_int(1))

    bbox = [0, 0, 0, 0]

    # Set up Tkinter window
    root = tk.Tk()
    root.wait_visibility(root)
    root.attributes('-alpha', 0.1)
    root.attributes('-fullscreen', True)

    # Create Tkinter Canvas and Rect object
    c = tk.Canvas(root)
    c.pack(fill='both', expand=True)
    rect = c.create_rectangle(0, 0, 0, 0, fill="blue")

    def end():
        nonlocal bbox
        bbox = c.coords(rect)
        root.destroy()

    # Set event bindings and start Tkinter main loop
    root.bind("<ButtonPress-1>", lambda e: c.coords(rect, e.x_root, e.y_root, e.x_root, e.y_root))
    root.bind("<B1-Motion>", lambda e: _mouseMove(c, rect, e.x_root, e.y_root))
    root.bind("<ButtonRelease-1>", lambda e: end())
    root.bind("<Escape>", lambda e: end())
    root.mainloop()

    return bbox
