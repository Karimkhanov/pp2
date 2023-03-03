import re

text = input('Enter a string: ').strip()

pattern = r"[A-Z][a-z]+"

matches = re.findall(pattern, text)

print(matches)
