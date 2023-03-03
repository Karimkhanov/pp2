def countdown(n):
    while n >=0:
        yield n
        n-=1

a = int(input('Enter the countdown number: '))

for i in countdown(a):
    print(i)