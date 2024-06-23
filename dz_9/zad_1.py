"""Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой
строке, от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:

file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
Функция принимает три аргумента:
a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json.
Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация
о параметрах и результатах вычислений для каждой строки данных из CSV-файла."""

from random import randint
import csv
from typing import Callable
import json


def generate_csv_file(file_name, rows):
    """Генерирует по три случайны числа в каждой строке, от 100-1000 строк"""
    with open(file_name, 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.writer(f_write)
        for i in range(rows):
            row = [randint(1, 1000) for _ in range(3)]
            csv_write.writerow(row)


def find_roots(a, b, c):
    """Находит корни квадратного уравнения вида ax^2 + bx + c = 0"""
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant < 0:
        return None
    elif discriminant == 0:
        root = -b / (2 * a)
        return {"result": root}
    else:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return {"result1": root1, "result2": root2}


def save_to_json(func: Callable):
    """Декоратор find_roots"""

    def wrapper(*args, **kwargs):
        filename = args[0]
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            csv_file = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            roots_data = []
            for row in csv_file:
                try:
                    a, b, c = map(float, row)
                    result = func(a, b, c)
                    if result is None:
                        roots_data.append({"parameters": row, 'Нет решения': 'discriminant < 0'})
                    else:
                        roots_data.append({"parameters": row, **result})
                except ValueError:
                    print(f"Ошибка при преобразовании строки {row} в числа")
            with open('results.json', 'w', encoding='utf-8') as outfile:
                json.dump(roots_data, outfile, ensure_ascii=False)

    return wrapper


@save_to_json
def find_roots(a, b, c):
    """Находит корни квадратного уравнения вида ax^2 + bx + c = 0"""
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant < 0:
        return None
    elif discriminant == 0:
        root = -b / (2 * a)
        return {"result": root}
    else:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return {"result1": root1, "result2": root2}


if __name__ == '__main__':
    generate_csv_file("input_data.csv", 110)
    find_roots("input_data.csv")

    with open("results.json", 'r') as f:
        data = json.load(f)
    if 100 <= len(data) <= 1000:
        print(True)
    else:
        print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")
    print(len(data) > 100)
