class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def count_area(self):
        return self.x * self.y


class Square(Rectangle):
    def __init__(self, z):
        self.z = z
        super().__init__(z, z)


class Cube():
    def __init__(self, square: Square):
        self.square = square
        self.x = square.x

    def count_area(self):
        return self.square.count_area() * 6

    def count_volume(self):
        return self.square.count_area() * self.x


class Cuboid():
    def __init__(self, figure, height):
        self.base = figure
        self.height = height

    def count_area(self):
        return self.base.count_area() * 2 + (self.height * 2)*(self.base.x + self.base.y)

    def count_volume(self):
        return self.base.count_area() * self.height
