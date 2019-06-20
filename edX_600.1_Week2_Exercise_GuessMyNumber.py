# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 23:31:08 2019

@author: HugoAfonso
"""

low = 0
high = 100
result = (high+low)//2.0
print('Please think of a number between 0 and 100!')
print('Is your secret number '+str(result)+'?')
test = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while test != 'c':
    if test == 'h':
        high = result
        result = (high+low)//2.0
        print('Is your secret number '+str(result)+'?')
        test = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    elif test == 'l':
        low = result
        result = (high+low)//2.0
        print('Is your secret number '+str(result)+'?')
        test = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    elif test not in ('h','l','c'):
        print('Sorry, I did not understand your input.')
        print('Is your secret number '+str(result)+'?')
        test = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
print('Game over. Your secret number was: '+str(result))