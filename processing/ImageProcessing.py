# Write function to change colours, saturation, and lighting
# Image in PIL

from PIL import Image
from PIL import ImageEnhance
from PIL import ImageChops

# img = Image.open("demodata\\test_image.jpeg")

"""
Class for processing images. 
Adjusts: Brightness, contrast, color, sharpness.
"""


class ImageProcessor:

    def __init__(self, im) -> None:
        """
        Initialize the ImageProcessor object.
        Args:
            variable containing PIL image.
        """
        self.image = im

    def brightness(self, param):
        """
        Adjusts image brightness
        Args:
            param: brightness parameter. 0:black, 1: same, >1: brighter
        Returns:
            brightness adjusted image
        """
        imb = ImageEnhance.Brightness(self.image)
        new_image = imb.enhance(param)
        new_image.show()
        return new_image

    def contrast(self, param):
        """
        Adjusts image contrast
        Args:
            param: contrast parameter. 0:full grey, 1: same, >1: more contrast
        Returns:
            contrast adjusted image
        """
        imc = ImageEnhance.Contrast(self.image)
        new_image = imc.enhance(param)
        new_image.show()
        return new_image

    def color(self, param):
        """
        Adjusts image colors
        Args:
            param: color parameter. 0:black and white, 1: same, >1: enhanced colors
        Returns:
            contrast adjusted image
        """
        imc = ImageEnhance.Color(self.image)
        new_image = imc.enhance(param)
        new_image.show()
        return new_image

    def sharpness(self, param):
        """
        Adjusts image colors
        Args:
            param: sharpness parameter. 0:blurr, 1: same, >1: sharpened image
        Returns:
            contrast adjusted image
        """
        ims = ImageEnhance.Sharpness(self.image)
        new_image = ims.enhance(param)
        new_image.show()
        return new_image


def substract(im1: Image, im2: Image, **kwargs) -> Image:
    """
    Substracts two images
    For absolute difference use ImageChops.difference
    Args:
        im1: first image
        im2: second image
    Returns:
        image containing the substraction of the two images
    """
    return ImageChops.subtract(im1, im2, **kwargs)


def difference(im1: Image, im2: Image, **kwargs) -> Image:
    """
    Absolute difference between two images
    For substraction use ImageChops.substract
    Args:
        im1: first image
        im2: second image
    Returns:
        image containing the abs difference between the two images
    """
    return ImageChops.difference(im1, im2, **kwargs)
