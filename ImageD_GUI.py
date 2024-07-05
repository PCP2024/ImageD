import sys
import traceback
import urllib.request
import os

import numpy as np
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QToolBar,
    QFileDialog,
    QMenu,
    QDialog,
    QVBoxLayout,
    QSlider,
    QDialogButtonBox,
    QLineEdit,
    QColorDialog,
)
from PyQt6.QtGui import QIcon, QAction, QPixmap
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QImage
from PIL import Image, ImageQt, ImageFont, ImageEnhance
from imaged.processing.ImageProcessing import (
    ImageProcessor,
    resize,
    reshape,
    rotate,
    addtext,
    remove_background,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.image = None
        self.image_processor = None

        # Initialize adjustment parameters
        self.brightness_param = 1.0
        self.contrast_param = 1.0
        self.color_param = 1.0
        self.sharpness_param = 1.0

        self.label = QLabel("Load an Image!")
        self.label.setMargin(10)
        self.setCentralWidget(self.label)

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
        file_menu.addAction(QAction("Save As...", self, triggered=self.save_image))

        edit_menu = menu.addMenu("Edit")
        self.add_edit_actions(edit_menu)

    def add_edit_actions(self, edit_menu):
        actions = [
            ("Brightness", self.edit_brightness),
            ("Contrast", self.edit_contrast),
            ("Color", self.edit_color),
            ("Sharpness", self.edit_sharpness),
            ("Resize", self.edit_resize),
            ("Rotate", self.edit_rotate),
            ("Add Text", self.edit_addtext),
            ("Remove Background", self.edit_remove_background),
        ]

        for name, method in actions:
            action = QAction(name, self)
            action.triggered.connect(self.wrap_in_try_except(method, name))
            edit_menu.addAction(action)

    def wrap_in_try_except(self, func, action_name):
        def wrapper():
            try:
                func()
            except Exception as e:
                print(f"Error in action '{action_name}': {e}")
                traceback.print_exc()

        return wrapper

    def button_clicked_load(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image File",
            "",
            "Image Files (*.png *.jpg *.bmp);; All Files (*)",
        )
        if file_name:
            self.image = Image.open(file_name)
            self.image_processor = ImageProcessor(self.image)
            self.show_image(self.image)

    def apply_adjustments(self, image):
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(self.brightness_param)

        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(self.contrast_param)

        enhancer = ImageEnhance.Color(image)
        image = enhancer.enhance(self.color_param)

        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(self.sharpness_param)

        return image

    def show_image(self, image):
        self.image = self.apply_adjustments(
            image
        )  # Apply adjustments before displaying
        self.image_processor.image = self.image  # Update the processor's image
        qt_image = ImageQt.ImageQt(self.image)
        pixmap = QPixmap.fromImage(qt_image)
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.adjustSize()

    def edit_brightness(self):
        if not self.image_processor:
            return
        param, ok = self.get_param("Brightness")
        if ok:
            self.brightness_param = param
            self.show_image(self.image)

    def edit_contrast(self):
        if not self.image_processor:
            return
        param, ok = self.get_param("Contrast")
        if ok:
            self.contrast_param = param
            self.show_image(self.image)

    def edit_color(self):
        if not self.image_processor:
            return
        param, ok = self.get_param("Color")
        if ok:
            self.color_param = param
            self.show_image(self.image)

    def edit_sharpness(self):
        if not self.image_processor:
            return
        param, ok = self.get_param("Sharpness")
        if ok:
            self.sharpness_param = param
            self.show_image(self.image)

    def edit_resize(self):
        if not self.image_processor:
            return
        new_size, ok = self.get_size()
        if ok:
            new_image = resize(self.image, new_size)
            self.image_processor.image = new_image
            self.show_image(new_image)

    def edit_rotate(self):
        if not self.image_processor:
            return
        angle, ok = self.get_param("Rotate", integer=True)
        if ok:
            try:
                new_image = rotate(self.image, angle)
                self.image_processor.image = new_image
                self.show_image(new_image)
            except Exception as e:
                print(f"Error rotating image: {e}")
                traceback.print_exc()

    def edit_addtext(self):
        if not self.image_processor:
            return
        text, ok = self.get_text("Enter text to add")
        if ok:
            font_size, ok = self.get_param("Font Size", integer=True)
            if ok:
                color = self.get_color()
                if color:
                    location, ok = self.get_location()
                    if ok:
                        # Specify the path to the font file
                        font_path = os.path.join(os.path.dirname(__file__), "arial.ttf")
                        try:
                            font = ImageFont.truetype(font_path, font_size)
                        except IOError:
                            print(f"Error: Could not load font at {font_path}")
                            return
                        new_image = addtext(self.image, text, font, color, location)
                        self.image_processor.image = new_image
                        self.show_image(new_image)

    def edit_remove_background(self):
        if not self.image_processor:
            return
        try:
            new_image = remove_background(self.image)
            self.show_image(new_image)
        except Exception as e:
            print(f"Error removing background: {e}")
            traceback.print_exc()

    def save_image(self):
        if not self.image_processor:
            return
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save Image File",
            "",
            "Image Files (*.png *.jpg *.bmp);; All Files (*)",
        )
        if file_name:
            self.image_processor.save_image(file_name)

    def get_param(self, title, integer=False):
        dialog = QDialog(self)
        dialog.setWindowTitle(title)
        layout = QVBoxLayout()
        slider = QSlider(Qt.Orientation.Horizontal)  # Corrected attribute access
        slider.setRange(0, 100)
        slider.setValue(50)
        layout.addWidget(slider)
        line_edit = QLineEdit()
        layout.addWidget(line_edit)
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)
        dialog.setLayout(layout)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            try:
                value = int(line_edit.text()) if integer else float(line_edit.text())
            except ValueError:
                value = slider.value() / 50 if not integer else slider.value() - 50
            return value, True
        return None, False

    def get_size(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Resize")
        layout = QVBoxLayout()
        width_edit = QLineEdit()
        width_edit.setPlaceholderText("Width")
        layout.addWidget(width_edit)
        height_edit = QLineEdit()
        height_edit.setPlaceholderText("Height")
        layout.addWidget(height_edit)
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)
        dialog.setLayout(layout)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            try:
                width = int(width_edit.text())
                height = int(height_edit.text())
                return (width, height), True
            except ValueError:
                pass
        return None, False

    def get_text(self, title):
        dialog = QDialog(self)
        dialog.setWindowTitle(title)
        layout = QVBoxLayout()
        line_edit = QLineEdit()
        layout.addWidget(line_edit)
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)
        dialog.setLayout(layout)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            return line_edit.text(), True
        return None, False

    def get_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            return color.getRgb()
        return None

    def get_location(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Location")
        layout = QVBoxLayout()
        x_edit = QLineEdit()
        x_edit.setPlaceholderText("X")
        layout.addWidget(x_edit)
        y_edit = QLineEdit()
        y_edit.setPlaceholderText("Y")
        layout.addWidget(y_edit)
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)
        dialog.setLayout(layout)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            try:
                x = int(x_edit.text())
                y = int(y_edit.text())
                return (x, y), True
            except ValueError:
                pass
        return None, False


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
