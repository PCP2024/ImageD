import unittest
from PIL import Image
from processing.ImageProcessing import difference
from processing.ImageProcessing import substract


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


class ImageProcessingTest(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
