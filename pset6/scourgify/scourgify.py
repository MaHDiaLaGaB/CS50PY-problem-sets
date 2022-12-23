import sys
import csv


def argv_checker():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    else:
        return True


def clean_data():
    file_1 = list()
    file_2 = list()
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file, fieldnames=["name","house"])
            for row in reader:
                file_1.append({'name':row['name'], 'house':row['house']})
            for name in range(len(file_1)):
                a = file_1[name]['name']

                if ',' in a:
                    last_name, first_name = a.split(', ')
                else:
                    continue
                file_2.append({'first_name': first_name, 'last_name': last_name, 'house':file_1[name]['house']})

        with open(sys.argv[2], 'w') as second_file:
            field_names = ['first', 'last', 'house']
            writer = csv.DictWriter(second_file, fieldnames=field_names)
            writer.writeheader()
            for i in range(len(file_2)):
                writer.writerow({
                    'first': file_2[i]['first_name'],
                    'last': file_2[i]['last_name'],
                    'house':file_2[i]['house']
                })
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')

def main():
    if argv_checker():
        clean_data()

if __name__=="__main__":
    main()
