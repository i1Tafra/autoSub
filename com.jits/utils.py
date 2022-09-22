from tkinter.filedialog import askdirectory
import os


def get_folder():
    return askdirectory(title='Select Folder')


def get_files_from_folder(directory=get_folder(), include_directory_in_name=False):
    file_list = []
    for (dir_path, dir_names, file_names) in os.walk(directory):
        if include_directory_in_name:
            file_list += [os.path.join(dir_path, file) for file in file_names]
        else:
            file_list += [os.path.join(file) for file in file_names]
    return file_list
