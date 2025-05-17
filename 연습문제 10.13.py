#연습문제 10.13
class Rectangle:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"Rectangle : (x = {self.__x}, y = {self.__y}, w = {self.__width}, h = {self.__height}), 면적 : {self.area()}"

    def set_x(self, x): self.__x = x
    def get_x(self): return self.__x

    def set_y(self, y): self.__y = y
    def get_y(self): return self.__y

    def set_width(self, width): self.__width = width
    def get_width(self): return self.__width

    def set_height(self, height): self.__height = height
    def get_height(self): return self.__height

    def area(self):
        return self.__width * self.__height

    def overlaps(self, other):
        left1 = self.__x
        right1 = self.__x + self.__width
        top1 = self.__y
        bottom1 = self.__y - self.__height

        left2 = other.__x
        right2 = other.__x + other.__width
        top2 = other.__y
        bottom2 = other.__y - other.__height

        return not (right1 <= left2 or right2 <= left1 or bottom1 >= top2 or bottom2 >= top1)

    def contains(self, other):
        left1 = self.__x
        right1 = self.__x + self.__width
        top1 = self.__y
        bottom1 = self.__y - self.__height

        left2 = other.__x
        right2 = other.__x + other.__width
        top2 = other.__y
        bottom2 = other.__y - other.__height

        return (left1 <= left2 and right1 >= right2 and top1 >= top2 and bottom1 <= bottom2)

