
'''Define a functino histogram() that takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:'''

def histogram(numbers):
    for number in numbers:
        print("*" * number)

input_numbers = list(map(int, input("Enter a list of integers: ").split()))
histogram(input_numbers)
