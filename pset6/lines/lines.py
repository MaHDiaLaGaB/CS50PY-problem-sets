import sys

def argv_error_checker():
    if len(sys.argv)==2:
        name = sys.argv[1]
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        sys.exit('Too few command-line arguments')
    return name

def lines():
    filename = argv_error_checker()
    if not filename.endswith('.py'):
        sys.exit('Not a Python file')
    try:
        with open(filename) as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                if line.lstrip().startswith('#'):
                    continue
                elif line.isspace():
                    continue
                else:
                    count += 1

        print(count)
    except FileNotFoundError:
        sys.exit('File does not exist')

def main():
    lines()

if __name__=="__main__":
    main()