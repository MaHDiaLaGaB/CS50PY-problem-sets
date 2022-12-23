import sys
import os
from PIL import Image, ImageOps

PRIFIX = ['.jpg','.jpeg','.png']

def handle_errors():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

    if os.path.splitext(output_file)[1] not in PRIFIX:
        sys.exit('Invalid output')

    if os.path.splitext(input_file)[1] not in PRIFIX:
        sys.exit('Invalid input')

    if not os.path.splitext(output_file)[1] == os.path.splitext(input_file)[1]:
        sys.exit('Input and output have different extensions')
    return input_file, output_file

def image_edit():
    input_file, output_file = handle_errors()
    try:
        input_image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit('input does not exist')

    shirt = Image.open('shirt.png')
    size = shirt.size
    output_image = ImageOps.fit(input_image, size)
    output_image.paste(shirt, shirt)
    output_image.save(output_file)

def main():
    handle_errors()
    image_edit()

if __name__=="__main__":
    main()
