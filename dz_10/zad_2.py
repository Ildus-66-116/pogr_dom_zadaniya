"""На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.

Напишите класс LotteryGame, который будет иметь метод compare_lists,
который будет сравнивать числа из вашего билета из list1 со списком выпавших чисел list2

Если совпадающих чисел нет, то выведите на экран:
Совпадающих чисел нет."""


class LotteryGame:
    def __init__(self, list_1, list_2):
        self._list_1 = list_1
        self._list_2 = list_2

    def compare_lists(self):
        result = []
        for i in self._list_1:
            if i in self._list_2:
                result.append(i)
        if result:
            return f'Совпадающие числа: {result}\nКоличество совпадающих чисел: {len(result)}'
        else:
            return 'Совпадающих чисел нет.'


if __name__ == '__main__':
    list1 = ["a", 12, 8, 41, 7, 21, 9, 14, 5, 30, 45]
    list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, "a", 45, 48]

    game = LotteryGame(list1, list2)
    matching_numbers = game.compare_lists()
    print(matching_numbers)
