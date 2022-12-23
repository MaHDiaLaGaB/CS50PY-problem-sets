import random

levels = [1, 2, 3]

def main():
    my_level = get_level()
    generate_integer(my_level)


def get_level():
    while True:
        try:
            n = int(input("Select level: "))
            if n not in levels:
                raise ValueError()
            break
        except ValueError:
            pass
    return n


def generate_integer(n):
    print(n)
    score = 0
    if n == 1:
        start = 0
        to = 9
    elif n == 2:
        start = 10
        to = 99
    elif n == 3:
        start = 100
        to = 999

    for i in range(10):
        ok = 0
        x = random.randint(start, to)
        y = random.randint(start, to)
        for j in range(3):
            print(f'{x} + {y} =')
            s = int(input())
            if(s == x+y):
                ok = 1
                score += 1
                break
            else:
                print("EEE")
        if ok == 0:
            print(x+y)
    print(score)


if __name__ == "__main__":
    main()