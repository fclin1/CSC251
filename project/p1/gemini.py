"""
Project 1: Mortgage Calculator
Class: CSC251
Date: 10/02/2025
This program calculates and displays an amortization table for a fixed-rate mortgage.
"""

import math
import rate_dict
from table_header import make_table_header

def get_positive_float(prompt):
    """Gets a positive float value from the user with input validation."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_valid_term(prompt):
    """Gets a valid loan term from the user."""
    valid_terms = [10, 15, 20, 30]
    while True:
        try:
            term = int(input(prompt))
            if term in valid_terms:
                return term
            else:
                print("We only offer 10, 15, 20, or 30-year terms. Please choose one.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_down_payment_percentage(prompt):
    """Gets a valid down payment percentage from the user."""
    while True:
        try:
            percentage = float(input(prompt))
            if 0 <= percentage <= 100:
                return percentage
            else:
                print("Please enter a percentage between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def output_loan_info(key):
    """
    Outputs the loan type with the rate information.
    Parameters:
        key (str): The key for the rates dictionary.
    Returns:
        None
    """
    rate = rate_dict.rates[key]
    print(f"Loan type: {key} at {rate:.3f}% APR")

def calc_PMI(purchase_price, down_payment_percentage):
    """
    Calculates the monthly PMI payment.
    Parameters:
        purchase_price (float): The purchase price of the home.
        down_payment_percentage (float): The down payment percentage.
    Returns:
        float: The monthly PMI payment.
    """
    loan_amount = purchase_price * (1 - down_payment_percentage / 100)
    ltv = (loan_amount / purchase_price) * 100
    pmi_rate = 0.0

    if 95 < ltv <= 100:
        pmi_rate = 1.040
    elif 90 < ltv <= 95:
        pmi_rate = 0.875
    elif 85 < ltv <= 90:
        pmi_rate = 0.685
    elif 80 < ltv <= 85:
        pmi_rate = 0.475

    monthly_pmi = (loan_amount * (pmi_rate / 100)) / 12
    return round(monthly_pmi, 2)

def main():
    """Main function to run the mortgage calculator."""
    purchase_price = get_positive_float("Enter the purchase price of your home: $")
    term_years = get_valid_term("Enter the term of the loan in years: ")
    down_payment_percent = get_down_payment_percentage("Enter your down payment percentage: ")

    down_payment_amount = purchase_price * (down_payment_percent / 100)
    loan_amount = purchase_price - down_payment_amount
    ltv_ratio = (loan_amount / purchase_price) * 100

    # Determine LTV string for dictionary key
    if ltv_ratio <= 80:
        ltv_string = "80% or less LTV"
    elif 80 < ltv_ratio <= 90:
        ltv_string = "80.1-90% LTV"
    else: # 90 < ltv_ratio <= 100
        if term_years == 10:
             ltv_string = "90.1-100% LTV"
        elif term_years == 15:
            ltv_string = "90.1-100% LTV"
        elif term_years == 20:
             ltv_string = "90.1-100% LTV"
        elif term_years == 30:
            ltv_string = "90.1-100% LTV"
        else: # Handle cases for 15, 20, 30 year loans that have different LTV brackets
             ltv_string = "90.1-100% LTV"


    if term_years in [15, 20, 30] and ltv_ratio <= 90:
        ltv_string = "90% or less LTV"
    elif term_years in [15, 20, 30] and ltv_ratio > 90:
        ltv_string = "90.1-100% LTV"

    # Construct the key for the rate dictionary
    rate_key = f"{term_years}-Year Fixed, {ltv_string}"


    annual_rate = rate_dict.rates[rate_key]
    monthly_rate = annual_rate / 100 / 12
    number_of_payments = term_years * 12

    # Calculate monthly payment
    if monthly_rate > 0:
        monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate)**number_of_payments) / ((1 + monthly_rate)**number_of_payments - 1)
    else:
        monthly_payment = loan_amount / number_of_payments
    monthly_payment = round(monthly_payment, 2)


    print(f"\nLoan amount: ${loan_amount:,.2f}")
    output_loan_info(rate_key)
    print(f"Monthly Payment: ${monthly_payment:,.2f}\n")

    make_table_header()

    principal_balance = loan_amount
    total_interest_paid = 0
    total_pmi_paid = 0
    monthly_pmi = calc_PMI(purchase_price, down_payment_percent)
    pmi_active = True

    print(f"{0:^8} {'':^18} {'':^20} {principal_balance:^20,.2f} {'':^9}")


    for payment_num in range(1, number_of_payments + 1):
        interest_payment = principal_balance * monthly_rate
        principal_payment = monthly_payment - interest_payment

        # Adjust final payment
        if principal_balance < monthly_payment:
            principal_payment = principal_balance
            monthly_payment = principal_payment + interest_payment

        principal_balance -= principal_payment

        # Check for PMI cutoff
        current_ltv = ((principal_balance+principal_payment) / purchase_price) * 100
        pmi_payment_this_month = 0
        if pmi_active:
            if current_ltv < 80:
                pmi_active = False
            else:
                 pmi_payment_this_month = monthly_pmi
                 total_pmi_paid += pmi_payment_this_month


        total_interest_paid += interest_payment

        print(f"{payment_num:^8} {interest_payment:^18,.2f} {principal_payment:^20,.2f} {principal_balance:^20,.2f} {pmi_payment_this_month:^9,.2f}")

    # Mortgage Summary
    total_principal_paid = loan_amount
    total_payments = total_principal_paid + total_interest_paid + total_pmi_paid

    print("\nMortgage Summary\n")
    print(f"{'Total interest paid:':<25} ${total_interest_paid:20,.2f}")
    print(f"{'Total payment to principal:':<25} ${total_principal_paid:20,.2f}")
    print(f"{'Total PMI paid:':<25} ${total_pmi_paid:20,.2f}")
    print(f"{'Total payments:':<25} ${total_payments:20,.2f}")


if __name__ == "__main__":
    main()
