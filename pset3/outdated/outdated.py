import datetime

class ErrorDate(Exception):
    pass

MONTHS = {"January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12"}

# 9/8/1990 or sep 9, 1990 <-- accepted
def clean_string(text):
    no_space = []
    if len(text) == 1:
        raise ErrorDate()

    if ',' in text[1]:
        for word in text:
            no_space.append(word.replace(",", ""))
    else:
        raise ErrorDate()

    if no_space[0].isdigit():
        raise ErrorDate()
    else:
        for k, v in MONTHS.items():
            if k == no_space[0]:
                no_space[0] = v
    return '/'.join(no_space)


def create():
    while True:
        try:
            unorder_date = input("Date: ").split()
            date_0 = '/'.join(unorder_date)
            date_final = datetime.datetime.strptime(date_0, "%m/%d/%Y")
            return date_final.strftime("%Y-%m-%d")

        except (TypeError, ValueError):
            try:
                date_1 = clean_string(unorder_date)
                date_2 = datetime.datetime.strptime(date_1, "%m/%d/%Y")
                return date_2.strftime("%Y-%m-%d")
            except (ErrorDate, ValueError):
                pass


def main():
    print(create())

if __name__=="__main__":
    main()