# # Importing the array module in Python
# import array

# # Defining an array of integers with a fixed size
# arr = array.array("i", [1, 2, 3, 4, 5])

# # Defining a list of mixed data types
# lst = [1, 2, "three", 4.0, [5]]

# # Accessing elements of the array
# print("Array Element at index 2:", arr[2])

# # Accessing elements of the list
# print("List Element at index 2:", lst[2])

# # Trying to change the size of the array (Not possible in Python)
# arr.append(6)  # This will raise an error

# # Changing the size of the list
# lst.append(6)  # This is possible and the size of the list will change


import random

random_number = random.randint(1, 100)
print(random_number)
