def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s) -> bool:
    # 1
    if len(s) < 2 or len(s) > 6:
        return False

    # 2
    x = 0
    while x < len(s):
        if s[x].isalpha() == False:
            if s[x] == '0' and s[x] != s[-1]:
                return False
        x += 1

    # 3
    if not s[:2].isalpha():
        return False

    # 4
    for y in s:
        if y in [' ', '?', '!', ',', '.']:
            return False

    return True

if __name__ == "__main__":
    main()
