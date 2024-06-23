# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
#
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Предметы не должны дублироваться.
#
# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
#
# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
from collections import Counter

items = {
    "спальник": 2.0,
    "палатка": 3.5,
    "термос": 0.8,
    "карта": 0.2,
    "фонарик": 0.5,
    "котелок": 1.0,
    "еда": 3.0,
    "одежда": 1.8,
    "обувь": 1.0,
    "нож": 0.3
}
max_weight = 10.0

# value_counts = Counter(items.values())
# keys_with_duplicates = [k for k, v in items.items() if v in value_counts and value_counts[v] > 1]
# if len(keys_with_duplicates) != 0:
#     items.pop(keys_with_duplicates[0])
#
# current_weight = 0.0
#
# list_values_1 = list(values for key, values in items.items())
# list_values_1.sort(reverse=True)
# list_values = []
# for i in range(len(list_values_1)):
#     if list_values_1[i] < max_weight:
#         list_values.append(list_values_1[i])
#
# if any(map(lambda values: values < max_weight, list_values)):
#     numbers_max = 0
#     for i in range(len(list_values)):
#         current_weight += list_values[i]
#         if current_weight < max_weight:
#             numbers_max = i
#
#     final_list = list(values for values in list_values[:numbers_max + 1])
#     summ_final_list = sum(final_list)
#
#     for i in range(numbers_max + 1, len(list_values)):
#         if summ_final_list + list_values[i] < max_weight:
#             final_list.append(list_values[i])
#             summ_final_list += list_values[i]
#
#     backpack = dict()
#     for key, values in items.items():
#         if values in final_list:
#             backpack[key] = values
# #    print(backpack)
# else:
#     backpack = {None: None}
# #    print(backpack)


backpack = {}

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight
print(backpack)
