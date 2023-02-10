
'''Write a function that accepts string from user, 
return a sentence with the words reversed. We are ready -> ready are We'''

def reverse_sentence(sentence):
    words = sentence.split()
    return " ".join(reversed(words))

sentence = input("Enter a sentence: ")
result = reverse_sentence(sentence)
print(result)
