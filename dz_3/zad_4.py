# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
from collections import Counter

lst = [1, 1, 2, 2, 3, 3]

final_lst = set()
duplicate_values = Counter(lst)
for key, items in duplicate_values.items():
    if items >= 2:
        final_lst.add(key)
result_my = list(final_lst)
print(result_my)

duplicates = set()
for item in lst:
    if lst.count(item) >= 2:
        duplicates.add(item)

result = list(duplicates)
print(result)




