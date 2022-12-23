from pyfiglet import Figlet
import sys
import random



def main():
    n = len(sys.argv)
    args_list = ['-f', '--font']
    f = Figlet()

    fonts = f.getFonts()

    if 1 < n < 3:
        sys.exit("wrong arg")

    if n == 3:
        if sys.argv[1] not in args_list:
            sys.exit("wrong arg")


    if n == 1:
        rand_font = random.randint(0, len(fonts))
        f.setFont(font=fonts[rand_font])
    elif n == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        arg_2 = sys.argv[2]
        f.setFont(font=arg_2)
    else:
        sys.exit()
    text = str(input("input: "))
    print(f.renderText(text))

if __name__=="__main__":
    main()
