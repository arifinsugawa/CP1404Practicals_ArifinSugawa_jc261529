from prac_08.taxi import Taxi 


class SilverServiceTaxi(Taxi):
    flagFall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name,fuel) 
        self.price_per_km *= fanciness; 

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(),self.flagFall)

    def get_fare(self):
        return super().get_fare() + self.flagFall
