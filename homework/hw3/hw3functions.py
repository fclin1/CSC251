"""
CSC 251
Homework 3
This module contains functions for input validation, conversion, and output formatting.
"""

CM_PER_INCH = 2.54
MIN_INCHES = 0
MAX_INCHES = 11
MIN_FEET = 0
MAX_FEET = 20


def inputVal(start_or_end):
    """
    Prompts the user for a height in feet and inches, validates values, and returns as a tuple.
    """
    valid_feet = False
    feet = 0
    while not valid_feet:
        feet_input = input(f"Enter the {start_or_end} height in feet and inches. First enter the number of feet: ")
        feet = round(float(feet_input))
        if MIN_FEET <= feet <= MAX_FEET:
            valid_feet = True
        else:
            print(f"Please enter a value between {MIN_FEET} and {MAX_FEET} feet.")
    
    valid_inches = False
    inches = 0
    while not valid_inches:
        inches_input = input("Enter the number of inches: ")
        inches = round(float(inches_input))
        if MIN_INCHES <= inches <= MAX_INCHES:
            valid_inches = True
        else:
            print(f"Please enter a value between {MIN_INCHES} and {MAX_INCHES} inches.")
    
    return feet, inches


def convert(feet, inches):
    """
    Converts height from feet and inches to centimeters.
    """
    total_inches = feet * 12 + inches
    centimeters = total_inches * CM_PER_INCH
    return centimeters


def tableRow(feet, inches, cm):
    """
    Prints out a single formatted row of values for the table.
    """
    print(f"{feet:>10} | {inches:>10} || {cm:>10.2f}")


def compareHeights(start_feet, start_inches, end_feet, end_inches):
    """
    Compares two heights to determine if the ending height is greater than or equal to starting height.
    """
    start_total_inches = start_feet * 12 + start_inches
    end_total_inches = end_feet * 12 + end_inches
    return end_total_inches >= start_total_inches