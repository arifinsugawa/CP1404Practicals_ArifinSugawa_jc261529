from prac_06.guitar import Guitar

def test():
    gibson = Guitar("Gibson L-5 CES",1922,16035.40)
    another = Guitar("Another Guitar",2013)
    print("{} get_age() - Expected {}. Got {}".format(gibson.name,"98",gibson.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(another.name,"7",another.get_age()))
    print("{} is_vintage - Expected {}. Got {}".format(gibson.name,"True",gibson.is_vintage()))
    print("{} is_vintage - Expected {}. Got {}".format(another.name,"False",another.is_vintage()))

def main():
    guitars = []
    """
    #For testing 
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    """
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name,year,cost)
        print(new_guitar,"added.")
        guitars.append(new_guitar)
        name = input("Name: ")
    
    for i, guitar in enumerate(guitars, 0):
    #for i in range(len(guitars)):
        #guitar = guitars[i]
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        #print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
        #Another way to print the object 
        print("Guitar {}: {guitar.name: >20} ({guitar.year}), worth ${guitar.cost:10,.2f}{}".format(i+1,vintage_string,guitar=guitar))
main()
