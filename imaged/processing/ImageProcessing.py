from PIL import Image
from PIL import ImageEnhance
from PIL import ImageChops
from PIL import ImageDraw, ImageFont


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
        # new_image.show()
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
        # new_image.show()
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
        # new_image.show()
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


def resize(im: Image.Image, size: tuple) -> Image.Image:
    """
    Resizes the image.
    Args:
        im: image to be resized.
        size: new size.
    Returns:
        resized image.
    """
    return im.resize(size)


def reshape(im: Image.Image, size: tuple) -> Image.Image:
    """
    Reshapes the image.
    Args:
        im: image to be reshaped.
        size: new size.
    Returns:
        reshaped image.
    """
    return im.resize(size)


def rotate(im: Image.Image, angle: float) -> Image.Image:
    """
    Rotates the image.
    Args:
        im: image to be rotated.
        angle: rotation angle in degrees.
    Returns:
        rotated image.
    """
    return im.rotate(angle)


def addtext(im: Image.Image, texts, font, c: tuple, loc: tuple):

    # create draw object
    img = im
    draw = ImageDraw.Draw(img)
    draw.text(xy=loc,
              text=texts,
              font=font,
              fill=c)

    # img.show()
    return img
