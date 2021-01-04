from person import Person

def load_from_CSV():
    persons = []
    try:
        csv_file_name = input("Enter csv file name : ") + ".csv"
        csv_file = open(csv_file_name,"r")
        for line in csv_file:
            line = line.strip()
            line = line.split(",")
            new_person = Person(line[0],line[1],line[2])
            persons.append(new_person)
    except IOError:
        print("{} is not found in current directory".format(csv_file_name))

    return persons 

def update_CSV(persons):
    csv_file_name = input("Enter csv file name : ") + ".csv"
    csv_file = open(csv_file_name,"w")

    for person in persons:
        print(person, file = csv_file)


def main():
    persons = load_from_CSV()
    for person in persons:
        print("{person.first_name} - {person.last_name} ({person.age})".format(person=person))

    first_name = input("First Name : ")
    while first_name != "":
        last_name = input("Last Name : ")
        age = int(input("Age : "))
        new_person = Person(first_name,last_name,age)
        persons.append(new_person)
        first_name = input("First Name : ")

    update_CSV(persons)

main()
