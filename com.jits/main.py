import argparse
import os
from gui import gui_get_folder
from constants import movie_extensions

def main():

    cli_args = parse_arguments()
    directory = get_directory(cli_args)
    video_files = get_movies_from_folder(directory)

    print(directory)
    print(cli_args)
    print(video_files)

def get_directory(args):
    return gui_get_folder(args.directory) if args.gui else args.directory


def parse_arguments():
    parser = argparse.ArgumentParser()
    #TODO: should set required=True
    parser.add_argument('-d', '--directory', type=str, help="Directory to search video movies/series in")
    parser.add_argument('-r', '--recursive', action="store_true", help="wheter to recursively search all subfolders")
    parser.add_argument('-g', '--gui', action="store_true", help="wheter to use GUI to select a folder, if used together with -d then specified folder should be the one that is open by default")
    return parser.parse_args() 
    print(args.directory)
    print(args.recursive)

#TODO can it be faster?
def get_movies_from_folder(directory, extensions_list=movie_extensions, recursive=True):  
    file_list = []

    if not recursive:
        for file in os.listdir(directory):
            if file.endswith(tuple(extensions_list)):
                file_list.append(os.path.join(dir_root, file))
        return file_list

    for (dir_root, dir_names, file_names) in os.walk(directory):
        for file in file_names:
            if file.endswith(tuple(extensions_list)):
                file_list.append(os.path.join(dir_root, file))
    return file_list

if __name__ == '__main__':
    main()
