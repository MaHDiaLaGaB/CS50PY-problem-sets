import random

class BadError(Exception):
    pass

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            pass
    num = random.randint(1, n)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > num:
                print("Too large!")
            elif guess < num:
                print("Too small!")
            elif guess == num:
                print("Just right!")
                break
        except ValueError:
            pass

if __name__=="__main__":
    main()
