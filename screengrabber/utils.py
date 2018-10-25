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
