
'''You are given list of numbers separated by spaces. 
Write a function filter_prime which will take 
list of numbers as an agrument and returns only prime numbers from the list.'''

def filter_prime(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]

numbers = list(map(int, input("Enter the prime numbers: ").split()))
print(filter_prime(numbers))
