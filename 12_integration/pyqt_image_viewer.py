# pyqt_image_viewer.py

import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QApplication


class ImageViewer(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("PyQt Image Viewer")

        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap('./pink_flower.jpg'))

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.image_label)
        self.setLayout(self.main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    app.exec_()