import re

text = "SplitThisStringAtUppercaseLetters"

split_text = re.findall('[A-Z][^A-Z]*', text)

print(split_text)
