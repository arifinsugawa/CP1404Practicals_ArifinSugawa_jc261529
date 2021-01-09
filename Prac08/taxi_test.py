from prac_08.taxi import Taxi 

def main():
    new_taxi = Taxi('prius 1', 100) 
    new_taxi.drive(40)
    print(new_taxi)
    new_taxi.start_fare()
    print(new_taxi)

main()
