import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    patt = r'\bum\b'
    string = s.split(' ')
    count = 0
    for word in string:
        # Split the text into a list of words
        regex = re.compile(patt, re.IGNORECASE)
        find_it = regex.search(word)
        if find_it:
            count += 1
    # Return the final count
    return count


if __name__ == "__main__":
    main()