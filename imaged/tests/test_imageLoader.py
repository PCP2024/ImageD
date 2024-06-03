import unittest
from PIL import Image
from ..dataio.imageLoader import ImageLoader, ImageLoadException
from pathlib import Path


class TestImageLoader(unittest.TestCase):
    def setUp(self):
        self.image_path = Path("demodata/test_image.jpeg")
        self.loader = ImageLoader(self.image_path)

    def tearDown(self):
        self.loader.close_image()

    def test_load_image(self):
        image = self.loader.load_image()
        self.assertIsInstance(image, Image.Image)
        self.assertEqual(image.mode, "RGB")
        self.assertEqual(image.size, (800, 600))

    def test_print_image_details(self):
        image = Image.new("RGB", (800, 600))
        self.loader.print_image_details(image)

    def test_save_image(self):
        image = Image.new("RGB", (800, 600))
        save_path = str(self.image_path.parent / "image.jpg")
        self.loader.save_image(image, save_path)
        # Add assertions to check if the image is saved correctly


if __name__ == "__main__":
    unittest.main()
