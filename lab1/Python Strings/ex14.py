"""Slicing Strings"""

#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

# Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])
