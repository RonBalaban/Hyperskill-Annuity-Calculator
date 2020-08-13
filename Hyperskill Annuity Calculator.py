# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 21:37:58 2020

@author: Rbala
"""

import math

print("""
What do you want to calculate?
type "n" for the count of months,
type "a" for the annuity monthly payment,
type "p" for the credit principal:
""")
choice = input().lower()

def time_fun(yrs, mns):  
    if mns == 12:  # If it says 12 months, make it 1 year instead
        yrs += 1
        mns -= 12  
    mns_filler = ''  # Start as empty fillers, then adjust
    yrs_filler = ''
    and_filler = ''
    if mns >= 1:  # Handles plurality
        if mns > 1:
            mns_filler = f' {mns} months'
        else:
            mns_filler = f' {mns} month'    
    if yrs >= 1:  # # Handles plurality
        if yrs > 1:
            yrs_filler = f' {yrs} years'
        else:
            yrs_filler = f' {yrs} year'     
    if mns >= 1 and yrs >= 1:  # If neither is missing, we need 'and'
        and_filler= ' and'
    return (f'You need{yrs_filler}{and_filler}{mns_filler} to repay this credit!')

def find_n():
    principal = float(input('Enter the credit principal: \n'))  # P
    monthly_payment = float(input('Enter the monthly payment: \n'))  # A
    int_monthly = float(input('Enter the credit interest: \n')) / 1200  # If user gives 12% Annual int. rate, we get i = 0.01
    #  n = math.log(A / (A - i * P), 1 + i)
    n = math.log(monthly_payment / (monthly_payment - int_monthly * principal), 1 + int_monthly)  # Count of periods
    y = int(n // 12)  # Years in n
    m = int(math.ceil(n) - (y * 12))  # months left after y years in n  
    return time_fun(y, m)  # Used to convert periods into years and months
    
def find_a():
    principal = float(input('Enter the credit principal: \n'))  # P
    periods = float(input('Enter the number of periods: \n'))  # n
    int_monthly = float(input('Enter the credit interest: \n')) / 1200  # i
    #  A = P * (i *(1 + i) ** n) / ((1 + i) ** n - 1)    
    A = math.ceil(principal * (int_monthly *(1 + int_monthly) ** periods) / ((1 + int_monthly) ** periods - 1))
    return f'Your annuity payment = {A}!' 

def find_p():
    monthly_payment = float(input('Enter the monthly payment: \n'))  # A
    periods = float(input('Enter the number of periods: \n'))  # n
    int_monthly = float(input('Enter the credit interest: \n')) / 1200  # i
    #  P = A / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    P = round(monthly_payment / ((int_monthly * (1 + int_monthly) ** periods) / ((1 + int_monthly) ** periods - 1)), )
    return f'Your credit principal = {P}!'

if choice == 'n':
    print(find_n())
    
elif choice == 'a':
    print(find_a())
    
elif choice == 'p':
    print(find_p())
    



"""
import math
principal = float(input('Enter the credit principal: '))
print("What do you want to calculate?
type 'm' - for the number of months,
type 'p' - for the monthly payment: ")
choice = input().lower()

def months_f():
    months = math.ceil(principal / payment)
    filler = 's'
    if months == 1:
        filler = ''
    return (f'\nIt takes {months} month{filler} to repay the credit')

def payment_f():
    payment = math.ceil(principal / months)
    filler = ''
    if months * payment > principal:  # In case the payments are non-level
        final_payment = int(principal - (months - 1) * payment)
        filler = f' with last monthly payment = {final_payment}.'   
    return(f'\nYour monthly payment = {payment}{filler}')
      
if choice == 'm':
    payment = float(input('Enter the monthly payment: '))
    print(months_f())
    
elif choice == 'p':
    months = int(input('Enter the count of months: '))
    print(payment_f())
"""













    
