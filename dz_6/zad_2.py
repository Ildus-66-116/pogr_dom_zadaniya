# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
# функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens),
# которая проверяет все возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.
from random import randint


def is_attacking(q1, q2):
    x1, y1 = q1[0], q1[1]
    x2, y2 = q2[0], q2[1]
    if x1 == x2 or y1 == y2:
        return True
    elif abs(x1 - x2) == abs(y1 - y2):
        return True
    return False


def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True



if __name__ == '__main__':
    queens = [(randint(1, 8), randint(1, 8)),
              (randint(1, 8), randint(1, 8)),
              (randint(1, 8), randint(1, 8)),
              (randint(1, 8), randint(1, 8))]
    result = check_queens(queens)
    print(result)
