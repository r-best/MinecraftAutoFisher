"""
Author: Robert Best
Description: Tkinter GUI application that allows the user to select
a rectangular portion of their screen, which will be recorded
as coordinates in a text file. Default file is `out.txt` but
a different name can be passed in on the command line.
"""
import sys
import tkinter as tk

class Rect():
    """Class representing a rectangle on a Tkinter Canvas.
    More easily exposes the coordinates for viewing & shifting.
    """
    def __init__(self, canvas, x1, y1, x2, y2, **kwargs):
        self.canvas = canvas
        self.widget = canvas.create_rectangle(x1, y1, x2, y2, kwargs)
        self.move(x1, y1, x2, y2)

    def move(self, x1, y1, x2, y2):
        """Moves the Rect to the given coordinates

        Arguments:
            x1, y1: numbers
                The destination coordinates of the upper left corner of the Rect
            x2, y2: numbers
                The destination coordinates of the lower right corner of the Rect
        
        Returns:
            None
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas.coords(self.widget, x1, y1, x2, y2)

    def origin(self):
        """Returns the coordinates of the upper left corner of the Rect

        Returns:
            x1: number
                The x-coordinate of the upper left corner of the Rect
            y1: number
                The y-coordinate of the upper left corner of the Rect
        """
        return self.x1, self.y1

    def coords(self):
        """Returns the Rect coordinates

        Returns:
            x1, y1: numbers
                The coordinates of the upper left corner of the Rect
            x2, y2: numbers
                The coordinates of the lower right corner of the Rect
        """
        return self.x1, self.y1, self.x2, self.y2


def mouseDown(e, rect):
    """Event callback for Tkinter <ButtonPress-1>. Resets
    the position of the bounding box.

    Arguments:
        e: Tkinter Event
            The event that triggered this callback
        rect: Rect
            The bounding box in use
    """
    rect.move(e.x_root, e.y_root, e.x_root, e.y_root)


def mouseMove(e, rect):
    """Event callback for Tkinter <B1-Motion>. Shifts the
    coordinates of the bounding box to match the current mouse
    position.

    Arguments:
        e: Tkinter Event
            The event that triggered this callback
        rect: Rect
            The bounding box in use
    """
    x1, y1 = rect.origin()
    rect.move(x1, y1, e.x_root, e.y_root)


def quit(rect, outfile):
    """Writes the final coordinates of the bounding box
    to the given file and closes the program.

    Arguments:
        rect: Rect
            The bounding box in use
        outfile:
            Name of file to write results to
    """
    x1, y1, x2, y2 = rect.coords()
    with open(outfile, 'w') as fp:
        fp.write("{} {} {} {}".format(x1, y1, x2, y2))
    exit()


def main(argv):
    OUTPUT_FILE = 'out.txt'

    if len(argv) > 0:
        OUTPUT_FILE = argv[0]

    # Set up Tkinter window
    root = tk.Tk()
    root.wait_visibility(root)
    root.attributes('-alpha', 0.1)
    root.attributes('-fullscreen', True)

    # Create Tkinter Canvas and Rect object
    c = tk.Canvas(root)
    c.pack(fill='both', expand=True)
    rect = Rect(c, 0, 0, 0, 0, fill="blue")

    # Set event bindings and start Tkinter main loop
    root.bind("<ButtonPress-1>", lambda e: mouseDown(e, rect))
    root.bind("<B1-Motion>", lambda e: mouseMove(e, rect))
    root.bind("<ButtonRelease-1>", lambda e: quit(rect, OUTPUT_FILE))
    root.bind("<Return>", lambda e: quit(rect, OUTPUT_FILE))
    root.bind("<Escape>", lambda e: e.widget.destroy())
    root.mainloop()
    

if __name__ == '__main__':
    main(sys.argv[1:])
