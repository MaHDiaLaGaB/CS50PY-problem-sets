def main():
    text = input("camelCase: ")
    x = camel(text)
    print(x)


def camel(text):
    my_list = list(text)
    sec_list = list()
    for i in range(len(my_list)):
        if my_list[i].isupper():
            sec_list.append("_")
            r = my_list[i].lower()
            sec_list.append(r)
        else:
            sec_list.append(my_list[i])
    return "".join(map(str, sec_list))


if __name__ == "__main__":
    main()
