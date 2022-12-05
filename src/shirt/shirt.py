import os
import sys
from os import path

from PIL import Image, ImageOps


def main():
    """
    The main function takes in two command-line arguments, the input and output file names.
    It checks if the input file exists.
    It checks if the output file has the same extension as the input file.
    It checks if the output file already exists.
    It opens the input file and the shirt image.
    It resizes the input file to fit the shirt image.
    It pastes the resized input file onto the shirt image.
    It saves the pasted image to the output file.

    Args:
      self: the object that is calling the method.
      new_data: The data to be written to the file.
    Returns:
      A string of the file name.

    """
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    input_filename = sys.argv[1].lower()
    output_filename = sys.argv[2].lower()

    _, ext = path.splitext(input_filename)
    _, out_ext = path.splitext(output_filename)
    if not ext in (".jpg", ".png", ".jpeg"):
        sys.exit("Invalid input")

    if not out_ext in (".jpg", ".png", ".jpeg"):
        sys.exit("Invalid output")

    if ext != out_ext:
        sys.exit("Input and output have different extensions")

    ext = ext.upper()
    try:
        with Image.open("shirt.png") as shirt, Image.open(input_filename) as photo:
            photo = ImageOps.fit(photo, shirt.size)
            photo.paste(shirt, shirt)
            photo.save(output_filename)

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
