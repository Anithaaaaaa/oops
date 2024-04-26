#AbstractVehicle.py (Abstract Class File):

from abc import ABC, abstractmethod

class AbstractVehicle(ABC):
    def __init__(self, color, num_tyres, gears):
        self.color = color
        self.num_tyres = num_tyres
        self.gears = gears

    @abstractmethod
    def display_details(self):
        pass

#Vehicle.py (Where Abstraction Happens):

from AbstractVehicle import AbstractVehicle

class Bike(AbstractVehicle):
    def display_details(self):
        print("Bike Details:")
        print("Color:", self.color)
        print("Number of Tyres:", self.num_tyres)
        print("Gears:", self.gears)

class Car(AbstractVehicle):
    def display_details(self):
        print("Car Details:")
        print("Color:", self.color)
        print("Number of Tyres:", self.num_tyres)
        print("Gears:", self.gears)

class Scooty(AbstractVehicle):
    def display_details(self):
        print("Scooty Details:")
        print("Color:", self.color)
        print("Number of Tyres:", self.num_tyres)
        print("Gears:", self.gears)


#Main.py (Main File Where the Calling of Methods Happens):
from Vehicle import Bike, Car, Scooty

def main():
    bike = Bike("Red", 2, 5)
    car = Car("Blue", 4, 6)
    scooty = Scooty("Green", 2, 4)

    bike.display_details()
    print("\n")
    car.display_details()
    print("\n")
    scooty.display_details()

if __name__ == "__main__":
    main()


