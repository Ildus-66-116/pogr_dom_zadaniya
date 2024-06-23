function_names = ["def save_to_json",
                  "def find_roots",
                  "def generate_csv_file",
                  ]
with open("__init__.py", "w", encoding='utf-8') as init_file:
    init_file.write('function_names = ["def save_to_json", "def find_roots", "def generate_csv_file"]')
