import imaged
import argparse
import PIL
import imaged.dataio
import imaged.processing
import imaged.processing.ImageProcessing


def main():
    parser = argparse.ArgumentParser(description="Hello! Thank you for using ImageD. We hope you have a pleasant experience. Enjoy!",
                                     epilog="Goodbye, thank you for using ImageD. You will be missed. xoxo",
                                     prog="ImageD")
    with open("VERSION", "r") as f:
        program_version = f.readline()

    parser.add_argument("--version", action="version", version=program_version)
    parser.add_argument(
        "input_image", help="file path for input image 1", metavar="IMAGE_IN_PATH")
    parser.add_argument("-o", "--output_image",
                        help="file path for output image", metavar="IMAGE_OUT_PATH")

    parser.add_argument("--brightness", type=float, metavar="BRIGHTNESS_RATIO",
                        help="""
        Adjusts image brightness.
        Args:
            param: brightness parameter. 0: black, 1: same, >1: brighter.
        Returns:
            brightness adjusted image.
        """)
    parser.add_argument("--contrast", type=float, metavar="CONTRAST_RATIO",
                        help="""
        Adjusts image contrast.
        Args:
            param: contrast parameter. 0: full grey, 1: same, >1: more contrast.
        Returns:
            contrast adjusted image.
        """)
    parser.add_argument("--color", type=float, metavar="COLOR_RATIO",
                        help="""
        Adjusts image colors.
        Args:
            param: color parameter. 0: black and white, 1: same, >1: enhanced colors.
        Returns:
            color adjusted image.
        """)

    parser.add_argument("--sharpness", type=float, metavar="SHARPNESS_RATIO",
                        help="""
        Adjusts image sharpness.
        Args:
            param: sharpness parameter. 0: blur, 1: same, >1: sharpened image.
        Returns:
            sharpness adjusted image.
        """)

    parser.add_argument("--resize", nargs=2, type=int, metavar=("HORIZ_PX", "VERT_PX"),
                        help="""
    Resizes the image.
    Args:
        size1: integer, horizontal pixel number
        size2: integer, vertical pixel number
    Returns:
        resized image.
    """)

    parser.add_argument("--rotate", type=float, metavar="ANGLE",
                        help="""
    Rotates the image.
    Args:
        angle: counter-clockwise rotation angle in degrees
    Returns:
        rotated image.
    """)

    args = parser.parse_args()

    # Load input images 1 and 2
    imload_instance = imaged.dataio.ImageLoader(args.input_image)
    image = imload_instance.load_image()
    imload_instance.show_image(image)

    # Process image
    if args.brightness is not None:
        process_instance = imaged.processing.ImageProcessing.ImageProcessor(
            image)
        image = process_instance.brightness(args.brightness)

    if args.contrast is not None:
        process_instance = imaged.processing.ImageProcessing.ImageProcessor(
            image)
        image = process_instance.contrast(args.contrast)

    if args.color is not None:
        process_instance = imaged.processing.ImageProcessing.ImageProcessor(
            image)
        image = process_instance.contrast(args.color)

    if args.sharpness is not None:
        process_instance = imaged.processing.ImageProcessing.ImageProcessor(
            image)
        image = process_instance.contrast(args.sharpness)

    if args.resize is not None:
        image = imaged.processing.ImageProcessing.resize(
            image, tuple(args.resize))
        image.show()

    if args.rotate is not None:
        image = imaged.processing.ImageProcessing.rotate(image, args.rotate)
        image.show()

    # output ()
    if args.output_image is not None:
        output_instance = imaged.dataio.ImageLoader(args.output_image)
        output_instance.save_image(image, save_path=args.output_image)

    # image = PIL.Image.open(args.input_image)
    # parser.add_argument("input_image", type=argparse.FileType('r'))


if __name__ == "__main__":
    main()
