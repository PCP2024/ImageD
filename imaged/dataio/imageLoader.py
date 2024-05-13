from PIL import Image
from typing import List


class ImageLoadException(Exception):
    """
    Exception raised when there is an error loading an image.
    """
    pass


class ImageLoader:
    """A class for loading, manipulating, and saving images."""

    def __init__(self, image_path: str) -> None:
        """
        Initialize the ImageLoader object.

        Args:
            image_path (str): The path to the image file.
        """
        self.image_path = image_path

    def __call__(self) -> Image.Image:
        """
        Load and return the image.

        Returns:
            Image.Image: The loaded image.
        """
        # Load the image.
        print("Loading image.")
        image = self.load_image()

        # Print the image's details.
        self.print_image_details(image)

        # Return the loaded image.
        return image

    def load_image(self) -> Image.Image:
        """
        Load the image from the specified path.

        Returns:
            Image.Image: The loaded image.

        Raises:
            ImageLoadException: If failed to load the image.
        """
        try:
            self.image = Image.open(self.image_path)
            print("Image loaded.")
            return self.image
        except Exception as e:
            raise ImageLoadException("Failed to load image.") from e

    def print_image_details(self) -> None:
        """
        Print the details of the image.

        Args:
            image (Image.Image): The image to print the details of.
        """
        print("Image data type:", self.image.mode)
        print("Image size:", self.image.size)

    def close_image(self) -> None:
        """
        Close the image.

        Args:
            image (Image.Image): The image to close.
        """
        print("Image closing.")
        self.image.close()

    def show_image(self) -> None:
        """
        Show the image.

        Args:
            image (Image.Image): The image to show.
        """
        print("Showing image.")
        self.image.show()

    def save_image(self, save_path: str, format: str = None) -> None:
        """
        Save the image to the specified path.

        Args:
            image (Image.Image): The image to save.
            save_path (str): The path to save the image.
            format (str, optional): The format to save the image in. Defaults to None.

        Raises:
            ValueError: If the image format is invalid.
        """
        # Validate the format.
        valid_formats = ["jpg", "jpeg", "png", "gif"]
        if format:
            if format not in valid_formats:
                raise ValueError("Invalid image format")

        # Save the image.
        self.image.save(save_path, format)
        print("Image saved at:", save_path)
