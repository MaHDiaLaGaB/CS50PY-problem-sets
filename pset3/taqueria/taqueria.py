
SWITCH = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }


def get_order():
    total = 0
    while True:
        try:
            order = str(input("Item: ")).title()
            if order in SWITCH:
                total += SWITCH[order]
        except EOFError:
            break
        finally:
            formated = "{:.2f}".format(total)
            print(f"Total: ${formated}")


def main():
    get_order()


if __name__=="__main__":
    main()
