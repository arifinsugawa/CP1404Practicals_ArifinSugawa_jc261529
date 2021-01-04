from datetime import date 

def input_birthdays():
    birthday_dict = {}
    for i in range(5):
        name = input("Enter name :")
        birthday = input("Enter birthday(dd/mm/yyyy) : ")
        birthday = birthday.split("/")
        birthday = [int(x) for x in birthday]
        birthday_dict[name] = birthday
    return birthday_dict

def display_age(birthday_dict):
    for name,birthday in birthday_dict.items():
        b_date = date(birthday[-1],birthday[-2],birthday[-3])
        today = date.today()
        age = today.year - b_date.year;
        if today.month < b_date.month and today.date < b_date.day:
            age -= 1
        print('{} - {}'.format(name,age))

def combine_list(names,dates_of_birth):
    birthday_dict = {}
    for x in range(len(names)):
        birthday_dict[names[x]] = dates_of_birth[x]
    return birthday_dict

def main():
    birthday_dict = input_birthdays()
    display_age(birthday_dict)
    names = ["Jack", "Jill", "Harry"]
    dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
    birthday_dict = combine_list(names,dates_of_birth)
    display_age(birthday_dict)


main()
