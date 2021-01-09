from silverServiceTaxi import SilverServiceTaxi

def main():
    new_car = SilverServiceTaxi('prius 1', 100, 2) 
    print(new_car)
    new_car.drive(18)
    print("{:.2f}".format(new_car.get_fare()))

main() 
