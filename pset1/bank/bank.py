def give_me_money(n):
    if "hello" in n:
        return '$0'
    elif n[0] == "h":
        return '$20'
    else:
        return '$100'


def main():
    x = input("Greeting: ")
    y = x.lower()
    j = "".join(y.split())
    print(give_me_money(j))


if __name__ == "__main__":
    main()
