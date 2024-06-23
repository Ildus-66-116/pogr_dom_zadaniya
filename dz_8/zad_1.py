"""Вам необходимо написать функцию traverse_directory(directory_),
которая будет выполнять обход директории и возвращать результаты в виде списка словарей.
После этого результаты должны быть сохранены в трех различных файлах
(JSON, CSV и Pickle) с помощью функций save_results_to_json,
save_results_to_csv и save_results_to_pickle.

Файлы добавляются в список results в том порядке, в котором они встречаются
при рекурсивном обходе директорий. При этом сначала добавляются файлы,
а затем директории.

Для каждого файла (name в files), сначала создается полный путь к файлу
(path = os.path.join(root, name)), и затем получается размер файла
(size = os.path.getsize(path)). Информация о файле добавляется в список results
в виде словаря {'Path': path, 'Type': 'File', 'Size': size}.

Затем, для каждой директории (name в dirs), также создается полный путь к
директории (path = os.path.join(root, name)), и вызывается функция get_dir_size(path),
чтобы получить размер всей директории с учетом ее содержимого.
Информация о директории добавляется в список results в виде
словаря {'Path': path, 'Type': 'Directory', 'Size': size}."""
import os
import json
import csv
import pickle

KEY_DIRECTORY = ['Path', 'Type', 'Size']


def get_dir_size(folder):
    total_size = 0
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        if os.path.isfile(item_path):
            total_size += os.path.getsize(item_path)
        elif os.path.isdir(item_path):
            total_size += get_dir_size(item_path)
    return total_size


def traverse_directory(directory):
    results = []
    for dir_path, dir_name, file_name in os.walk(directory):
        results.append({KEY_DIRECTORY[0]: dir_path.replace('\\', '/'), KEY_DIRECTORY[1]: 'Directory',
                        KEY_DIRECTORY[2]: get_dir_size(dir_path)})
        for name in file_name:
            path_1 = {KEY_DIRECTORY[0]: os.path.join(dir_path, name).replace('\\', '/'),
                      KEY_DIRECTORY[1]: 'File',
                      KEY_DIRECTORY[2]: os.path.getsize(os.path.join(dir_path, name))}
            results.append(path_1)
    return results[1:]


def save_results_to_json(data_json, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data_json, f, ensure_ascii=False)


def save_results_to_csv(data_csv, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=["Path", "Type", "Size"], quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        csv_write.writerows(data_csv)


def save_results_to_pickle(data_pickle, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(data_pickle, f)


if __name__ == '__main__':
    key_dict = traverse_directory('C:/Users/Ильдус/Documents/Моя учеба/Основы Python/praktika/dz_8')
    save_results_to_json(key_dict, 'directory.json')
    save_results_to_csv(key_dict, 'directory.csv')
    save_results_to_pickle(key_dict, 'directory.pickle')
    list(map(lambda x: print(x), key_dict))
