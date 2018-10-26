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


def main(argv):
    CONFIG_FILE = "config.json"
    if len(argv) > 0:
        CONFIG_FILE = argv[0]

    coords = grab()
    with open(CONFIG_FILE, 'r+') as fp:
        try:
            data = json.load(fp)
        except json.decoder.JSONDecodeError:
            data = dict()
    with open(CONFIG_FILE, 'w') as fp:
        data['screengrab_coords'] = coords
        json.dump(data, fp, indent=4, sort_keys=True)
        fp.truncate()


if __name__ == '__main__':
    main(sys.argv[1:])
