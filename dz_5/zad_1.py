# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os


def get_file_info(file_path: str) -> tuple:
    # directory = os.path.dirname(file_path)
    # if directory == '':
    #     directory_new = directory
    # else:
    #     directory_new = directory + '/'
    # filename = os.path.basename(file_path)
    # name, extension = os.path.splitext(filename)
    # return directory_new, name, extension

    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension) - 1], "." + file_extension)


file_path = 'file_in_current_directory.txt'
print(get_file_info(file_path))

file_path = "C:/Users/User/Documents/example.txt"
print(get_file_info(file_path))
