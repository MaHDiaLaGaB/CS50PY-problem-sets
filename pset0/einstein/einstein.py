SPEED = 300000000 ** 2

def energy(m):
    e = m * SPEED
    return e

def main():
    m = int(input("m: "))
    print(energy(m))

if __name__ == "__main__":
    main()