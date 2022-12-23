def forty_two(n):

    if n.lower() == "fortytwo" or n == "42":
        return "Yes"
    else:
        return "No"


def main():
    n = input(
        "What is the answer to the Great Question of Life, the Universe and Everything? ")
    if "42" in n:
        x = "".join(n.split())
        print(forty_two(x))
    else:
        y = n.replace("-", " ")
        g = "".join(y.split())
        print(forty_two(g))


if __name__ == "__main__":
    main()
