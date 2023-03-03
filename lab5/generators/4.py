def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input('Enter the a: '))
b = int(input('Enter the b: '))

for square in squares(a, b):
    print(square)