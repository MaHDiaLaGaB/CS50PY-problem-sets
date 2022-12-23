
def ask_user():
    x = True
    due = 50
    while x:

        amount = int(input("Insert Coin: "))
        if amount in [25,10, 5]:
            if amount <= due:
                due = due - amount
                if due != 0:
                    print(f"Amount due:{due}")
                else:
                    print(f"Change owed: {due}")
                    x = False
            else:
                print(f"Amount Owed:{10}")
                x = False
        else:
            print(f"Amount due:{due}")


def main():
    ask_user()


if __name__ == "__main__":
    main()
