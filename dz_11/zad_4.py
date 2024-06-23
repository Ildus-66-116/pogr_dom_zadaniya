"""Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.
Атрибуты класса:
rows (int): Количество строк в матрице.
cols (int): Количество столбцов в матрице.
data (list): Двумерный список, содержащий элементы матрицы.

Методы класса:

__init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows и cols, а также создает
двумерный список data размером rows x cols и заполняет его нулями.

__str__(self): Метод, возвращающий строковое представление матрицы. Возвращаемая строка представляет матрицу,
где элементы разделены пробелами, а строки разделены символами новой строки.
Например:
1 2 3
4 5 6
__repr__(self): Метод, возвращающий строковое представление объекта, которое может быть использовано для создания
нового объекта того же класса с такими же размерами и данными.
__eq__(self, other): Метод, определяющий операцию "равно" для двух матриц. Сравнивает две матрицы и возвращает True,
если они имеют одинаковое количество строк и столбцов, а также все элементы равны. Иначе возвращает False.
__add__(self, other): Метод, определяющий операцию сложения двух матриц. Проверяет, что обе матрицы имеют
одинаковые размеры (количество строк и столбцов). Если размеры совпадают, создает новую матрицу,
где каждый элемент равен сумме соответствующих элементов входных матриц.
__mul__(self, other): Метод, определяющий операцию умножения двух матриц.
Проверяет, что количество столбцов в первой матрице равно количеству строк во второй матрице.
Если условие выполняется, создает новую матрицу, где элемент на позиции [i][j] равен сумме произведений элементов
соответствующей строки из первой матрицы и столбца из второй матрицы.
"""


class Matrix:
    data = []

    def __new__(cls, rows, cols, *args):
        instance = super().__new__(cls)
        cls.data = []
        return instance

    def __init__(self, rows: int, cols: int):
        """Конструктор класса, который инициализирует атрибуты rows(Количество строк в матрице)
        и cols(Количество столбцов в матрице.)"""
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        """Метод, возвращающий строковое представление матрицы."""
        result = ""
        for row in self.data:
            result += " ".join(map(str, row)) + "\n"
        return result.rstrip()

    def __repr__(self):
        """Метод, возвращающий строковое представление объекта"""
        return f'Matrix({self.rows}, {self.cols})'

    def __eq__(self, other):
        """Метод, определяющий операцию сложения двух матриц. Проверяет, что обе матрицы имеют одинаковые
        размеры (количество строк и столбцов)."""
        if self.rows == other.rows and self.cols == other.cols:
            return self.data == other.data
        return False

    def __add__(self, other):
        """Метод, определяющий операцию сложения двух матриц. Проверяет, что обе матрицы имеют одинаковые размеры"""
        if self.rows == other.rows and self.cols == other.cols:
            summ_matrix = [[self.data[i][j] + other.data[i][j]
                            for j in range(len(self.data[0]))] for i in range(len(self.data))]
            result_sum = Matrix(self.rows, self.cols)
            result_sum.data = summ_matrix
            return result_sum
        else:
            raise ValueError('Не соответствует размеры матриц')

    def __mul__(self, other):
        """Метод, определяющий операцию умножения двух матриц.
        Проверяет, что количество столбцов в первой матрице равно количеству строк во второй матрице.
        Если условие выполняется, создает новую матрицу, где элемент на позиции [i][j] равен сумме произведений
        элементов соответствующей строки из первой матрицы и столбца из второй матрицы."""
        if self.cols == other.rows:
            result_matrix = [[0] * other.cols for _ in range(self.rows)]
            for i in range(len(self.data)):
                for j in range(len(other.data[0])):
                    for k in range(len(other.data)):
                        result_matrix[i][j] += self.data[i][k] * other.data[k][j]
            result = Matrix(self.rows, other.cols)
            result.data = result_matrix
            return result
        else:
            raise ValueError('Не соответствует размеры матриц')


if __name__ == '__main__':
    # Создаем матрицы
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(2, 3)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]

    # Выводим матрицы
    print(matrix1)

    print(matrix2)

    # Сравниваем матрицы
    print(matrix1 == matrix2)

    # Выполняем операцию сложения матриц
    matrix_sum = matrix1 + matrix2
    print(matrix_sum)

    # Выполняем операцию умножения матриц
    matrix3 = Matrix(3, 2)
    matrix3.data = [[1, 2], [3, 4], [5, 6]]

    matrix4 = Matrix(2, 2)
    matrix4.data = [[7, 8], [9, 10]]

    result = matrix3 * matrix4
    print(result)
