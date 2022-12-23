import inflect
import sys

# p = inflect.engine()
# # JOIN WORDS INTO A LIST:

# mylist = p.join(("apple", "banana", "carrot"))
# # "apple, banana, and carrot"

# mylist = p.join(("apple", "banana"))
# # "apple and banana"

# mylist = p.join(("apple", "banana", "carrot"), final_sep="")
# # "apple, banana and carrot"

def main():
    p = inflect.engine()
    list_of_names = []
    while True:
        try:
            name = input("Name: ")
            list_of_names.append(name)
        except EOFError:
            break
    if len(list_of_names) == 0:
        sys.exit()
    my_list = p.join(list_of_names)
    print(f"Adieu, adieu, to {my_list}")
if __name__=="__main__":
    main()