import imaged
import argparse
import PIL
import imaged.dataio
import imaged.processing
import imaged.processing.ImageProcessing


def main():
    parser = argparse.ArgumentParser(description = "Hello! Thank you for using ImageD. We hope you have a pleasant experience. Enjoy!",
                                     epilog = "Goodbye, thank you for using ImageD. You will be missed. xoxo",
                                     prog = "ImageD")
    with open("VERSION", "r") as f:
        program_version = f.readline()
    
    parser.add_argument("--version", action = "version", version = program_version)
    parser.add_argument("input_image", help="file path")
    parser.add_argument("-o","--output_image", help="file path for output image")

    parser.add_argument("--brightness", type=float, help="""
        Adjusts image brightness.
        Args:
            param: brightness parameter. 0: black, 1: same, >1: brighter.
        Returns:
            brightness adjusted image.
        """)
    
    args = parser.parse_args()

    # Load image
    imload_instance = imaged.dataio.ImageLoader(args.input_image)
    image = imload_instance.load_image()

    # Process image
    if args.brightness is not None:
        process_instance = imaged.processing.ImageProcessing.ImageProcessor(image)
        image = process_instance.brightness(args.brightness)

    # output
    if args.output_image is not None:
        output_instance = imaged.dataio.ImageLoader(args.output_image)
        output_instance.save_image(image, save_path=args.output_image)


    #image = PIL.Image.open(args.input_image)
    # parser.add_argument("input_image", type=argparse.FileType('r'))


if __name__ == "__main__":
    main()
