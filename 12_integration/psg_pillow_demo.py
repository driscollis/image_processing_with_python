# psg_pilloww_demo.py

import PySimpleGUI as sg
from PIL import Image, ImageTk

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]


def main():
    elements = [
        [sg.Image(key="image")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), enable_events=True, key="file"),
            sg.FileBrowse(file_types=file_types),
        ],
    ]

    window = sg.Window("Image Viewer", elements)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "file":
            image = Image.open(values["file"])
            image.thumbnail((400, 400))
            photo_img = ImageTk.PhotoImage(image)
            window["image"].update(data=photo_img)

    window.close()


if __name__ == "__main__":
    main()