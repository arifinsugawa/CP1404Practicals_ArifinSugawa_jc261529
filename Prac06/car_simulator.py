from prac_06.car import Car

def num_validation(user_input,message,prompt):
    while user_input < 0:
        print("{} must be >= 0".format(message))
        user_input = int(input(prompt))
    return user_input

def drive(car):
    prompt = "How many km do you wish to drive? "
    distance = num_validation(int(input(prompt)),"Distance",prompt) 
    actual_distance = car.drive(distance)
    drive_str = "."
    if actual_distance != distance:
        drive_str = " and ran out of fuel."
    print("The car drove {}km{}".format(actual_distance,drive_str))

def refuel(car):
    prompt = "How many units of fuel do you want to add to the car? "
    fuel = num_validation(int(input(prompt)), "Fuel", prompt)
    car.add_fuel(fuel)
    print("Added {} units of fuel.".format(fuel))

def menu():
    print("Menu:")
    print("d) drive")
    print("r) refuel")
    print("q) quit")

def main():
    print("Let`s drive!")
    name = input("Enter your car name: ")
    car = Car(name,100)
    print("{car.name}, fuel={car.fuel}, odo={car.odometer}".format(car=car))
    menu()
    user_choice = input("Enter your choice: ").lower()
    while user_choice != "q":
        if user_choice == "d":
            drive(car)
        elif user_choice == "r":
            refuel(car)
        else:
            print("Invalid choice")
        print("{car.name}, fuel={car.fuel}, odo={car.odometer}".format(car=car))
        menu()
        user_choice = input("Enter your choice: ").lower()

    print("Good bye {}`s driver".format(car.name))

main()
