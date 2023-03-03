import re

string = input('Enter a string: ')

pattern = r'a[bb]{2,3}'

if re.search(pattern, string):
    print("Match found!")
else:
    print('Match not found.')