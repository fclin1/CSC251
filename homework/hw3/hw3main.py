"""
Author: Frank Lin
Email: fclin@ncsu.edu
Class: CSC 251 Fall 2025
Program: Homework 3
Purpose: Outputs a height conversion table.
Bugs: None
Acknowledgements: None
"""

import hw3functions as func
import header

def main():
    # start height
    start_feet, start_inches = func.inputVal("starting")
    
    # end height
    invalid = True
    while invalid:
        end_feet, end_inches = func.inputVal("ending")
        if func.compareHeights(start_feet, start_inches, end_feet, end_inches):
            break
        else:
            print("Ending height must be greater than or equal to starting height. Please re-enter.")
    
    # table header
    header.header()
    
    # print table
    current_feet = start_feet
    current_inches = start_inches
    
    finished = False
    while not finished:
        cm = func.convert(current_feet, current_inches)
        func.tableRow(current_feet, current_inches, cm)
        
        if current_inches < 11:
            current_inches += 1
        else:
            current_inches = 0
            current_feet += 1
        
        if (current_feet > end_feet) or (current_feet == end_feet and current_inches > end_inches):
            finished = True

if __name__ == "__main__":
    main()