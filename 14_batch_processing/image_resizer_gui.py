# image_resizer_gui.py

import controller
import PySimpleGUI as sg


def create_row(label, key):
    return [
        sg.Text(label),
        sg.Input(size=(25, 1), key=key, readonly=True),
        sg.FolderBrowse(),
    ]


def resize(values):
    input_folder = values["-INPUT_FOLDER-"]
    output_folder = values["-OUTPUT_FOLDER-"]
    width = values['-WIDTH-'] if values['-WIDTH-'] else None
    height = values['-HEIGHT-'] if values['-HEIGHT-'] else None

    verified = verify(input_folder, output_folder, width, height)
    if not verified:
        return
    if width is not None:
        width = int(width)
    if height is not None:
        height = int(height)

    image_paths = controller.get_image_paths(
        input_folder,
        values["-RECURSIVE-"],
        values["-FORMAT-"])
    if len(image_paths) < 1:
        sg.popup("No images found")
        return
    controller.resize_images(image_paths, width, height,
                             output_folder)


def verify(input_folder, output_folder, width, height):
    if not width and not height:
        sg.popup("Width or height has to be set")
        return False
    if not input_folder:
        sg.popup("Input folder not set")
        return False
    if not output_folder:
        sg.popup("Output folder not set")
        return False
    if input_folder == output_folder:
        sg.popup("input folder cannot be the same as output")
        return False
    return True


def main():
    layout = [
        create_row("Input Image Folder:", "-INPUT_FOLDER-"),
        [sg.Checkbox("Recursive Search", key="-RECURSIVE-",
                     enable_events=True),
         sg.Text("Format:"),
         sg.Combo(values=["jpg, png"], default_value="png",
                  readonly=True, key="-FORMAT-", enable_events=True)],
        create_row("Output Image Folder", "-OUTPUT_FOLDER-"),
        [
            sg.Text("Width"),
            sg.Input(key="-WIDTH-", enable_events=True, size=(10, 5)),
            sg.Text("Height"),
            sg.Input(key="-HEIGHT-", enable_events=True, size=(10, 5))
        ],
        [sg.Output()],
        [sg.Button("Resize")],
    ]

    window = sg.Window("Image Resizer", layout, size=(450, 250))

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-WIDTH-" and values["-WIDTH-"]:
            if not values["-WIDTH-"][-1].isdigit():
                window["-WIDTH-"].update(values["-WIDTH-"][:-1])
        elif event == "-HEIGHT-" and values["-HEIGHT-"]:
            if not values["-HEIGHT-"][-1].isdigit():
                window["-HEIGHT-"].update(values["-HEIGHT-"][:-1])
        elif event == "Resize":
            resize(values)

    window.close()


if __name__ == "__main__":
    main()