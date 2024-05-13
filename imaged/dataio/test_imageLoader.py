import unittest
from PIL import Image
from imageLoader import ImageLoader, ImageLoadException


class ImageLoaderTests(unittest.TestCase):

    def setUp(self):
        self.image_path = "../tests/image.jpg"
        self.loader = ImageLoader(self.image_path)

    def tearDown(self):
        try:
            self.loader.image.close()
        except AttributeError:
            pass

    def test_load_image(self):
        image = self.loader.load_image()
        self.assertIsInstance(image, Image.Image)
        self.assertEqual(image.mode, "RGB")
        self.assertEqual(image.size, (800, 600))

    def test_load_image_exception(self):
        invalid_image_path = "../tests/invalid_image.jpg"
        invalid_loader = ImageLoader(invalid_image_path)
        with self.assertRaises(ImageLoadException):
            invalid_loader.load_image()

    def test_save_image(self):
        save_path = "../tests/save_image.jpg"
        self.loader.load_image()
        self.loader.save_image(save_path)
        saved_image = Image.open(save_path)
        self.assertEqual(saved_image.mode, "RGB")
        self.assertEqual(saved_image.size, (800, 600))

    def test_save_image_with_format(self):
        save_path = "../tests/save_image.png"
        self.loader.load_image()
        self.loader.save_image(save_path, format="png")
        saved_image = Image.open(save_path)
        self.assertEqual(saved_image.mode, "RGB")
        self.assertEqual(saved_image.size, (800, 600))


if __name__ == "__main__":
    unittest.main()
