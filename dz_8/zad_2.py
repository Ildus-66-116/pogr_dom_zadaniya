function_names = ["def get_dir_size",
                  "def save_results_to_json"
                  "def save_results_to_csv",
                  "def save_results_to_pickle",
                  "def traverse_directory",
                  ]
with open("__init__.py", "w", encoding='utf-8') as init_file:
    init_file.write('function_names = ["def get_dir_size", "def save_results_to_json", "def save_results_to_csv", '
                    '"def save_results_to_pickle", "def traverse_directory",]')
