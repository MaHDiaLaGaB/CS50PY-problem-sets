def main():
    frac = input("Fraction: ")
    x = convert(frac)
    print(gauge(x))


def convert(fraction):
     while True:
        try:
            a, b = fraction.split('/', 3)
            result = int(a)/int(b)
            if result <= 1:
                return round(result*100)
        except ZeroDivisionError:
            raise
        except ValueError:
            raise


def gauge(percentage):
    if percentage >= 100:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()