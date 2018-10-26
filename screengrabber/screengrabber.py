"""
Author: Robert Best
Description: Tkinter GUI application that allows the user to select
a rectangular portion of their screen, which will be recorded
as coordinates in a text file. Default file is `out.txt` but
a different name can be passed in on the command line.
"""
import sys
import json
import tkinter as tk


def _mouseMove(c, rect, x, y):
    """Event callback for Tkinter <B1-Motion>. Shifts the
    coordinates of the bounding box to match the current mouse
    position.

    Arguments:
        e: Tkinter Event
            The event that triggered this callback
        rect: Rect
            The bounding box in use
    """
    x1, y1, _, _ = c.coords(rect)
    c.coords(rect, x1, y1, x, y)


def start():
    # Set up Tkinter window
    root = tk.Tk()
    root.wait_visibility(root)
    root.attributes('-alpha', 0.1)
    root.attributes('-fullscreen', True)

    # Create Tkinter Canvas and Rect object
    c = tk.Canvas(root)
    c.pack(fill='both', expand=True)
    rect = c.create_rectangle(0, 0, 0, 0, fill="blue")

    # Set event bindings and start Tkinter main loop
    root.bind("<ButtonPress-1>", lambda e: c.coords(rect, e.x_root, e.y_root, e.x_root, e.y_root))
    root.bind("<B1-Motion>", lambda e: _mouseMove(c, rect, e.x_root, e.y_root))
    root.bind("<ButtonRelease-1>", lambda e: e.widget.quit())
    root.bind("<Escape>", lambda e: e.widget.quit())
    root.mainloop()

    return c.coords(rect)
