# pyqt_pillow_demo.py

import sys

from PIL import Image, ImageQt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtWidgets import QVBoxLayout, QApplication


class ImageViewer(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("PyQt Image Viewer")

        # Open up image in Pillow
        image = Image.open("pink_flower.jpg")
        pil_qt_img = ImageQt.ImageQt(image)
        pixmap = QPixmap.fromImage(QImage(pil_qt_img))

        self.image_label = QLabel('')
        self.image_label.setPixmap(pixmap)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.image_label)
        self.setLayout(self.main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    app.exec_()