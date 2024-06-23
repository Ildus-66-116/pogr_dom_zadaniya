# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске,
# в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом,
# что они не находятся на одной вертикали, горизонтали или диагонали.
# Список из 4-х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.

from random import randint
from zad_2 import check_queens


def generate_board():
    board = []
    for i in range(1, 9):
        queen = (i, randint(1, 8))
        board.append(queen)
    return board


def generate_boards():
    my_board_list = []
    while len(my_board_list) < 4:
        queens = generate_board()
        if check_queens(queens):
            my_board_list.append(queens)
    return my_board_list


board_list = generate_boards()
print(board_list)
if len(board_list) != 4:
    print("Вы собрали не то количество комбинаций")
else:
    print("Отлично!")
