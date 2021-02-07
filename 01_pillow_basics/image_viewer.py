# image_viewer.py

import PySimpleGUI as sg
from PIL import Image, ImageTk

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]


def main():
    elements = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), enable_events=True, key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
        ],
    ]

    window = sg.Window("Image Viewer", elements)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-FILE-":
            image = Image.open(values["-FILE-"])
            image.thumbnail((400, 400))
            photo_img = ImageTk.PhotoImage(image)
            window["-IMAGE-"].update(data=photo_img)

    window.close()


if __name__ == "__main__":
    main()
