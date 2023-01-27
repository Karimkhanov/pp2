"""Python Strings"""

print("Hello")
print('Hello')

a = "Hello"
print(a)

#You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Get the character at position 1 
a = "Hello, World!"
print(a[1])

#Loop through the letters in the word "banana":
for x in "banana":
  print(x)

#The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

#Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

#Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

#print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

