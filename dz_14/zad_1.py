"""Возьмите задачу Rectangle с прошлых семинаров. Напишите тесты для этой задачи.
Исходный код в редакторе кода надо доработать, чтобы вызывалось исключение NegativeValueError.
Используйте модуль doctest."""

import doctest
class NegativeValueError(ValueError):
    pass


class Rectangle:
    """
    Класс, представляющий прямоугольник.
    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника
    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        """
        >>> r1 = Rectangle(5)
        >>> r1.width
        5
        >>> r3 = Rectangle(-2)
        Traceback (most recent call last):
        ...
        zad_1.NegativeValueError: Ширина должна быть положительной, а не -2
        >>> r4 = Rectangle(5, -3)
        Traceback (most recent call last):
        ...
        zad_1.NegativeValueError: Высота должна быть положительной, а не -3
        >>> r2 = Rectangle(3, 4)
        >>> r2.width == 3
        True
        >>> r2.height == 4
        True
        """
        if width <= 0:
            raise NegativeValueError(f"Ширина должна быть положительной, а не {width}")
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f"Высота должна быть положительной, а не {height}")
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise NegativeValueError(f"Ширина должна быть положительной, а не {value}")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value is None:
            self._height = self._width
        elif value <= 0:
            raise NegativeValueError(f"Высота должна быть положительной, а не {value}")
        else:
            self._height = value

    def perimeter(self):
        """
        >>> r1 = Rectangle(5)
        >>> r1.perimeter() == 20
        True
        >>> r2 = Rectangle(3, 4)
        >>> r2.perimeter() == 14
        True
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        >>> r1 = Rectangle(5)
        >>> r1.area() == 25
        True
        >>> r2 = Rectangle(3, 4)
        >>> r2.area() == 12
        True
        """
        return self.width * self.height

    def __add__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 + r2
        >>> r3.width
        8
        >>> r3.height
        6.0
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 - r2
        >>> r3.width == 2
        True
        >>> r3.height
        2.0
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.
        Аргументы:
        - other (Rectangle): второй прямоугольник
        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.
        Аргументы:
        - other (Rectangle): второй прямоугольник
        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.
        Аргументы:
        - other (Rectangle): второй прямоугольник
        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.
        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.
        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"


if __name__ == '__main__':
    doctest.testmod(extraglobs={'__file__': __file__})

