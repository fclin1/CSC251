"""HW 6 menu.py, provides user options for car lot inventory
    Class: CSC251
    Date: Fall 2025
"""

def showMenu():
  '''Prints a menu of user options
    Parameters: none
    Returns: choice(str): string input from user
  '''
  print("\nChoose an option:")
  print("(s)how inventory")
  print("(a)dd a car")
  print("(r)emove a car")
  print("(c)hange a car price")
  print("(e)xit program")
  choice = input()
  print()
  return choice
