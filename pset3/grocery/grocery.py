def grocery():
    basket = dict()
    while True:
        try:
            order = str(input()).upper()
            if order in basket:
                basket[order] += 1
            else:
                basket[order] = 1

        except EOFError:
            for value in sorted(basket.keys()):
                print(basket[value], value)
            break

def main():
    grocery()

if __name__=="__main__":
    main()