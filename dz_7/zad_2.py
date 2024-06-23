with open("__init__.py", "a", encoding='utf-8') as init_file:
    init_file.write('from .zad_1 import rename_files\n\n__all__ = ["rename_files"]\n')
