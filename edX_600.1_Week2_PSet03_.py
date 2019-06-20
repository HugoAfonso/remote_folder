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
    errorMargin = 0.01
    lower_bound = balance/12
    upper_bound = (balance * (1+monthlyInterestRate)**12)/12 
    tempBalance = balance
    tempPayment = (lower_bound+upper_bound)/2
    print(str(tempPayment))
    done = False
    while done != True:
        for t in range(1,13):
            monthlyUnpaidBalance = tempBalance - tempPayment
            updatedBalanceMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
            tempBalance = updatedBalanceMonth
            t+=1
        if abs(tempBalance) >= errorMargin and tempBalance > 0:
            lower_bound = tempPayment
        elif abs(tempBalance) >= errorMargin and tempBalance < 0:
            upper_bound = tempPayment
        else:
            done = True
        tempBalance = balance        
        tempPayment = (lower_bound+upper_bound)/2
    print('Lowest payment: '+str(round(tempPayment,2)))
    print('Lowest balance: '+str(round(tempBalance,2)))

payFixedDebtYear(320000,0.2)
print(str('29157.09'))
payFixedDebtYear(999999,0.18)
print('90325.03')
