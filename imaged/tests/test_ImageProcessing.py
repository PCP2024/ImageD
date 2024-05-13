import unittest
from PIL import Image, ImageEnhance
from processing.ImageProcessing import (
    difference,
    subtract,
    ImageProcessor,
    remove_background,
)


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

    def test_subtract(self):
        # Create two test images
        im1 = Image.new("RGB", (100, 100), color="red")
        im2 = Image.new("RGB", (100, 100), color="blue")

        # Call the substract function
        result = subtract(im1, im2)

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

    def test_rotate(self):
        # Create a test image
        im = Image.new("RGB", (100, 100), color="red")

        # Create an ImageProcessor object
        processor = ImageProcessor(im)

        # Call the rotate method
        result = processor.rotate(90)

        # Assert that the result is an instance of the Image class
        self.assertIsInstance(result, Image.Image)

        # Assert that the result image has the expected size
        self.assertEqual(result.size, (100, 100))

    def test_resize(self):
        # Create a test image
        im = Image.new("RGB", (100, 100), color="red")

        # Create an ImageProcessor object
        processor = ImageProcessor(im)

        # Call the resize method
        result = processor.resize((50, 50))

        # Assert that the result is an instance of the Image class
        self.assertIsInstance(result, Image.Image)

        # Assert that the result image has the expected size
        self.assertEqual(result.size, (50, 50))

    def test_reshape(self):
        # Create a test image
        im = Image.new("RGB", (100, 100), color="red")

        # Create an ImageProcessor object
        processor = ImageProcessor(im)

        # Call the reshape method
        result = processor.reshape((50, 50))

        # Assert that the result is an instance of the Image class
        self.assertIsInstance(result, Image.Image)

        # Assert that the result image has the expected size
        self.assertEqual(result.size, (50, 50))

    def test_remove_background(self):
        # Create a test image
        # im = Image.new("RGB", (100, 100), color="red")
        im = Image.open("demodata/test_image.jpg")

        # Call the remove_background function
        result = remove_background(im)

        # Assert that the result is an instance of the Image class
        self.assertIsInstance(result, Image.Image)

        # Assert that the result image has the same size as the input image
        self.assertEqual(result.size, im.size)


if __name__ == "__main__":
    unittest.main()
