# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:58:26 2019

@author: HugoAfonso
"""
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    output = []
    for l in string.ascii_lowercase:
        if l not in lettersGuessed:
            output.append(l)
    return ''.join(output)

print(getAvailableLetters( ['a','e', 'i', 'k', 'p', 'r', 's','z'] ))
print(getAvailableLetters( [] ))

        print('''Good guess: '''+getGuessedWord(secretWord,lettersGuessed))
        print( '''-------------
Congratulations, you won!''')

