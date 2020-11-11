# exif_viewer.py

import os
import wx

from PIL import Image
from PIL.ExifTags import TAGS

wildcard = "JPEG (*.jpg)|*.jpg|" "All files (*.*)|*.*"


def get_exif_data(path: str) -> dict:
    """
    Extracts the EXIF information from the provided photo
    """
    exif_data = {}
    i = Image.open(path)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exif_data[decoded] = value

    return exif_data


def get_photo_size(path: str) -> str:
    photo_size = os.path.getsize(path)
    photo_size = photo_size / 1024.0
    if photo_size > 1000:
        # photo is larger than 1 MB
        photo_size = photo_size / 1024.0
        size = f"{photo_size:.2f} MB"
    else:
        size = f"{photo_size:.2f} KB"
    return size


class Photo:
    def __init__(self, photo: str) -> None:
        """Constructor"""
        self.exif_data = get_exif_data(photo)
        self.filename = os.path.basename(photo)
        self.filesize = get_photo_size(photo)


class MainPanel(wx.Panel):
    def __init__(self, parent: wx.Frame) -> None:
        """Constructor"""
        super().__init__(parent)

        # dict of Exif keys and static text labels
        self.photo_data = {
            "MaxApertureValue": "Aperture",
            "DateTime": "Creation Date",
            "ExifImageHeight": "Height",
            "ExifImageWidth": "Width",
            "ExposureTime": "Exposure",
            "FNumber": "F-Stop",
            "Flash": "Flash",
            "FocalLength": "Focal Length",
            "ISOSpeedRatings": "ISO",
            "Model": "Camera Model",
            "ShutterSpeedValue": "Shutter Speed",
        }

        self.exif_data = {}
        self.filename = ""
        self.filesize = ""

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        load_file_button = wx.Button(self, label="Load Image Metadata")
        load_file_button.Bind(wx.EVT_BUTTON, self.on_load_file)
        self.main_sizer.Add(load_file_button, 0, wx.ALL | wx.CENTER, 5)
        self.layout_widgets()
        self.SetSizer(self.main_sizer)

    def layout_widgets(self) -> None:
        ordered_widgets = [
            "Model",
            "ExifImageWidth",
            "ExifImageHeight",
            "DateTime",
            "static_line",
            "MaxApertureValue",
            "ExposureTime",
            "FNumber",
            "Flash",
            "FocalLength",
            "ISOSpeedRatings",
            "ShutterSpeedValue",
        ]

        self.build_row("Filename", "", "Filename")
        self.build_row("File Size", "", "FileSize")
        for key in ordered_widgets:
            if key != "static_line":
                self.build_row(self.photo_data[key], "", key)
            else:
                self.main_sizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND, 5)

    def build_row(self, label: str, value: str, txt_name: str) -> None:
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        lbl = wx.StaticText(self, label=label, size=(95, -1))
        txt = wx.TextCtrl(
            self, value=str(value), size=(150, -1), style=wx.TE_READONLY, name=txt_name
        )
        sizer.Add(lbl, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(txt, 0, wx.ALL, 5)
        self.main_sizer.Add(sizer)

    def on_load_file(self, event: wx.EVT_BUTTON) -> None:
        std_paths = wx.StandardPaths.Get()
        with wx.FileDialog(
            self,
            message="Choose a file",
            defaultDir=std_paths.GetDocumentsDir(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_CHANGE_DIR,
        ) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                photo = Photo(path)
                self.update_panel(photo)

    def update_panel(self, photo: Photo) -> None:
        self.exif_data = photo.exif_data

        children = self.GetChildren()
        for child in children:
            if isinstance(child, wx.TextCtrl):
                self.update(photo, child)

    def update(self, photo: Photo, txt_widget: wx.TextCtrl) -> None:
        key = txt_widget.GetName()

        if key in self.exif_data:
            value = self.exif_data[key]
        else:
            value = "No Data"

        if key == "Filename":
            txt_widget.SetValue(photo.filename)
        elif key == "FileSize":
            txt_widget.SetValue(photo.filesize)
        else:
            txt_widget.SetValue(str(value))


class PhotoInfo(wx.Frame):
    def __init__(self) -> None:
        super().__init__(None, title="Image Information")
        panel = MainPanel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App()
    frame = PhotoInfo()
    app.MainLoop()
