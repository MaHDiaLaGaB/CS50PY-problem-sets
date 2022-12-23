import datetime
import sys
import inflect

p = inflect.engine()

def main():
    date_of_birth = input("Date of Birth: ")
    print(convert(date_of_birth))


def convert(date_of_birth):
    today = datetime.date.today()
    try:
        the_past = datetime.date.fromisoformat(date_of_birth)
        age = today - the_past
        age_in_minutes = age.days*60*24
        age_in_minutes = p.number_to_words(age_in_minutes, andword="")
        cap_age_in_minutes = age_in_minutes.capitalize()
        return (cap_age_in_minutes + ' minutes')
    except:
        sys.exit(1)


if __name__=="__main__":
    main()