# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:58:26 2019

@author: HugoAfonso
"""

#x = (1, 2, (3, 'John', 4), 'Hi')
#
#y = x[0:-1]

#x = [1, 2, [3, 'John', 4], 'Hi']
#listA = [1, 4, 3, 0]
#listB = ['x', 'z', 't', 'q'] 
animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}
def how_many(aDict):
    count = 0
    for k,v in aDict.items():
        count += len(v)
        
    return count

how_many(animals)

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    count = 0
    key = ''
    for k,v in aDict.items():
        if len(v) > count:
            count = len(v)
            key = k
#    return count
    print(key)

biggest(animals)