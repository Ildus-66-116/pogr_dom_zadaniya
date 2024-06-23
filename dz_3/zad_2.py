# В большой текстовой строке text подсчитать количество встречаемых слов
# и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд
# (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов.
# Слова выведите в обратном алфавитном порядке.
import re


def word_count(text):
    counts = dict()
    words = text.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


text = "Hello world. don't Hello 5689 Python. Hello again."
processed_text = re.sub("[@#$!?.,'0123456789]", " ", text)
processed_text = processed_text.lower()
words = processed_text.split()
words.sort(reverse=True)
sorted_text = ' '.join(words)
final_dict = word_count(sorted_text)
sorted_dict = dict(sorted(final_dict.items(), key=lambda item: item[1], reverse=True))
final_tuple = list(sorted_dict.items())[:10]
print(final_tuple)



# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words1 = cleaned_text.split()
word_counts = {}

for word in words1:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]

print(top_words)




