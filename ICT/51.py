# for i in range(5, 51):
#     print(i, end = ' ')

# a = int(input('Enter the start:'))
# b = int(input('Enter the end:'))
# c = int(input('Enter the step:'))

# for i in range(a,b,c):
#     print(i, end ="-")


# width = int(input('Enter the widht of the pyramid:'))
# for i in range(1,width + 1, 2):
#     print( " " * ((width - i) // 2) + '*'*i + " "*((width-i)//2))


# height = int(input("Enter the height of the pyramid: "))
# for i in range(1, height+1, 1):
#     spaces = height - i
#     print(' ' * spaces + '*' * (2*i-1) + ' ' * spaces)


a = int(input('Enter a number:'))
if a > 1:
    for i in range(2, num):
     if (num % i) == 0:
            print("No because", i, "*", "=",(num/i))