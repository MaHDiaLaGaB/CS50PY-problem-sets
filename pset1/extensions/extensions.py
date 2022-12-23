
SUFF = ['jpg', 'jpeg', 'gif', 'png', 'pdf', 'zip', 'txt']
MM = ['text/plain', 'application', 'image']


def extenstion(n):
    for x in SUFF:
        if x in n:
            if x in SUFF[:2]:
                return f"{MM[2]}/jpeg"
            elif x in SUFF[-1:]:
                return "text/plain"
            elif x in SUFF[-5:-3]:
                return f"{MM[2]}/{x}"
            elif x in SUFF[-3: -1]:
                return f'{MM[1]}/{x}'
    for x in SUFF:
        if x not in n:
            return "application/octet-stream"


def main():
    n = input('File name: ')
    y = n.lower()
    # print(SUFF[-3:-1])
    print(extenstion(y))


if __name__ == "__main__":
    main()
