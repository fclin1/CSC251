"""
Car and Carlot class definitions
"""

import sys

class Car:
    """Represents a car with make, model, year, and price."""

    def __init__(self, mk, mo, yr, pr):
        """
        Initialize a Car instance with validation
        Parameters:
            mk (str): Make of the car
            mo (str): Model of the car
            yr (int): Year of manufacture
            pr (int): Price of the car
        """
        self.__make = mk
        self.__model = mo
        self.__year = yr if yr >= 1900 else 2025
        self.__price = round(pr) if pr >= 0 else 25000

    @property
    def make(self):
        """Accessor for make"""
        return self.__make
    
    @property
    def model(self):
        """Accesor for model"""
        return self.__model
    
    @property
    def year(self):
        """Accessor for year"""
        return self.__year
    
    @property
    def price(self):
        """Accessor for price"""
        return self.__price
    
    @price.setter
    def price(self, p):
        """Mutator for price"""
        self.__price = round(p) if p >= 0 else 25000

    def __str__(self):
        """String representation of the Car"""
        return f"{self.__year} {self.__make} {self.__model} ${self.__price:,}"

class Carlot:
    """Represents a collection of Car instances"""

    def __init__(self):
        """Initialize an empty Carlot"""
        self.__clist = []

    @property
    def clist(self):
        """Accessor for the car list"""
        return self.__clist
    
    def readFile(self, file1):
        """
        Read car data from a file and populate the car list
        Parameters:
            file1 (str): Path to the input file
        """
        try:
            with open(file1, 'r') as file:
                for line in file:
                    parts = line.strip().split(" ")
                    if len(parts) >= 4:
                        mk, mo, yr, pr = parts
                        car = Car(mk, mo, int(yr), int(pr))
                        self.__clist.append(car)
        except IOError as e:
            print(e)
            sys.exit(1)

    def showCars(self):
        """Display all cars in the car list"""
        for car in self.__clist:
            print("Car Lot Inventory")
            print("-" * 30)
            for i in range(len(self.__clist)):
                print(f"{i} {self.__clist[i]}")

    def addCar(self, carObj):
        """
        Add a new car to inventory
        Parameters:
            carObj (Car): Car instance to add
        """
        self.__clist.append(carObj)
        print(f"{carObj.year} {carObj.make} {carObj.model} added.")

    def removeCar(self, n):
        """
        Remove a car from inventory by its index
        Parameters:
            n (int): Index of the car to remove, starts from 1
            """
        if 1 <= n <= len(self.__clist):
            car = self.__clist[n - 1]
            print(f"{car.year} {car.make} {car.model} removed.")
            del self.__clist[n - 1]
        else:
            print("Invalid car number.")

    def changePrice(self, n, newp):
        """
        Change the price of a car by its index
        Parameters:
            n (int): Index of the car to change, starts from 1
            newp (int): New price to set
        """
        if 1 <= n <= len(self.__clist):
            car = self.__clist[n - 1]
            car.price = newp
            print(f"{car.year} {car.make} {car.model} price changed to ${car.price:,}.")
        else:
            print("Invalid car number.")

    def writeFile(self, file2):
        """
        Write the current car inventory to a file
        Parameters:
            file2 (str): Path to the output file
        """
        with open(file2, 'w') as file:
            for car in self.__clist:
                file.write(f"{car.make} {car.model} {car.year} {car.price}\n")
        print(f"Inventory written to {file2}.")