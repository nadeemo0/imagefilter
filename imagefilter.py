import math
import sys
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

    def grayscale(height, width):
        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x,y))
                gray = new_image.putpixel((x,y), (math.floor((r + g + b) / 3)))
                new_image.putpixel((x,y)(gray, gray, gray))
        new_image.save("grayscale.JPG")

    def switch(height, width):
        for x in range(width):
            for y in range(height):
                # Get the pixel from the original image
                r, g, b = image.getpixel((x,y))
                # Set the pixel in the new image
                new_image.putpixel((width-1-x, y), (r, g, b))
            
            # Show and save the new image
        new_image.show()
        new_image.save("switch.JPG")
                
    def flip(height, width):
        for x in range(width):
            for y in range(height):
                # Get the pixel from the original image
                r, g, b = image.getpixel((x,y))
                # Set the pixel in the new image
                new_image.putpixel((x, height-1-y), (r, g, b))

        # Show and save the new image
        new_image.show()
        new_image.save("flip.JPG")

    mode = sys.argv[1]

    if mode == "gray":
        grayscale(height, width)
    
    if mode == "switch":
        switch(height, width)
    
    if mode == "flip":
        flip(height, width)

if __name__ == "__main__":
    main()