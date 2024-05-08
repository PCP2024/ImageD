from PIL import Image
from PIL import ImageEnhance
from PIL import ImageChops


class ImageProcessor:
    def __init__(self, im: Image.Image) -> None:
        """
        Initialize the ImageProcessor object.
        Args:
            im: PIL image object.
        """
        self.image = im

    def brightness(self, param: float) -> Image.Image:
        """
        Adjusts image brightness.
        Args:
            param: brightness parameter. 0: black, 1: same, >1: brighter.
        Returns:
            brightness adjusted image.
        """
        imb = ImageEnhance.Brightness(self.image)
        new_image = imb.enhance(param)
        new_image.show()
        return new_image

    def contrast(self, param: float) -> Image.Image:
        """
        Adjusts image contrast.
        Args:
            param: contrast parameter. 0: full grey, 1: same, >1: more contrast.
        Returns:
            contrast adjusted image.
        """
        imc = ImageEnhance.Contrast(self.image)
        new_image = imc.enhance(param)
        new_image.show()
        return new_image

    def color(self, param: float) -> Image.Image:
        """
        Adjusts image colors.
        Args:
            param: color parameter. 0: black and white, 1: same, >1: enhanced colors.
        Returns:
            color adjusted image.
        """
        imc = ImageEnhance.Color(self.image)
        new_image = imc.enhance(param)
        new_image.show()
        return new_image

    def sharpness(self, param: float) -> Image.Image:
        """
        Adjusts image sharpness.
        Args:
            param: sharpness parameter. 0: blur, 1: same, >1: sharpened image.
        Returns:
            sharpness adjusted image.
        """
        ims = ImageEnhance.Sharpness(self.image)
        new_image = ims.enhance(param)
        new_image.show()
        return new_image


def subtract(im1: Image.Image, im2: Image.Image, **kwargs) -> Image.Image:
    """
    Subtracts two images.
    For absolute difference, use ImageChops.difference.
    Args:
        im1: first image.
        im2: second image.
    Returns:
        image containing the subtraction of the two images.
    """
    return ImageChops.subtract(im1, im2, **kwargs)


def difference(im1: Image.Image, im2: Image.Image, **kwargs) -> Image.Image:
    """
    Absolute difference between two images.
    For subtraction, use ImageChops.subtract.
    Args:
        im1: first image.
        im2: second image.
    Returns:
        image containing the absolute difference between the two images.
    """
    return ImageChops.difference(im1, im2, **kwargs)
