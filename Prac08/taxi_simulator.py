from Prac08.car import Car
from Prac08.taxi import Taxi
from Prac08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, s)elect taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's Get Our Driving Started!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Available Taxis: ")
            display_taxis(taxis)
            taxi_choice = int(input("Select Taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("This {} trip has cost you ${:.2f}".format(current_taxi.name,
                                                         trip_cost))
            total_bill += trip_cost
        else:
            print("Error")
        print("Total Bill To Date: ${:.2f}".format(total_bill))
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("Total cost of the trip: ${:.2f}".format(total_bill))
    print("Taxis Are Now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def run_tests():
    bus = Car("Datsun", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    bus.drive(55)
    print("fuel =", bus.fuel)
    print("odo = ", bus.odometer)
    print(bus)

    distance = int(input("How Far You Want To Drive? "))
    while distance > 0:
        travelled = bus.drive(distance)
        print("{} travelled {}".format(str(bus), travelled))
        distance = int(input("How Far You Want To Drive? "))

    t = Taxi("Prius 1", 100)
    print(t)
    t.drive(25)
    print(t, t.get_fare())
    t.start_fare()
    t.drive(40)
    print(t, t.get_fare())

    sst = SilverServiceTaxi("Limo", 100, 2)
    print(sst, sst.get_fare())
    sst.drive(10)
    print(sst, sst.get_fare())


main()