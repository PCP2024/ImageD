import unittest
from PIL import Image
from imaged.processing.ImageProcessing import ImageProcessor
from imaged.processing.ImageProcessing import remove_background
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

    def test_remove_background(self):
        # Load test image
        image_path = "imaged/demodata/nerve-cell.png"
        image = Image.open(image_path)

        # Call remove_background function
        result = remove_background(image)

        # Assert that the result is an instance of Image.Image
        self.assertIsInstance(result, Image.Image)
        # Add additional assertions to check if the background is removed correctly
        desired_result_path = "imaged/demodata/nerve-cell-no-bg.png"
        desired_result = Image.open(desired_result_path)
        self.assertEqual(result.size, desired_result.size)
        self.assertEqual(result.mode, desired_result.mode)


if __name__ == "__main__":
    unittest.main()
