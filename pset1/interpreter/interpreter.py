
def interpreter(a: str, b: str, c: str):
    my_dict = {
        "+": int(a)+int(c),
        "-": int(a)-int(c),
        "/": int(a)/int(c),
        "*": int(a)*int(c)
    }
    return my_dict[b]


def main():
    a, b, c = input("Expression: ").split()
    x = (interpreter(a, b, c))
    print("{:.1f}".format(x))


if __name__ == "__main__":
    main()
