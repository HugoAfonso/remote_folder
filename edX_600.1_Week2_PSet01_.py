# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:17:43 2019

@author: HugoAfonso

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

"""
#def payDebtYear(balance, annualInterestRate, monthlyPaymentRate):
monthlyInterestRate = annualInterestRate / 12.0
t=0
tempBalance = balance
while t < 12:
    minMonthlyPayment = tempBalance * monthlyPaymentRate
    monthlyUnpaidBalance = tempBalance - minMonthlyPayment
    updatedBalanceMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    tempBalance = updatedBalanceMonth
    t+=1
print('Remaining balance: '+str(round(tempBalance,2)))

#payDebtYear(42,0.2,0.04)