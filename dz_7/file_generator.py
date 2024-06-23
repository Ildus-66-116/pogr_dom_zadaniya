from random import randbytes, randint
from name_generator import random_name


def create_file(extension, min_len=6, max_len=30, min_size=256, max_size=4096, file_count=42):
    for i in range(1, file_count + 1):
        with open(f'test_folder/{random_name(min_len, max_len)}.{extension}', 'wb') as f:
            f.write(randbytes(randint(min_size, max_size)))


create_file('doc', file_count=3)
create_file('txt', file_count=5)
