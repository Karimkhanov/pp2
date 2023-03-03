#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

text = input('Enter string: ').split(",")
pattern = r"[a-z][_]"

for i in text:
    if re.search(pattern, i):
        print(i)