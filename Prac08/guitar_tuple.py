import csv 

def main():
    guitars = []
    in_file = open('guitars.csv','r', newline ='')
    reader = csv.reader(in_file)
    for row in reader:
        guitars.append(tuple(row))

    for guitar in guitars:
        print(guitar)

main()
