string = input("Enter a string: ")

num_upper = sum(1 for char in string if char.isupper())

num_lower = sum(1 for char in string if char.islower())

print("Number of uppercase letters:", num_upper)
print("Number of lowercase letters:", num_lower)
