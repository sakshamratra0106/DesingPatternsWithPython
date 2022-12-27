from abc import ABC, abstractmethod

class Rectangle:

    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    # In Python, a getter is a method that is used to retrieve the value of an attribute.
    # It is defined using the @property decorator, which allows the method to be accessed like an attribute.
    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self._height = value


class AreaCalculator:
    def calculate(self, rects):
        for r in rects:
            print("Area is : {}".format(r.height * r.width))


class Square(Rectangle):
    def get_width(self) -> float:
        return self._width

    def set_width(self, value: float) -> None:
        self._width = value
        self._height = value

    def get_height(self) -> float:
        return self._height

    def set_height(self, value: float) -> None:
        self._width = value
        self._height = value

    width = property(get_width, set_width)
    height = property(get_height, set_height)


sq = Square(8, 8)
sq.width = 8
sq.height = 8

rect = Square(2, 3)
rect.width = 2
rect.height = 3

liste = [sq, rect]
ac = AreaCalculator()
ac.calculate(liste)
# Area is : 64
# Area is : 9


## After improvements

class Rectangle:

    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self._height = value

    @property
    def area(self) -> float:
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side: float) -> None:
        self.__side = side
        super(Square, self).__init__(side, side)

    @property
    def width(self) -> float:
        return self.__side

    @width.setter
    def width(self, value: float) -> None:
        self.__side = value

    @property
    def height(self) -> float:
        return self.__side

    @height.setter
    def height(self, value: float) -> None:
        self.__side = value


r = Rectangle(width=10, height=5)
print(r.area)
# 50

s = Square(side=5)
print(s.area)
# 25