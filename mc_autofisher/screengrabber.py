"""
Author: Robert Best
Description: Tkinter application that allows the user to select
a rectangular portion of their screen using the `grab()` function,
which will be returned as a coordinate tuple. If run as a script,
the coordinates will be written to a JSON config file, default file
is `out.txt` but a different name can be passed in on the command line.
"""
import sys
import json
import tkinter as tk


def _mouseMove(c, rect, x, y):
    """Moves the lower right corner of a rectangle on
    a Tkinter Canvas to the given (x, y)-coordinates,
    effectively stretching the rectangle

    Arguments:
        c: Tkinter Canvas
            Any Tkinter Canvas object
        rect: int
            The identifier of a rectangle on the canvas,
            returned by canvas.create_rectangle
        x: int
            Destination x-coordinate
        y: int
            Destination y-coordinate
    """
    x1, y1, _, _ = c.coords(rect)
    c.coords(rect, x1, y1, x, y)


def grab():
    """Opens a Tkinter window and allows the user to
    click and drag a rectangular selection, then returns
    the coordinates of the selection
    """
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
