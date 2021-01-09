from prac_08.guitar import Guitar
import csv 

def display_guitars(guitars):
    guitars.sort()

    for guitar in guitars:
        print(guitar)


def main():
    guitars = []
    in_file = open('guitars.csv', 'r', newline ='')
    reader = csv.reader(in_file)

    for row in reader:
        guitars.append(Guitar(row[0],int(row[1]),float(row[2])))

    display_guitars(guitars)

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name,year,cost)
        print(new_guitar,"added.")
        guitars.append(new_guitar)
        name = input("Name: ")

    display_guitars(guitars)

    out_file = open('myguitars.csv','w')
    for guitar in guitars:
        print(guitar.csv_output(), file = out_file)

main()
