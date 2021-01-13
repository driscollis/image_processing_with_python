# image_filter_gui.py

import os
import shutil
import wx

from blur_image import blur
from contour_image import contour
from detail_image import detail
from edge_enhance_image import edge_enhance
from emboss_image import emboss
from find_edges_image import find_edges


class ImageConverterPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.max_size = 460
        self.original_image = ""
        self.current_image = ""
        self.image = None
        self.std_paths = wx.StandardPaths.Get()
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.create_widgets()

        self.SetSizer(self.main_sizer)
        self.main_sizer.Fit(parent)
        self.Layout()

    def create_widgets(self):
        img = wx.Image(self.max_size, self.max_size)
        self.image_ctrl = wx.StaticBitmap(self, bitmap=wx.Bitmap(img))
        self.main_sizer.Add(self.image_ctrl, 0, wx.ALL, 5)

        browse_btn = wx.Button(self, label="Browse")
        browse_btn.Bind(wx.EVT_BUTTON, self.on_browse)
        self.photo_txt = wx.TextCtrl(self, size=(200, -1))
        self.add_row_of_widgets([browse_btn, self.photo_txt])

        effects_label = wx.StaticText(self, label="Effects")
        selections = [
            "Blur",
            "Contour",
            "Detail",
            "Edge Enhance",
            "Emboss",
            "Find Edges",
            "Normal",
        ]
        self.effects_combo = wx.ComboBox(self, choices=selections, value=selections[-1])
        self.effects_combo.Bind(wx.EVT_COMBOBOX, self.on_effect)
        self.add_row_of_widgets([effects_label, self.effects_combo])

        save_btn = wx.Button(self, label="Save")
        save_btn.Bind(wx.EVT_BUTTON, self.on_save)
        self.main_sizer.Add(save_btn, 0, wx.ALL | wx.CENTER, 5)

    def add_row_of_widgets(self, widgets):
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        for widget in widgets:
            hsizer.Add(widget, 0, wx.ALL, 5)
        self.main_sizer.Add(hsizer, 0, wx.ALL, 5)

    def on_browse(self, event):
        """
        Browse for an image file
        @param event: The event object
        """
        wildcard = "JPEG files (*.jpg)|*.jpg"
        with wx.FileDialog(
            None, "Choose a file", wildcard=wildcard, style=wx.FD_OPEN
        ) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.original_image = dialog.GetPath()
                self.current_image = self.original_image
                self.photo_txt.SetValue(self.original_image)
                self.load_image()

    def on_effect(self, event):
        """
        Apply the specified effect to the image
        """
        if not self.current_image:
            return

        tmp = os.path.join(self.std_paths.GetTempDir(), "temp.jpg")
        effects = {
            "Blur": blur,
            "Contour": contour,
            "Detail": detail,
            "Edge Enhance": edge_enhance,
            "Emboss": emboss,
            "Find Edges": find_edges,
        }
        effect = self.effects_combo.GetValue()
        if effect in effects:
            effects[effect](self.original_image, tmp)
            self.current_image = tmp
            self.load_image()
        else:
            self.current_image = self.original_image
            self.load_image()

    def on_save(self, event):
        """
        Save the image
        """
        if not self.current_image:
            # current image is empty
            return
        if not self.original_image:
            # no image loaded
            return
        if self.effects_combo.GetValue() == "Normal":
            # nothing to save
            return

        wildcard = "JPEG files (*.jpg)|*.jpg"
        with wx.FileDialog(
            None, "Choose a file", wildcard=wildcard, style=wx.FD_SAVE
        ) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                save_path = dialog.GetPath()
                if save_path == self.original_image:
                    self.show_error_message()
                else:
                    # Copy the temporary image to the
                    # save location
                    shutil.copy(self.current_image, save_path)

    def load_image(self):
        """
        Load the image and display it to the user
        """
        img = wx.Image(self.current_image, wx.BITMAP_TYPE_ANY)

        # scale the image, preserving the aspect ratio
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            new_w = self.max_size
            new_h = int(self.max_size * H / W)
        else:
            new_h = self.max_size
            new_w = int(self.max_size * W / H)
        img = img.Scale(new_w, new_h)

        self.image_ctrl.SetBitmap(wx.Bitmap(img))
        self.Refresh()

    def show_error_message(self):
        with wx.MessageDialog(
            None,
            message="Overwriting original image is not allowed!",
            caption="Error",
            style=wx.ICON_ERROR,
        ) as dlg:
            dlg.ShowModal()


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Image Filter App")
        panel = ImageConverterPanel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()
