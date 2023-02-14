import math
# run pip install pillow to install
from PIL import Image

def main():
    # Open image
    image = Image.open('jump.jpeg')

    # Show image
    image.show()

    # get the height and width
    width, height = image.size

    # get the rgb values of a pixel at a certain coordinate
    r, g, b = image.getpixel((50, 50))
    
    # create a new image of the same size as the original
    new_image = Image.new("RGB", (image.size), "white")

    # open the new image
    new_image.show()

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x,y))
            gray = new_imageputpixel((x,y), (math.floor((r + g + b) / 3)))
            new_image.putpixel((x,y)(gray, gray, gray))
    
    new_image.save("grayscale.JPG")

if __name__ == "__main__":
    main()