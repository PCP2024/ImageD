import unittest
from PIL import Image
from imaged.processing.ImageProcessing import ImageProcessor
from pathlib import Path


class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.image_path = Path("imaged/demodata/test_image.jpeg")
        self.image = Image.open(self.image_path)
        self.processor = ImageProcessor(self.image)

    def tearDown(self):
        self.image.close()

    def test_brightness(self):
        param = 1.5
        result = self.processor.brightness(param)
        self.assertIsInstance(result, Image.Image)
        # Add assertions to check if the brightness is adjusted correctly

    def test_contrast(self):
        param = 0.8
        result = self.processor.contrast(param)
        self.assertIsInstance(result, Image.Image)
        # Add assertions to check if the contrast is adjusted correctly

    def test_color(self):
        param = 1.2
        result = self.processor.color(param)
        self.assertIsInstance(result, Image.Image)
        # Add assertions to check if the colors are adjusted correctly

    def test_sharpness(self):
        param = 1.3
        result = self.processor.sharpness(param)
        self.assertIsInstance(result, Image.Image)
        # Add assertions to check if the sharpness is adjusted correctly


if __name__ == "__main__":
    unittest.main()
