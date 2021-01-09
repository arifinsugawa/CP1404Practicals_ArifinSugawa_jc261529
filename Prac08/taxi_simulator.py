from prac_08.taxi import Taxi
from prac_08.silverServiceTaxi import SilverServiceTaxi 

def choose_taxi(taxis):
    for x , taxi in enumerate(taxis,0):
        print("{} - {}".format(x,taxi))
    if option < 0 or option > len(option):
        print("Invalid input") 
        return None
    else:
        option = int(input("Choose taxi: "))
        return taxis[option]

def drive_taxi(taxi):
    if taxi == None:
        print("Please select a taxi first")
        return 0
    else:
        distance = int(input("Drive how far? "))
        taxi.start_fare()
        taxi.drive(distance)
        print("Your {} trip cost you ${:.2f}".format(taxi.name, taxi.get_fare()))
        return taxi.get_fare()

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    option = ''
    bill = 0
    current_taxi = None
    print("Let`s drive!")

    while option != 'q':
        print("q)uit, c)hoose taxi, d)drive)")
        option = input(">>> ").lower()
        if option == 'q':
            print("Total trip cost: {:.2f}".format(bill))
        else:
            if option == 'c':
                current_taxi = choose_taxi(taxis)
            elif option == 'd':
                bill += drive_taxi(current_taxi) 
            print("Bill to date: {:.2f}".format(bill))

main()
