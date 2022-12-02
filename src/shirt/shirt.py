import os
import sys
from os import path

from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    input_filename = sys.argv[1].lower()
    output_filename = sys.argv[2].lower()

    _, ext = path.splitext(input_filename)
    _, out_ext = path.splitext(output_filename)
    if not (ext == ".jpg" or ext == ".png" or ext == ".jpeg"):
        sys.exit("Invalid input")

    if not (out_ext == ".jpg" or out_ext == ".png" or out_ext == ".jpeg"):
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
