import sys
from PIL import Image
from typing import List


def main() -> None:
    # Check if the user has provided an image file.
    if len(sys.argv) != 2:
        print("Usage: python3 Assignment 1.py <image>")
        sys.exit(1)

    # Load the image.
    print("Loading image.")
    image: Image.Image = Image.open(sys.argv[1])

    # Print the image's details.
    # Data type:
    print("Image data type:", image.mode)
    # Image size:
    print("Image size:", image.size)

    # Display the image.
    print("Displaying image. Close the window to exit.")
    image.show()

    # Wait until the user closes the window.
    print("Image closing.")
    image.close()

    # Exit the program.
    print("Image closed. Exiting.")
    sys.exit(0)


if __name__ == "__main__":
    main()
