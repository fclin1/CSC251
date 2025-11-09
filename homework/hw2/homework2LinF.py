"""
Author: Frank Lin
Email: fclin@ncsu.edu
Class: CSC 251 Fall 2025
Program: Homework 2
Purpose: Return fabric yardage and cost for pillowcase
Bugs: None
Acknowledgements: None
"""

import math

MAX_LENGTH = 108
INCHES_PER_YARD = 36

def get_pillowcase_length():
    """
    Prompts user for pillowcase length with input validation.
    """
    length = int(input('Enter the length of the pillowcase in inches (0-108"): '))
    while length < 0 or length > MAX_LENGTH:
        length = int(input('Invalid input for length. Re-enter the length in inches (0-108"): '))
    return length


def get_fabric_price():
    """
    Prompts user for fabric price per yard with input validation.
    """
    price = float(input("Enter the price per yard: $"))
    while price < 0:
        price = float(input("Invalid input for price. Re-enter the price per yard: $"))
    return price


def calculate_fabric_yards(finished_length):
    """
    Calculates the minimum fabric needed in yards.
    """
    # Add 1 inch for the two 1/2 inch seam allowances
    fabric_length_needed = finished_length + 1
    
    # Convert inches to yards
    yards_needed = fabric_length_needed / INCHES_PER_YARD
    
    # Round up to nearest 1/8 yard
    eighths = math.ceil(yards_needed * 8)
    
    return eighths / 8.0


def gcd(a, b):
    """
    Calculates the greatest common divisor of two numbers. Used for reducing fractions to lowest terms.
    """
    while b:
        a, b = b, a % b
    return a


def format_yards(yards):
    """
    Formats the yard measurement as a string with proper fraction display.
    """
    # Convert to eighths
    eighths = int(yards * 8)
    
    # Separate into whole yards and fractional part
    whole_yards = eighths // 8
    remaining_eighths = eighths % 8
    
    if remaining_eighths == 0: # Integer yards only
        if whole_yards == 1:
            return "1 yard"
        else:
            return f"{whole_yards} yards"
    else: # Reduce fraction to lowest terms
        divisor = gcd(remaining_eighths, 8)
        numerator = remaining_eighths // divisor
        denominator = 8 // divisor
        
        if whole_yards == 0: # Less than 1 yard
            return f"{numerator}/{denominator} yard"
        else: # Mixed number format
            if yards <= 1.125:  # Up to 1-1/8 yards is singular
                return f"{whole_yards}-{numerator}/{denominator} yards"
            else:
                return f"{whole_yards}-{numerator}/{denominator} yards"


# Caluclate cost with lambda function
calculate_cost = lambda yards, price_per_yard: round(yards * price_per_yard, 2)


def main():
    """
    Main function.
    """
    # Get user inputs
    pillowcase_length = get_pillowcase_length()
    fabric_price = get_fabric_price()
    
    # Calculate fabric needed
    fabric_yards = calculate_fabric_yards(pillowcase_length)
    
    # Calculate cost
    total_cost = calculate_cost(fabric_yards, fabric_price)
    
    # Format and display results
    fabric_display = format_yards(fabric_yards)
    print(f"Minimum fabric needed: {fabric_display}")
    print(f"Fabric cost: ${total_cost:.2f}")


if __name__ == "__main__":
    main()