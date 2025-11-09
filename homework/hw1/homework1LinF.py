"""
Author: Frank Lin
Email: fclin@ncsu.edu
Class: CSC 251 Fall 2025
Program: Homework 1
Purpose: Returns change with least number of coins
Bugs: None
Acknowledgements: None
"""

# Coin value constants
DOLLAR = 1.00
HALF_DOLLAR = 0.50
QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

# Constants for table formatting
TABLE_WIDTH = 26
LEFT_COLUMN_WIDTH = 16
RIGHT_COLUMN_WIDTH = 10

# User input for total change
change = float(input("Enter the total amount of money: $"))
subtot = change

# Calculate number of each coin type
dollars = subtot // DOLLAR
subtot -= dollars * DOLLAR

halves = subtot // HALF_DOLLAR
subtot -= halves * HALF_DOLLAR

quarters = subtot // QUARTER
subtot -= quarters * QUARTER

dimes = subtot // DIME
subtot -= dimes * DIME

nickels = subtot // NICKEL
subtot -= nickels * NICKEL

subtot = round(subtot, 2) # Round to avoid floating point issues
pennies = subtot // PENNY

# Total number of coins
coins = dollars + halves + quarters + dimes + nickels + pennies

# Print formatted output
print(f"Fewest coins for ${change:.2f}")
print("=" * TABLE_WIDTH)
print(f"{'Coin Type':<{LEFT_COLUMN_WIDTH}}{'Number':>{RIGHT_COLUMN_WIDTH}}")
print(f"{'Dollars':<{LEFT_COLUMN_WIDTH}}{int(dollars):>{RIGHT_COLUMN_WIDTH}}")
print(f"{'Half-Dollars':<{LEFT_COLUMN_WIDTH}}{int(halves):>{RIGHT_COLUMN_WIDTH}}")
print(f"{'Quarters':<{LEFT_COLUMN_WIDTH}}{int(quarters):>{RIGHT_COLUMN_WIDTH}}")
print(f"{'Dimes':<{LEFT_COLUMN_WIDTH}}{int(dimes):>{RIGHT_COLUMN_WIDTH}}")
print(f"{'Nickels':<{LEFT_COLUMN_WIDTH}}{int(nickels):>{RIGHT_COLUMN_WIDTH}}")
print(f"{'Pennies':<{LEFT_COLUMN_WIDTH}}{int(pennies):>{RIGHT_COLUMN_WIDTH}}")
print("-" * TABLE_WIDTH)
print(f"{'Total Coins':<{LEFT_COLUMN_WIDTH}}{int(coins):>{RIGHT_COLUMN_WIDTH}}")