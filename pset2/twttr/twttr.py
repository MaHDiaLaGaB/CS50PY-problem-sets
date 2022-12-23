def remove():
    text = list(input("Input: "))
    twttr = list()
    for y in text:
        if y not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            twttr.append(y)
    return "".join(twttr)

def main():
    print(remove())

if __name__ == "__main__":
    main()