# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 14:48:20 2018

@author: HugoAfonso
"""
#
#def genTest():
#    yield 1
#    yield 2 #After this, we get StopIteration Error
#
#foo = genTest()
#foo.__next__()
#foo.__next__()
#foo.__next__()
#
#def genFib():
#    fibn_1 = 1 #fib(n-1)
#    fibn_2 = 0 #fib(n-2)
#    while True:
#        #fib(n)=fib(n-1) + fib(n-2)
#        next = fibn_1  +fibn_2
#        yield next
#        fibn_2 = fibn_1
#        fibn_1 = next
        
# "range" is a generator
        
#def genPrimes():
#    primes = []
#    x = 1 #the starting number
#    while True: #loop start
#        x += 1 #the first prime number is 2
#        for i in primes: #first number in i is 1, so 2%1 == 0
#            if x % i == 0: #verification...
#                break #...action for not prime
#        else:
#            primes.append(x) #...action for prime
#            yield x #function
#        
#primeGen = genPrimes()
#primeGen.__next__()
import string

def shiftCD(shift):
    lowerCD = {}
    upperCD = {}
    fullShiftCD = {}
    for k,v in enumerate(string.ascii_lowercase):
        try:
            lowerCD[k] = string.ascii_lowercase[k+shift]
        except IndexError:
            lowerCD[k] = string.ascii_lowercase[k-26+shift]
    
    for k,v in enumerate(string.ascii_uppercase):
        try:
            upperCD[k] = string.ascii_uppercase[k+shift]
        except IndexError:
            upperCD[k] = string.ascii_uppercase[k-26+shift]
    a = list(lowerCD.values())
    b = list(upperCD.values())
    c = a + b
    fullShiftCD = dict(zip(string.ascii_letters, c))
        
    return fullShiftCD


