"""Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:

a. Принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. Принимать параметр количество цифр в порядковом номере.
c. Принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. Принимать параметр расширение конечного файла.
e. Принимать диапазон сохраняемого оригинального имени. Например, для диапазона [3, 6] берутся буквы с 3 по 6
    из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
    Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории"""
import os
import shutil
from pathlib import Path


def rename_files(desired_name, num_digits, source_ext, target_ext):
    number = 0
    file_in_dir = os.listdir('test_folder')
    file_in_dir.sort()
    for obj in file_in_dir:
        if os.path.splitext(obj)[1] == f'.{source_ext}':
            number += 1
            formatted_number = f"{number:0{num_digits}}"
            new_name = f'{desired_name}{formatted_number}.{target_ext}'
            source = f'test_folder/{obj}'
            dest = f'test_folder/{new_name}'
            os.rename(source, dest)


rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

