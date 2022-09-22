from utils import *
import argparse

def main():
    list_of_files = get_movies_from_folder()
    print(list_of_files)


def parse_arguments():
    parser = argparse.ArgumentParser()
    #TODO: should set required=True
    parser.add_argument('-d', '--directory', type=str, help="Directory to search video movies/series in")
    parser.add_argument('-r', '--recursive', action="store_true", help="wheter to recursively search all subfolders")
    args = parser.parse_args()
    print(args.directory)
    print(args.recursive)


if __name__ == '__main__':
    main()
