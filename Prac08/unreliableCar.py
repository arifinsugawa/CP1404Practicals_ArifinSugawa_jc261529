#from prac_088.car import Car 
from prac_08.car import Car 
import random  

class UnreliableCar(Car):
    def __init__(self, name , fuel, reliability):
        super().__init__(name,fuel)
        self.reliability = reliability

    def drive(self,distance):
        if random.randint(0,100) < self.reliability:
            return 0
        else: 
            return super().drive(distance) 
