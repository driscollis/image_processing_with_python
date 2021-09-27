# wx_pillow_demo.py

import wx
from PIL import Image


class ImagePanel(wx.Panel):
    def __init__(self, parent, image_size):
        super().__init__(parent)

        pil_img = Image.open("pink_flower.jpg")
        width, height = pil_img.size
        bitmap = wx.BitmapFromBuffer(width, height, pil_img.tobytes())

        self.image_ctrl = wx.StaticBitmap(self, bitmap=wx.Bitmap(bitmap))

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.image_ctrl, 0, wx.ALL, 5)

        self.SetSizer(main_sizer)
        main_sizer.Fit(parent)
        self.Layout()


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="wxPython Image Viewer")
        panel = ImagePanel(self, image_size=(240, 240))
        self.Show()


if __name__ == "__main__":
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()