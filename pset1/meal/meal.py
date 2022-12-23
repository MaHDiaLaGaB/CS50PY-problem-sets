def main():
    time = input("What time is it: ")
    print(convert(time))


def convert(time):

    hours, minutes = time.split(":")
    if 00 <= int(hours) <= 24 and 00 <= int(minutes) <= 60:
        x = hours
        y = minutes
        num = float(x+"."+y)
    else:
        return "wrong input"

    if 6.0 <= num < 12.0:
        return "breakfast time"
    elif 12.0 <= num <= 18.0:
        return "lunch time"
    elif 18.0 < num <= 20.0:
        return "dinner time"


if __name__ == "__main__":
    main()
