def to_lower():
    text = str(input())
    if text.isupper() or text.isdigit():
        print(text.lower())

if __name__ == '__main__':
    to_lower()