from tkinter.filedialog import askdirectory
from constants import *
import os


def get_folder():
    return askdirectory(title='Select Folder')


def get_movies_from_folder(directory=get_folder(), extensions_list=movie_extensions):
    file_list = []
    for (dir_path, dir_names, file_names) in os.walk(directory):
        for file in file_names:
            if file.endswith(tuple(extensions_list)):
                file_list.append(file)
    return file_list
