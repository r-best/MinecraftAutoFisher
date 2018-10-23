"""

"""
import sys
import tkinter as tk

class Rect(tk.Widget):
    def __init__(self, canvas, x1, y1, x2, y2, **kwargs):
        self.canvas = canvas
        self.widget = canvas.create_rectangle(x1, y1, x2, y2, kwargs)
        self.move(x1, y1, x2, y2)

    def move(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas.coords(self.widget, x1, y1, x2, y2)

    def origin(self):
        return self.x1, self.y1

    def coords(self):
        return self.x1, self.y1, self.x2, self.y2


def mouseDown(e, rect):
    rect.move(e.x_root, e.y_root, e.x_root, e.y_root)


def mouseUp(e, rect):
    # print(e.x_root, e.y_root)
    pass


def mouseMove(e, rect):
    x1, y1 = rect.origin()
    rect.move(x1, y1, e.x_root, e.y_root)


def quit(e, rect, outfile):
    x1, y1, x2, y2 = rect.coords()
    with open(outfile, 'w') as fp:
        fp.write("{} {} {} {}".format(x1, y1, x2, y2))
    e.widget.destroy()


def main(argv):
    OUTPUT_FILE = 'out.txt'

    if len(argv) > 0:
        OUTPUT_FILE = argv[0]

    # Set up Tkinter window
    root = tk.Tk()
    root.wait_visibility(root)
    root.attributes('-alpha', 0.1)
    root.attributes('-fullscreen', True)

    # Create Tkinter Canvas
    c = tk.Canvas(root)
    c.pack(fill='both', expand=True)
    rect = Rect(c, 0, 0, 0, 0, fill="blue")

    root.bind("<ButtonPress-1>", lambda e: mouseDown(e, rect))
    root.bind("<ButtonRelease-1>", lambda e: mouseUp(e, rect))
    root.bind("<B1-Motion>", lambda e: mouseMove(e, rect))
    root.bind("<Return>", lambda e: quit(e, rect, OUTPUT_FILE))
    root.bind("<Escape>", lambda e: quit(e, rect, OUTPUT_FILE))
    root.mainloop()
    

if __name__ == '__main__':
    main(sys.argv[1:])
