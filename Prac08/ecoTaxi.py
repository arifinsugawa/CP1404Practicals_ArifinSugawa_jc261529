from prac_08.taxi import Taxi 

class EcoTaxi(Taxi):
    discount = 0.8
    
    def drive (self, distance):
        distance = super().drive(distance)
        self.fuel += distance/2
        return distance 

    def get_fare(self):
        return super().get_fare() * discount

    def __str__(self):
        return "{} with discount of {}%".format(super().__str__(), round((1 - self.discount) * 100),2)
