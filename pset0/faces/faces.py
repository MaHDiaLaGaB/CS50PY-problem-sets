def convert(face):
    if ":)" in face and ":(" in face:
        x = face.replace(':)', '\N{slightly smiling face}').replace(':(', '\N{slightly frowning face}')
        return x
    elif ":(" in face and ":)" not in face:
        return face.replace(':(', '\N{slightly frowning face}')

    elif ":)" in face and ":(" not in face:
        return face.replace(':)', '\N{slightly smiling face}')
    else:
        return face


def main():
    print(convert(str(input())))

if __name__ == "__main__":
    main()