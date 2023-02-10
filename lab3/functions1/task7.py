
'''Given a list of ints, 
return True if the array contains a 3 next to a 3 somewhere.'''

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums = [int(x) for x in input("Enter a list of integers: ").split()]
result = has_33(nums)
print(result)
