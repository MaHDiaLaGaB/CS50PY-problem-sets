import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if match:
        parts = match.groups()
        old_format = {'hour': parts[1], 'minuts': parts[2], 'NOD': parts[3]}
        new_format = {'hour': parts[5], 'minuts': parts[6], 'NOD': parts[7]}
        if int(old_format['hour']) > 12 or int(new_format['hour']) > 12:
            raise ValueError
        first_time = convert_format(**old_format)
        second_time = convert_format(**new_format)
        return f"{first_time} to {second_time}"
    else:
        raise ValueError


def convert_format(**format):
    if format['NOD'] == "PM":
        if int(format['hour']) == 12:
            hour = 12
        else:
            hour = int(format['hour']) + 12
    else:
        if int(format['hour']) == 12:
            hour = 0
        else:
            hour = int(format['hour'])
    if format['minuts'] == None:
        minute = ":00"
        time = f"{hour:02}" + minute
    else:
        time = f"{hour:02}" + ":" + format['minuts']
    return time

if __name__ == "__main__":
    main()