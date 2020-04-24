from Prac06.guitar import Guitar


def main():
    guitars = []

    print("Guitars List!")
    name = input("Enter Guitar Name: ")
    while name != "":
        year = int(input("Enter its Year: "))
        cost = float(input("Enter its Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "Guitar Added!")
        name = input("Enter Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:  # lists, strings and other collections are False when empty, True when non-empty
        # In order for sorting to work on Guitar objects,
        # at least the __lt__ method must be defined in Guitar class
        guitars.sort()
        print("My Guitars List:")
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}\
             {2}".format(i + 1, guitar, vintage_string))
    else:
        print("No guitars are found in your list :( Do go and buy!")


main()