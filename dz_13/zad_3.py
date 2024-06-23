"""В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет
следующие атрибуты:
Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число)
Сотрудники имеют также уникальный идентификационный номер (ID),
который должен быть шестизначным положительным целым числом.

Ваша задача:
Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях
(Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и
генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.

Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.

Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.

Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID
(по остатку от деления на 7).

Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно
при передаче неверных данных."""


class InvalidNameError(ValueError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Invalid name: {self.name}. Name should be a non-empty string.'


class InvalidAgeError(ValueError):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'Invalid age: {self.age}. Age should be a positive integer.'


class InvalidIdError(ValueError):
    def __init__(self, id_number):
        self.id_number = id_number

    def __str__(self):
        return f'Invalid id: {self.id_number}. Id should be a 6-digit positive integer between 100000 and 999999.'


class Person:
    MAX_LEVEL = 7

    def __init__(self, last_name: str, first_name: str, surname: str, age: int):
        if not isinstance(last_name, str) or len(last_name.strip()) == 0:
            raise InvalidNameError(last_name)
        if not isinstance(first_name, str) or len(first_name.strip()) == 0:
            raise InvalidNameError(first_name)
        if not isinstance(surname, str) or len(surname.strip()) == 0:
            raise InvalidNameError(surname)
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(age)
        self._last_name = last_name
        self._first_name = first_name
        self._surname = surname
        self._age = age

    def get_age(self):
        return self._age

    def birthday(self):
        self._age += 1

    def __str__(self):
        return f'Фамилия: {self._last_name}, Имя: {self._first_name}, Отчество: {self._surname}, Возраст: {self._age}'


class Employee(Person):
    def __init__(self, last_name: str, first_name: str, surname: str, age: int, id_number=100001):
        super().__init__(last_name, first_name, surname, age)
        if not isinstance(id_number, int) or id_number < 100_000 or id_number > 999_999:
            raise InvalidIdError(id_number)
        self._id_number = id_number

    def get_level(self):
        # id_level = str(self._id_number)
        level = sum(int(digit) for digit in str(self._id_number))
        return level // self.MAX_LEVEL

    def __str__(self):
        return super().__str__() + f' id: {self._id_number}'


if __name__ == '__main__':
    person = Person("Ford", "John", "Doe", 30)
    print(person)
    protrusion = Employee('Bad', 'Il', 'Ay', 44, 123_456)
    print(protrusion)
    print(protrusion.get_level())
    print(person.get_age())
    person.birthday()
    print(person.get_age())
