
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', type=str, help="Directory to search video movies/series in") #TODO: should set required=True
    parser.add_argument('-r', '--recursive', action="store_true", help="wheter to recursively search all subfolders")

    args = parser.parse_args()

    print(args.directory)
    print(args.recursive)


def main():
    parse_arguments()

if __name__ == '__main__':
    main()
