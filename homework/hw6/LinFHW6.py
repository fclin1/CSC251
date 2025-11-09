"""
Author: Frank Lin
Email: fclin@ncsu.edu
Class: CSC 251 Fall 2025
Program: Homework 6
Purpose: Manages a car lot inventory system.
Bugs: None
Acknowledgements: Used Claude to help with main structure.
"""

from car import Car, Carlot
from menu import showMenu

def main():
    """Main program to manage car lot inventory"""
    
    print("*** Welcome to the Car Lot ***")
    
    # Get input filename and read data
    input_file = input("Enter name of car data input file: ")
    carlot = Carlot()    
    carlot.readFile(input_file)
    
    # Main menu loop
    loop = True
    while loop:
        choice = showMenu()

        # Show cars in inventory
        if choice == 's':
            carlot.showCars()
            
        # Add a new car
        elif choice == 'a':
            try:
                make = input("Enter the make of the car: ")
                model = input("Enter the model of the car: ")
                year = int(input("Enter the year the car was manufactured: "))
                price = float(input("Enter the price of the car: "))
                
                new_car = Car(make, model, year, price)
                carlot.addCar(new_car)
                
            except (ValueError, TypeError) as e:
                print(e)

        # Remove a car     
        elif choice == 'r':
            try:
                carlot.showCars()
                car_num = int(input(f"Enter car number(1 to {len(carlot.clist)}): "))
                
                carlot.removeCar(car_num)
                
            except (ValueError, TypeError) as e:
                print(e)

        # Change the price of a car        
        elif choice == 'c':
            try:
                carlot.showCars()
                car_num = int(input(f"Enter car number(1 to {len(carlot.clist)}): "))
                new_price = float(input("Enter new price: "))
                
                carlot.changePrice(car_num, new_price)
                
            except (ValueError, TypeError) as e:
                print(e)

        # Exit program and save inventory        
        elif choice == 'e':
            output_file = input("Enter name of car data output file: ")
            carlot.writeFile(output_file)
            loop = False

if __name__ == "__main__":
    main()