def print_menu():
    print("A - Enter a new name & address")
    print("B - Change an address for an existing entry")
    print("C - Print the address for a name entered")
    print("Q - Quit")

def input_address(address_dict):
    name = input("Enter a name : ")
    address = input("Enter address : ")
    if name not in address_dict:
        address_dict[name] = address

def update_address(address_dict):
    name = input("Enter a name : ")
    if name not in address_dict:
        print("Name not registered")
    else:
        address = input("Enter new address : ")
        address_dict[name] = address

def print_address(address_dict):
    name = input("Enter a name : ")
    if name not in address_dict:
        print("Name not registered")
    else:
        print("{}`s address is {}".format(name,address_dict[name]))

def load_from_CSV():
    address_dict = {}
    try:
        csv_file_name = input("Enter csv file name : ") + ".csv"
        csv_file = open(csv_file_name,"r")
        for line in csv_file:
            line = line.strip()
            line = line.split(",")
            address_dict[line[0]] = line[1]
    except IOError:
        print("{} is not found in current directory".format(csv_file_name))

    return address_dict

def update_CSV(address_dict):
    csv_file_name = input("Enter csv file name : ") + ".csv"
    csv_file = open(csv_file_name,"w")

    for name,address in address_dict.items():
        entry = name + "," + address
        print(entry, file = csv_file)


def main():
    address_dict = load_from_CSV()
    for name,address in address_dict.items():
        print("{} - {}".format(name,address))

    print_menu()
    user_choice = input("Enter Choice : ").upper()
    while user_choice != "Q":
        if user_choice == "A" :
            input_address(address_dict) 
        elif user_choice == "B":
            update_address(address_dict)
        elif user_choice == "C":
            print_address(address_dict)
        
        print_menu()
        user_choice = input("Enter Choice : ").upper()
    
    update_CSV(address_dict)

main()
