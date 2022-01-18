"""
Christopher Morales
lab1.py

Problem: The purpose of this program is to calculate the average daily balance as well as finding the
monthly interest using inputs and arithmetic.

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with:
Ashley Woods
Isaiah Stapleton
"""
def finding_monthly_interest():
    annual_interest_rate = eval(input("Enter the Annual Percentage Rate:"))
    days_in_billing_cycle =eval(input("Enter the Days in The Billing Cycle:"))
    net_balance = eval(input("Enter the Net Balance:"))
    payment_received = eval(input("How much was the payment received?:"))
    day_of_payment = eval(input("What is the day of the payment?:"))
    step_one = net_balance * days_in_billing_cycle
    day = days_in_billing_cycle - day_of_payment
    step_two = payment_received * day
    step_three = step_one - step_two
    average_daily_balance = step_three / days_in_billing_cycle
    monthly_interest_rate = annual_interest_rate / 12 / 100
    found_monthly_interest_rate = str(round(average_daily_balance * monthly_interest_rate, 2))
    print("The Monthly Interest is $" + found_monthly_interest_rate)

finding_monthly_interest()