def main():
    import time
    from ascii_renderer import AsciiRenderer
    from PIL import Image

    def average(color):
        total = 0
        total += color[0]
        total += color[1]
        total += color[2]
        total = total / 3
        return total

    def translate(value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)

    #Variables
    density_list = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,^`'."
    density_list = list(density_list)
    index_max = len(density_list) - 1

    img = Image.open("pic.png")
    pix = img.load()
    img_width, img_height = img.size


    #Create renderer object
    renderer = AsciiRenderer(img_width, img_height)

    #Clear frame buffer
    renderer.clear()

    for y in range(img_height):
        for x in range(img_width): #For every 5 pixels in the image
            color = average(pix[x,y])
            if color != 255:
                char_to_set = round(translate(color, 0, 255, 0, index_max))
                renderer.set_pixel(x, y, density_list[char_to_set])

    #Render final image
    renderer.render()

    input("press enter to close. . .")

if __name__ == "__main__":
    main()