"""
Author: Frank Lin
Email: fclin@ncsu.edu
Class: CSC 251 Fall 2025
Program: Homework 5
Purpose: Displays a statisticl summary of student records from a file.
Bugs: None
Acknowledgements: Used Claude to help with the structure of load_info().
"""

from hw5_table_header import hw5_table_header

def main():
    """
    Main function.
    """
    # Load records from file
    student_records = load_info()

    if student_records:
        sort_info(student_records)
        print_info(student_records)

        # Calculate statistics
        mean = get_mean(student_records)
        median = get_median(student_records)

        valid_grades = []
        for record in student_records:
            grade = record[2]
            if isinstance(grade, int):
                valid_grades.append(grade)
        if valid_grades:
            min_grade = min(valid_grades)
            max_grade = max(valid_grades)

            print("\nExam Stats")
            print("-" * 35)
            print(f"{'Minimum':<15}{min_grade:>20}")
            print(f"{'Maximum':<15}{max_grade:>20}")
            print(f"{'Mean':<15}{mean:>20.1f}")
            print(f"{'Median':<15}{median:>20.1f}")

def load_info():
    """
    Prompts user for filename and reads student records from the file.
    Returns: a list of tuples (name, id, grade).
    """
    student_records = []
    file_opened = False
    
    # Keep prompting until valid file is opened
    while not file_opened:
        try:
            filename = input("Enter input filename: ")
            with open(filename, 'r') as file:
                lines = file.readlines()
                file_opened = True
        except IOError as e:
            print(f"Exception thrown: {e}")
            continue
        except FileNotFoundError as e:
            print(f"Exception thrown: {e}")
            continue
    
    # Process the file
    i = 0
    while i < len(lines):
        try:
            # Check for incomplete record
            if i + 2 >= len(lines):
                raise ValueError()

            # Read and process student record
            name = lines[i].strip()
            if len(name) > 19:
                name = name[:19]

            student_id = lines[i + 1].strip()
            if len(student_id) > 7:
                student_id = student_id[:7]

            grade = process_grade(lines[i + 2].strip())
            
            # Add record to list
            student_records.append([name, student_id, grade])
            i += 3
            
        except ValueError as ve:
            print(f"Exception thrown: {ve}")
            break
    
    return student_records
        
def process_grade(grade_str):
    """
    Processes the grade string and returns a valid grade or "N/A".
    Raises ValueError for invalid grade formats.
    """
    try:
        grade = float(grade_str)
        grade = round(grade)
        
        if grade < 0 or grade > 110:
            return "N/A"
        elif grade == 0:
            return "N/A"
        else:
            return grade
    except ValueError:
        raise ValueError()

def print_info(student_records):
    """
    Prints the records in a formatted table.
    """
    hw5_table_header()
    for record in student_records:
        name, student_id, grade = record
        print(f"{name:<20}{student_id:>7}{grade:>8}")

def sort_info(student_records):
    """
    Sorts student records by grade in descending order.
    N/A grades are placed at the end, identical grades maintain original order.
    """

    def sort_grade(record):
        grade = record[2]
        if grade == "N/A":
            return -1
        else:
            return grade
    student_records.sort(key=sort_grade, reverse=True)

def get_mean(student_records):
    """
    Returns the mean of valid grades.
    """
    valid_grades = []
    for record in student_records:
        grade = record[2]
        if isinstance(grade, int):
            valid_grades.append(grade)

    if valid_grades:
        return sum(valid_grades) / len(valid_grades)
    else:
        return 0.0

def get_median(student_records):
    """
    Returns the median of valid grades.
    """
    valid_grades = []
    for record in student_records:
        grade = record[2]
        if isinstance(grade, int):
            valid_grades.append(grade)
    
    valid_grades.sort()
    n = len(valid_grades)
    
    if n == 0:
        return 0.0
    elif n % 2 == 1:
        return valid_grades[n // 2]
    else:
        mid1 = valid_grades[n // 2 - 1]
        mid2 = valid_grades[n // 2]
        return (mid1 + mid2) / 2
    
if __name__ == "__main__":
    main()