"""Напишите к ней тесты, используя unittest и лежать в class TestRectangle(unittest.TestCase)"""

import unittest


class NegativeValueError(ValueError):
    pass


class Rectangle:

    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


class TestPrime(unittest.TestCase):
    def test_width(self):
        self.r1 = Rectangle(5)
        self.assertEqual(self.r1.width, 5)

    def test_height(self):
        self.r2 = Rectangle(3, 4)
        self.assertEqual(self.r2.height, 4)

    def test_perimeter(self):
        self.r1 = Rectangle(5)
        self.assertEqual(self.r1.perimeter(), 20)

    def test_area(self):
        self.r2 = Rectangle(3, 4)
        self.assertEqual(self.r2.area(), 12)

    def test_addition(self):
        self.r1 = Rectangle(5)
        self.r2 = Rectangle(3, 4)
        self.r3 = self.r1 + self.r2
        self.assertEqual(self.r3.width, 8)
        self.assertEqual(self.r3.height, 6.0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
