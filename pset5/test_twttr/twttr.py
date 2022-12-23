def main():
    print(shorten(str(input())))


def shorten(word):

    twttr = list()
    for y in word:
        if y not in ["a", "e", "i", "o", "u"]:
            twttr.append(y)
    return "".join(twttr)


if __name__ == "__main__":
    main()