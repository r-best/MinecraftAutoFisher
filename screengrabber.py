import tkinter as tk


def mouseDown(e, c, rect):
    last_click_x = e.x_root
    last_click_y = e.y_root
    c.coords(rect, last_click_x, last_click_y, last_click_x, last_click_y)


def mouseUp(e, c, rect):
    print(e.x_root, e.y_root)


def mouseMove(e, c, rect):
    x1, y1, _, _, = c.coords(rect)
    c.coords(rect, x1, y1, e.x_root, e.y_root)


def quit(e, c, rect):
    x1, y1, x2, y2 = c.coords(rect)
    with open('out.txt', 'w') as fp:
        fp.write("{} {} {} {}".format(x1, y1, x2, y2))
    e.widget.destroy()


def main():
    # Set up Tkinter window
    root = tk.Tk()
    root.wait_visibility(root)
    root.attributes('-alpha', 0.1)
    root.attributes('-fullscreen', True)

    # Create Tkinter Canvas
    c = tk.Canvas(root)
    c.pack(fill='both', expand=True)
    rect = c.create_rectangle(0, 0, 0, 0, fill="blue")

    root.bind("<ButtonPress-1>", lambda e: mouseDown(e, c, rect))
    root.bind("<ButtonRelease-1>", lambda e: mouseUp(e, c, rect))
    root.bind("<B1-Motion>", lambda e: mouseMove(e, c, rect))
    root.bind("<Return>", lambda e: quit(e, c, rect))
    root.bind("<Escape>", lambda e: quit(e, c, rect))
    root.mainloop()
    

if __name__ == '__main__':
    main()
