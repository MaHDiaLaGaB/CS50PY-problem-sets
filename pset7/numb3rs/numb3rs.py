import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
     # Regular Expression for IPv4 Version IP Address
    m = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    return bool(m) and all(map(lambda n: 0 <= int(n) <= 255, m.groups()))


if __name__ == "__main__":
    main()
