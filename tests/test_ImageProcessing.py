import unittest
from PIL import Image, ImageEnhance
from processing.ImageProcessing import difference, substract, ImageProcessor


class TestImageProcessing(unittest.TestCase):
    def test_difference(self):
        # Create two sample images
        im1 = Image.new("RGB", (100, 100), color="red")
        im2 = Image.new("RGB", (100, 100), color="blue")

        # Calculate the absolute difference
        result = difference(im1, im2)

        # Assert that the result is an instance of the Image class
        self.assertIsInstance(result, Image.Image)

        # Assert that the result image has the same size as the input images
        self.assertEqual(result.size, im1.size)

        # Assert that the result image is not equal to either of the input images
        self.assertNotEqual(result, im1)
        self.assertNotEqual(result, im2)

        # Assert that the result image has the expected pixel values
        expected_pixels = [(255, 0, 255)] * 100 * 100  # All magenta pixels
        self.assertEqual(list(result.getdata()), expected_pixels)

    def test_substract(self):
        # Create two test images
        im1 = Image.new("RGB", (100, 100), color="red")
        im2 = Image.new("RGB", (100, 100), color="blue")

        # Call the substract function
        result = substract(im1, im2)

        # Assert that the result is an instance of the Image class
        self.assertIsInstance(result, Image.Image)

        # Assert that the result image has the same size as the input images
        self.assertEqual(result.size, im1.size)

        # Assert that the result image has the expected pixel values
        expected_pixels = [(255, 0, 0)] * 100 * 100  # All red pixels
        self.assertEqual(list(result.getdata()), expected_pixels)


class ImageProcessorTest(unittest.TestCase):
    def test_brightness(self):
        # Create a test image
        im = Image.new("RGB", (100, 100), color="red")

        # Create an ImageProcessor object
        processor = ImageProcessor(im)

        # Call the brightness method
        result = processor.brightness(1.5)

        # Assert that the result is an instance of the Image class
        self.assertIsInstance(result, Image.Image)

        # Assert that the result image has the same size as the input image
        self.assertEqual(result.size, im.size)

    def test_contrast(self):
        # Create a test image
        im = Image.new("RGB", (100, 100), color="red")

        # Create an ImageProcessor object
        processor = ImageProcessor(im)

        # Call the contrast method
        result = processor.contrast(1.5)

        # Assert that the result is an instance of the Image class
        self.assertIsInstance(result, Image.Image)

        # Assert that the result image has the same size as the input image
        self.assertEqual(result.size, im.size)

    def test_color(self):
        # Create a test image
        im = Image.new("RGB", (100, 100), color="red")

        # Create an ImageProcessor object
        processor = ImageProcessor(im)

        # Call the color method
        result = processor.color(1.5)

        # Assert that the result is an instance of the Image class
        self.assertIsInstance(result, Image.Image)

        # Assert that the result image has the same size as the input image
        self.assertEqual(result.size, im.size)

    def test_sharpness(self):
        # Create a test image
        im = Image.new("RGB", (100, 100), color="red")

        # Create an ImageProcessor object
        processor = ImageProcessor(im)

        # Call the sharpness method
        result = processor.sharpness(1.5)

        # Assert that the result is an instance of the Image class
        self.assertIsInstance(result, Image.Image)

        # Assert that the result image has the same size as the input image
        self.assertEqual(result.size, im.size)


if __name__ == "__main__":
    unittest.main()
