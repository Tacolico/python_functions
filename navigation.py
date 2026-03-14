def new_folder(folder_path):
    # Deprecated
    import os
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def find(directory_path):
    # Deprecated
    import os
    file_names = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))] 
    return sorted(file_names)

def check_path(PATH):
    import os
    directory = os.path.dirname(PATH)
    if directory:  
        os.makedirs(directory, exist_ok=True)


def abs_path(directory):
    from pathlib import Path
    path = Path(directory).expanduser().resolve()
    return [str(f.resolve()) for f in path.iterdir() if f.is_file()]
