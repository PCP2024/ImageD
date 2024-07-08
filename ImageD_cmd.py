import imaged
import argparse
import PIL
import imaged.dataio
import imaged.processing
import imaged.processing.ImageProcessing
import json


def main():
    config = json.load(open("config.json"))
    config = config.get("CMD", None)[0]

    parser = argparse.ArgumentParser(
        description="Hello! Thank you for using ImageD. We hope you have a pleasant experience. Enjoy!",
        epilog="Goodbye, thank you for using ImageD. You will be missed. xoxo",
        prog="ImageD",
    )

    with open("VERSION", "r") as f:
        program_version = f.readline()

    parser.add_argument("--version", action="version", version=program_version)

    parser.add_argument(
        "input_image", help="file path for input image 1", metavar="IMAGE_IN_PATH"
    )

    parser.add_argument(
        "-o",
        "--output_image",
        help="file path for output image",
        metavar="IMAGE_OUT_PATH",
    )

    parser.add_argument(
        "--brightness",
        type=float,
        metavar="BRIGHTNESS_RATIO",
        help="""
        Adjusts image brightness.
        Args:
            BRIGHTNESS_RATIO: brightness ratio. 0: black, 1: same, >1: brighter.
        """,
    )

    parser.add_argument(
        "--contrast",
        type=float,
        metavar="CONTRAST_RATIO",
        help="""
        Adjusts image contrast.
        Args:
            CONTRAST_RATIO: contrast ratio. 0: full grey, 1: same, >1: more contrast.
        """,
    )

    parser.add_argument(
        "--color",
        type=float,
        metavar="COLOR_RATIO",
        help="""
        Adjusts image colors.
        Args:
            COLOR_RATIO: color ratio. 0: black and white, 1: same, >1: enhanced colors.
        """,
    )

    parser.add_argument(
        "--sharpness",
        type=float,
        metavar="SHARPNESS_RATIO",
        help="""
        Adjusts image sharpness.
        Args:
            SHARPNESS_RATIO: sharpness ratio. 0: blur, 1: same, >1: sharpened image.
        """,
    )

    parser.add_argument(
        "--resize",
        nargs=2,
        type=int,
        metavar=("HORIZ_PX", "VERT_PX"),
        help="""
    Resizes the image.
    Args:
        HORIZ_PX: integer, horizontal pixel count
        VERT_PX: integer, vertical pixel count
    """,
    )

    parser.add_argument(
        "--rotate",
        type=float,
        metavar="ANGLE",
        help="""
    Rotates the image.
    Args:
        angle: counter-clockwise rotation angle in degrees
    """,
    )

    parser.add_argument(
        "--remove_background",
        action="store_true",
        help="""
    Removes the background from the image.
    """,
    )

    args = parser.parse_args()

    # Load input images 1 and 2
    imload_instance = imaged.dataio.ImageLoader(args.input_image)
    image = imload_instance.load_image()
    imload_instance.show_image(image)

    # Process image
    if args.remove_background or config.get("remove_background", False):
        image = imaged.processing.ImageProcessing.remove_background(image)

    if args.brightness is not None or config.get("brightness", None) is not None:
        brightness = args.brightness if args.brightness is not None else config.get(
            "brightness", None)
        process_instance = imaged.processing.ImageProcessing.ImageProcessor(
            image)
        image = process_instance.brightness(brightness)

    if args.contrast is not None or config.get("contrast", None) is not None:
        contrast = args.contrast if args.contrast is not None else config.get(
            "contrast", None)
        process_instance = imaged.processing.ImageProcessing.ImageProcessor(
            image)
        image = process_instance.contrast(contrast)

    if args.color is not None or config.get("color", None) is not None:
        color = args.color if args.color is not None else config.get(
            "color", None)
        process_instance = imaged.processing.ImageProcessing.ImageProcessor(
            image)
        image = process_instance.contrast(color)

    if args.sharpness is not None or config.get("sharpness", None) is not None:
        sharpness = args.sharpness if args.sharpness is not None else config.get(
            "sharpness", None)
        process_instance = imaged.processing.ImageProcessing.ImageProcessor(
            image)
        image = process_instance.contrast(sharpness)

    if args.resize is not None or config.get("resize", None) is not None:
        resize = args.resize if args.resize is not None else config.get(
            "resize", None)
        image = imaged.processing.ImageProcessing.resize(
            image, tuple(resize))
        image.show()

    if args.rotate is not None or config.get("rotate", None) is not None:
        rotate = args.rotate if args.rotate is not None else config.get(
            "rotate", None)
        image = imaged.processing.ImageProcessing.rotate(image, rotate)
        image.show()

    if args.output_image is not None or config.get("output_image", None) is not None:
        output_image = args.output_image if args.output_image is not None else config.get(
            "output_image", None)
        output_instance = imaged.dataio.ImageLoader(output_image)
        output_instance.save_image(image, save_path=output_image)


if __name__ == "__main__":
    main()
