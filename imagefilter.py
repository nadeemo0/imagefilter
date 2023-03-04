import math
from PIL import Image

VALID_MODES = ['gray', 'flip', 'shrink']

def main():
    # Open image
    image = Image.open('jump.jpeg')

    # Show image
    image.show()

    # Get the height and width
    width, height = image.size

    # Create a new image of the same size as the original
    new_image = Image.new("RGB", (width, height), "white")

    mode = input("Enter mode: ")

    if mode in VALID_MODES:
        if mode == "gray":
            grayscale(image, new_image)
        elif mode == "flip":
            m2 = input("Vertical or Horizontal?\n")
            if m2 == "Vertical":
                flip("Vertical", image, new_image)
            elif m2 == "Horizontal":
                flip("Horizontal", image, new_image)
        elif mode == "shrink":
            shrink(image, new_image)
    else:
        print("Invalid mode")

def grayscale(image, new_image):
    # Convert image to grayscale
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x,y))
            gray = math.floor((r + g + b) / 3)
            new_image.putpixel((x,y), (gray, gray, gray))
    new_image.show()
    new_image.save("grayscale.JPG")

def flip(direction, image, new_image):
    # Flip image 
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x,y))
            if direction == "Vertical": 
                new_image.putpixel((x, image.height-1-y), (r, g, b))
            elif direction == "Horizontal":
                new_image.putpixel((image.width-1-x, y), (r, g, b))
    new_image.show()
    new_image.save("flip.JPG")

def shrink(image, new_image):
    # Calculate new width and height
    new_width = image.width // 2
    new_height = image.height // 2

    # Create new image with half the pixels
    new_image = Image.new("RGB", (new_width, new_height), "white")

    # Copy every other pixel from original image to new image
    for x in range(new_width):
        for y in range(new_height):
            r, g, b = image.getpixel((2*x, 2*y))
            new_image.putpixel((x,y), (r, g, b))

    # Show and save new image
    new_image.show()
    new_image.save("shrink.JPG")

if __name__ == "__main__":
    main()