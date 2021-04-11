# exif_viewer.py

import PySimpleGUI as sg

from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS

file_types = [
        ("(JPEG (*.jpg)", "*.jpg"),
        ("All files (*.*)", "*.*"),
        ]

fields = {
        "File name": "File name",
        "File size": "File size",
        "Model": "Camera Model",
        "ExifImageWidth": "Width",
        "ExifImageHeight": "Height",
        "DateTime": "Creation Date",
        "static_line": "*",
        "MaxApertureValue": "Aperture",
        "ExposureTime": "Exposure",
        "FNumber": "F-Stop",
        "Flash": "Flash",
        "FocalLength": "Focal Length",
        "ISOSpeedRatings": "ISO",
        "ShutterSpeedValue": "Shutter Speed",
        }


def get_exif_data(path):
    """
    Extracts the EXIF information from the provided photo
    """
    exif_data = {}
    try:
        image = Image.open(path)
        info = image._getexif()
    except OSError:
        info = {}

    if info is None:
        info = {}

    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exif_data[decoded] = value

    return exif_data


def main():
    layout = [[
            sg.FileBrowse(
                "Load image data", file_types=file_types, key="-LOAD-",
                enable_events=True,
                )
            ]]
    for field in fields:
        layout += [[
                sg.Text(fields[field], size=(10, 1)),
                sg.Text("", size=(25, 1), key=field),
                ]]
    window = sg.Window("Image information", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-LOAD-":
            image_path = Path(values["-LOAD-"])
            exif_data = get_exif_data(image_path.absolute())
            for field in fields:
                if field == "File name":
                    window[field].update(image_path.name)
                elif field == "File size":
                    window[field].update(image_path.stat().st_size)
                else:
                    window[field].update(exif_data.get(field, "No data"))


if __name__ == "__main__":
    main()