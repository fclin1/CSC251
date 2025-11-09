"""
Author: Frank Lin
Email: fclin@ncsu.edu
Class: CSC 251 Fall 2025
Program: Project 1
Purpose: Displays an amortization table for a fixed-rate mortgage.
Bugs: None
Acknowledgements: None
"""

import math
import rate_dict
from table_header import make_table_header

def get_purchase_price(prompt):
    """Validates user input to ensure a positive float for purchase price."""
    while True:
        try:
            price = float(input(prompt))
            if price >= 0:
                return price
            else:
                print("Please enter a positive value for the purchase price.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_term_years(prompt):
    """Validates user input to ensure the term is one of the allowed values."""
    valid_terms = [10, 15, 20, 30]
    while True:
        try:
            term = int(input(prompt))
            if term in valid_terms:
                return term
            else:
                print("Please choose a 10, 15, 20, or 30-year term.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_down_payment_percentage(prompt):
    """Validates user input to ensure the down payment percentage is between 0 and 100."""
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
    """
    rate = rate_dict.rates[key]
    print(f"Loan type: {key} at {rate:.3f}% APR")

def calc_PMI(purchase_price, down_payment_percentage):
    """
    Calculates the monthly PMI payment.
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
    """Main function to execute the mortgage calculator program."""
    # Get user input
    purchase_price = get_purchase_price("Enter the purchase price of the home: $")
    term_years = get_term_years("Enter the term of the loan in years: ")
    down_payment_percentage = get_down_payment_percentage("Enter your down payment percentage: ")

    # Calculate down payment and loan amount
    down_payment_amount = (down_payment_percentage / 100) * purchase_price
    loan_amount = purchase_price - down_payment_amount
    ltv_ratio = (loan_amount / purchase_price) * 100

    # Convert LTV ratio to string for rate lookup
    ltv_str = ""
    if term_years == 10:
        if ltv_ratio <= 80:
            ltv_str = "80% or less LTV"
        elif 80 < ltv_ratio <= 90:
            ltv_str = "80.1-90% LTV"
        else:
            ltv_str = "90.1-100% LTV"
    else:
        if ltv_ratio <= 90:
            ltv_str = "90% or less LTV"
        else:
            ltv_str = "90.1-100% LTV"
    
    # Construct the key for rate lookup
    rate_key = f"{term_years}-Year Fixed, {ltv_str}"

    annual_rate = rate_dict.rates[rate_key] / 100
    monthly_rate = annual_rate / 12
    total_payments = term_years * 12

    # Calculate monthly payment
    monthly_payment = loan_amount * monthly_rate * (1 + monthly_rate) ** total_payments / ((1 + monthly_rate) ** total_payments - 1)
    monthly_payment = round(monthly_payment, 2)

    # Output amortization table
    print(f"\nLoan amount: ${loan_amount:,.2f}")
    output_loan_info(rate_key)
    print(f"Monthly Payment = ${monthly_payment:,.2f}\n")

    make_table_header()
    print(f"{0:^8} {'':^18} {'':^20} {loan_amount:^20,.2f} {'':^9}")

    principal = loan_amount
    total_interest = 0
    total_pmi = 0
    monthly_pmi = calc_PMI(purchase_price, down_payment_percentage)
    pmi_required = True

    for payment in range(1, total_payments + 1):
        interest_payment = round(principal * monthly_rate, 2)
        principal_payment = round(monthly_payment - interest_payment, 2)

        # Check for PMI
        if pmi_required:
            current_ltv = (principal / purchase_price) * 100
            if current_ltv < 80:
                pmi_required = False
                monthly_pmi = 0
            else:
                 total_pmi += monthly_pmi

        principal -= principal_payment
        total_interest += interest_payment

        print(f"{payment:^8} {interest_payment:^18,.2f} {principal_payment:^20,.2f} {principal:^20,.2f} {monthly_pmi:^9,.2f}")

    # Mortgage summary
    total_payments = loan_amount + total_interest + total_pmi

    print("\nMortgage Summary\n")
    print(f"{'Total interest paid: $':<30}{total_interest:>47,.2f}")
    print(f"{'Total payment to principal: $':<30}{loan_amount:>47,.2f}")
    print(f"{'Total PMI paid: $':<30}{total_pmi:>47,.2f}")
    print(f"{'Total payments: $':<30}{total_payments:>47,.2f}")

if __name__ == "__main__":
    main()