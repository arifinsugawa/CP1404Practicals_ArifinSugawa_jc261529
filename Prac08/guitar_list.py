from prac_08.guitar import Guitar
import csv 

def main():
    guitars = []
    in_file = open('guitars.csv', 'r', newline ='')
    reader = csv.reader(in_file)

    for row in reader:
        guitars.append(Guitar(row[0],int(row[1]),float(row[2])))

    guitars.sort()

    for guitar in guitars:
        print(guitar)

main()
