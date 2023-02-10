
'''Write a Python function that checks whether a word or phrase is palindrome or not. 
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam'''

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

input_word = input("Enter a word or phrase: ")
result = is_palindrome(input_word)
if result:
    print("The word or phrase is a palindrome.")
else:
    print("The word or phrase is not a palindrome.")
