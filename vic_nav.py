def new_folder(folder_path):
    import os
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def find(directory_path):
    import os
    file_names = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))] 
    return sorted(file_names)
