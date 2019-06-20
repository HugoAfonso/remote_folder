# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:17:43 2019

@author: HugoAfonso

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
    

Monthly interest rate= (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

"""
def payFixedDebtYear(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    initialFixedPayment = 10
    tempBalance = balance
    done = False
    while done != True:
        for t in range(1,13):
            monthlyUnpaidBalance = tempBalance - initialFixedPayment
            updatedBalanceMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
            tempBalance = updatedBalanceMonth
            t+=1
        if tempBalance > 0:
            tempBalance = balance
            initialFixedPayment +=10
        else:
            done = True
    print('Lowest payment: '+str(round(initialFixedPayment,2)))

payFixedDebtYear(4773,0.2)
print(str('440'))