import os

class AsciiRenderer:
    def __init__(self, width, height):
        """
        Initializes a new AsciiRenderer object with the specified width and height.
        :param width: (int) Width of the AsciiRenderer object.
        :param height: (int) Height of the AsciiRenderer object.
        """
        self.width = width
        self.height = height
        self.pixels = [[' ' for y in range(height)] for x in range(width)]
    
    def set_pixel(self, x, y, char):
        """
        Sets the pixel at the specified (x,y) coordinates to the specified character.
        :param x: (int) X-coordinate of the pixel.
        :param y: (int) Y-coordinate of the pixel.
        :param char: (str) Character to set the pixel to.
        """
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            self.pixels[x][y] = char
    
    def draw_ellipse(self, x, y, rx, ry, char="*"):
        """
        Draws an ellipse on the AsciiRenderer object with center at (x,y), specified radii rx and ry, and with the specified character.
        :param x: (int) X-coordinate of the center of the ellipse.
        :param y: (int) Y-coordinate of the center of the ellipse.
        :param rx: (int) X-radius of the ellipse.
        :param ry: (int) Y-radius of the ellipse.
        :param char: (str) Character to draw the ellipse with. Optional, defaults to "".
        """
        for i in range(self.width):
            for j in range(self.height):
                if ((i-x)/rx)**2 + ((j-y)/ry)**2 <= 1:
                    self.set_pixel(i, j, char)
                    
    def draw_text(self, x, y, text):
        """
        Draws the specified text on the AsciiRenderer object starting at the specified (x,y) coordinates.
        :param x: (int) X-coordinate of the start of the text.
        :param y: (int) Y-coordinate of the start of the text.
        :param text: (str) Text to draw.
        """
        for i, char in enumerate(text):
            self.set_pixel(x + i, y, char=char)
    
    def draw_line(self, x1, y1, x2, y2, char="*"):
        """
        Draws a line on the AsciiRenderer object from (x1,y1) to (x2,y2) with the specified character.
        :param x1: (int) X-coordinate of the start of the line.
        :param y1: (int) Y-coordinate of the start of the line.
        :param x2: (int) X-coordinate of the end of the line.
        :param y2: (int) Y-coordinate of the end of the line.
        :param char: (str) Character to draw the line with. Optional, defaults to "".
        """
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            self.set_pixel(x1, y1, char="*")
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    def draw_rect(self, x, y, width, height, fill=False, char='*'):
        """
        Draws a rectangle on the AsciiRenderer object with the specified starting coordinates (x,y), width, height, and character.
        :param x: (int) X-coordinate of the top-left corner of the rectangle.
        :param y: (int) Y-coordinate of the top-left corner of the rectangle.
        :param width: (int) Width of the rectangle.
        :param height: (int) Height of the rectangle.
        :param fill: (bool) Whether or not to fill the rectangle with the specified character. Optional, defaults to False.
        :param char: (str) Character to draw the rectangle with. Optional, defaults to "".
        """
        if fill:
            for i in range(x, x + width):
                for j in range(y, y + height):
                    self.set_pixel(i, j, char)
        else:
            for i in range(x, x + width):
                self.set_pixel(i, y, char)
                self.set_pixel(i, y + height - 1, char)
            for j in range(y, y + height):
                self.set_pixel(x, j, char)
                self.set_pixel(x + width - 1, j, char)
    
    def clear(self):
        """
        Clears the AsciiRenderer object by resetting all pixels to " ".
        """
        self.pixels = [[' ' for y in range(self.height)] for x in range(self.width)]
    
    def render(self, border=False, borderChar="*"):
        """
        Renders the current state of the AsciiRenderer object. If border is True, draws a border with the specified character.
        :param border: (bool) Whether or not to draw a border around the AsciiRenderer object. Optional, defaults to False.
        :param borderChar: (str) Character to draw the border with. Optional, defaults to "".
        """
        os.system('cls')
        if border == True:
            self.draw_rect(0,0, self.width, self.height, char=borderChar)
        for j in range(self.height):
            for i in range(self.width):
                print(self.pixels[i][j], end='')
            print()