import csv
import sys
from tabulate import tabulate


def read_and_show():
    if not sys.argv[1].endswith(".csv"):
        sys.exit('wrong prifix')

    if len(sys.argv) == 2:
        my_list = []
        try:
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for row in reader:
                    my_list.append(row)
                return tabulate(my_list[1:], headers=my_list[0], tablefmt='grid')

        except FileNotFoundError:
            sys.exit('File does not exist')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')

    else:
        sys.exit('Too few command-line arguments')


def main():
    minu = read_and_show()
    print(minu)

if __name__=="__main__":
    main()
