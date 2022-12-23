import emoji

def create_emoji():
    e = str(input("Input: "))
    print(emoji.emojize(f"{e}"))

def main():
   create_emoji()

if __name__=="__main__":
    main()