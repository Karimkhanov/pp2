
'''Write a function that accepts string 
from user and print all permutations of that string.'''

import itertools

def permutations(string):
    perms = [''.join(p) for p in itertools.permutations(string)]
    return set(perms)

string = input("Enter a string: ")
result = permutations(string)
print("\n".join(result))
