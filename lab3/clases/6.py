def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

numbers =  map(int, input("Enter the numbers:").split())

# Use filter function and a lambda function to filter out prime numbers
primes = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list:", primes)
