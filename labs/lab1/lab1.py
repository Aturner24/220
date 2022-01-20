"""
Andrew Turner
lab1.py
Create an algorithm to calculate a user's monthly interest
I certify that this assignment is entirely my own work.
"""
def monthly_interest():
    annual_interest = (eval(input("Annual interest rate:")) / 12) / 100
    billing_chilling = eval(input("Days in billing cycle:"))
    net_balance = eval(input("Net Balance:"))
    payment = eval(input("payment amount:"))
    billing_day = eval(input("Day of billing cycle:"))
    dailybalance  = ((net_balance * billing_chilling) - (payment * (billing_chilling-billing_day) )) / billing_chilling
    print("Your monthly interest is: $", dailybalance * annual_interest)

