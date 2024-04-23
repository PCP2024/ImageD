import unittest
from ..dataio.imageLoader import main
import sys


class ImageLoaderTestCase(unittest.TestCase):
    def test_image_loading(self):
        # Test loading a valid image file
        # Replace 'path_to_image' with the actual path to an image file
        image_path = 'path_to_image'
        sys.argv = ['Assignment 1.py', image_path]
        main()

    def test_missing_image_file(self):
        # Test when no image file is provided
        sys.argv = ['Assignment 1.py']
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)

    def test_invalid_image_file(self):
        # Test loading an invalid image file
        # Replace 'path_to_invalid_image' with the actual path to an invalid image file
        invalid_image_path = 'path_to_invalid_image'
        sys.argv = ['Assignment 1.py', invalid_image_path]
        with self.assertRaises(Exception):
            main()


if __name__ == '__main__':
    unittest.main()
