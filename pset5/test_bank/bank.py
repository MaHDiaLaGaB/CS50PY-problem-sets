def main():
    x = value(input("greeting: "))
    print(f'${x}')


def value(greeting):
    y = greeting.lower().split()

    if "hello" in y:
        return 0
    elif "h" in y[1]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
