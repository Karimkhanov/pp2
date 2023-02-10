
'''Write a Python function that takes a list 
and returns a new list with unique elements of the first list. 
Note: don't use collection set'''

def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

lst = [int(x) for x in input("Enter a list of numbers: ").split()]
unique_lst = unique_list(lst)
print("The unique list is:", unique_lst)
