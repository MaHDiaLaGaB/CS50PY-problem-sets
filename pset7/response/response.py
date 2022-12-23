import validators

def match(s):
    match = validators.email(s)
    # Check if a match was found
    if match:
        return "Valid"
    else:
        return "Invalid"

def main():
    print(match(str(input("What's your email address? "))))

if __name__=="__main__":
    main()
