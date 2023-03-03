import re

pattern = r'a.*b$'

strings = input('Enter a string:').split(",")

for string in strings:
    if re.match(pattern, string):
        print(f"{string} matches the pattern")
    else:
        print(f"{string} does not match the pattern")
