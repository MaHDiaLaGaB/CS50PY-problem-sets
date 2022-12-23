
def handle():
    while True:
        try:
            inp = input("Fraction: ")
            a, b = inp.split('/', 3)
            result = int(a)/int(b)
            if result <= 1:
                return round(result*100)
        except ZeroDivisionError:
            pass
        except ValueError:
            pass

def main():
    result = handle()
    if result >= 99:
        print("F")
    elif result <= 1:
        print("E")
    else:
        print(f"{result}%")

if __name__=="__main__":
    main()