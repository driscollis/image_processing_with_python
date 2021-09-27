# tk_pillow_demo.py

from tkinter import Tk, Canvas, NW
from PIL import Image, ImageTk


def main():
    root = Tk()
    root.title("Tkinter Image Viewer")
    pil_img = Image.open("pink_flower.jpg")
    width, height = pil_img.size
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    img = ImageTk.PhotoImage(pil_img)
    canvas.create_image(20, 20, anchor=NW, image=img)
    root.mainloop()

if __name__ == "__main__":
    main()