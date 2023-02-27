# #The string representation of an object WITH the __str__() function:
# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age

# #   def __str__(self):
# #     return f"{self.name}({self.age})"

# # p1 = Person("John", 36)

# # print(p1)

# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def __str__(self):
# #         return f"{self.name}({self.age})"
# # info = Person('Joe', 78)
# # print(info)

# # def ounces(inp):
# #     return 28.3495231 * inp
# # print(ounces(int(input())))


# # def toOunces(grams):
# #     print(28.3495231 * grams)
    
# # x = int(input())
# # toOunces(x)

# # def grams_to_ounces(grams):
# #     return grams / 28.34952
# # print(grams_to_ounces(100))



# # lenght = int(input('Enter a lenght:'))
# # width = int(input('Enter a width:'))
# # msg = '*' *lenght + '\n'
# # print(msg*width)

# # height = int(input())
# # width = int(input())
# # for i in range(height):
# #     print('*' * width)

# # sum_num = 0
# # for i in range(11): #range(start, end, step)
# #     sum_num += i
# # print(sum_num)

# # for i in range(1, 11):
# #     print(i)

# # n = 0
# # for i in range(0, 10, 2):
# #     n += i
# # print(n)

# # sum_odd = 0
# # for i in range(21, 51, 2):
# #     sum_odd += i
# # print(sum_odd)

# # for i in range(1,6):
# #     print(i)
# #     if i > 5:
# #         break

# '''ask user input

# print all number from 20 until the minimum between 100 and the user input

# if you stop at 100, print: 'It's too long I stopped'

# input: 1000 output: numbers from 20 until 100

# input: 80 output: numbers from 20 until 80'''

# # def print_numbers():
# #     user_input = int(input("Please enter a number: "))
# #     for i in range(20, 101):
# #         if i > user_input:
# #             break
# #         print(i)
# #     if i == 100:
# #         print("It's too long I stopped")
# # print(print_numbers())


# '''
# Repeat every letter of a user input
# Repeat only the letters
# Skip the letter 'o'
# example: input: "hello, you", output: "hheelllloo,, yyoouu"

# example: input: "hello, you", output: "hheelllloo, yyoouu"

# example: input: "hello, you", output: "hheellll, yyuu" '''

# # def repeat_letters():
# #     user_input = input("Please enter a string: ")
# #     result = ""
# #     for char in user_input:
# #         if char.isalpha() and char != 'o':
# #             result += char * 2
# #         else:
# #             result += char
# #     print(result)
# # print(repeat_letters())

# # a = input('Enter a text: ')
# # for i in a:
# #   if i == ',' or i == ' ':
# #     print(i, end = '')
# #   else:
# #     print(i*2, end = '')

# base_width = int(input("Enter the width of the pyramid: "))

# for i in range(1, base_width+1, 2):
#     print(' ' * ((base_width - i) // 2) + '*' * i + ' ' * ((base_width - i) // 2))


# num = int(input("Enter a number: "))

# # Prime numbers are greater than 1
# if num > 1:
#     # Check for factors
#     for i in range(2, int(num/2)+1):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print("Because", i, "x", int(num/i), "=", num)
#             break
#     else:
#         print(num, "is a prime number")
        
# # If input number is less than or equal to 1, it is not a prime number
# else:
#     print(num, "is not a prime number")


# mytuple = ('apple','jam', 'noodle')
# mu = iter(mytuple)
# print(next(mu))
# print(next(mu))
# print(next(mu))

# myname = ['Sultan','Tursynkhan','Asyl','Altynbek']
# friends = iter(myname)
# print(next(friends))

def

















