import sys
import subprocess
import urllib.request

import numpy as np
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QToolBar,
    QFileDialog,
)
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap

import imaged
import imaged.dataio


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello, World!")
        label.setMargin(10)
        self.setCentralWidget(label)

        # file_menu.addAction("Exit")

        # button = QPushButton("Press Me!")
        # button.clicked.connect(self.button_clicked)
        # self.setCentralWidget(button)

        # Set up a toolbar
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(50, 50))
        self.addToolBar(toolbar)

        button_action_load = QAction(QIcon("dragon.png"), "Open...", self)
        button_action_load.triggered.connect(self.button_clicked_load)
        toolbar.addAction(button_action_load)

        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        file_menu.addAction(button_action_load)
        # file_menu.addAction("Save...")

    # def button_clicked_emoji(self):
    #     label = QLabel(self)
    #     pixmap = QPixmap("fire.png")
    #     label.setPixmap(pixmap)
    #     self.setCentralWidget(label)
    #     self.resize(pixmap.width(), pixmap.height())
    #     print("Emoji clicked")

    def button_clicked_load(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            "",
            "Image Files (*.png *.jpg *.bmp);; All Files (*)",
        )
        if file_name:
            # subprocess.run(["python", "path/to/ImageD_cmd.py", file_name])
            # print("asdfsadfsadfadsfds")
            imload_instance = imaged.dataio.ImageLoader(file_name)
            image = imload_instance.load_image()
            imload_instance.show_image(image)

    # def button_clicked(self):
    #     print("Button clicked")


def main():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
