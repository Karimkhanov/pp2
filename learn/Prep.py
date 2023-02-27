#Preparation to defense!

# print('Hello World!')

# if 6 > 3:
#     print("Six is greater than 3!")

'''if 7 < 7
print("Seven is not greater than itself!")'''

# if 4 > 3:
#     print('Four is greater than three')
# if 5 > 9:
#     print("Imposiblle!")

'''if 3 > 1:
    print("It is true!")
        print("Imposible!")'''

# a = 5
# u = 'Hello Pal!'
# print(a)
# print(u)

#This is a comment.
# print("Hello WOrld!")

# print("Hello") #Hello

#print('Hello')
# print('Hiii')

# a = 3 #a is integer 
# a = "Hool" #now a is string
# print(a)

# a = str(7)
# s = int(8)
# d = float(67)
# print(a,'\n', s,'\n', d)

# a = 5 
# i = "Jon"
# d = 1j + 3
# s = 342.87e3
# print(type(a))
# print(type(i))
# print(type(d))
# print(type(s))

# a = 3
# A = "Fight"
# print(a, A)

# x, y, z = "Roor3", 'jjsi', 'Huiw'
# print(x,'\t', y, '\t', z)

# a = e = r = 'Joo,'
# print(a,e,r)

# fruits = ["apple", "banana", "cherry"]
# a, s, d = fruits
# print(a, s, d)    #Unpacking a list

# a = "U "
# d = "are"
# s = "Awesome"
# print(a, d, s) or print(a + d + s)

# a = 3
# e = 2
# print(a + e)

'''a = 3
u = 'Hij'
print(a + u)'''

# a = 34
# rj  = 'JOj'
# print(a, rj)

# a = 'awesome'

# def myfunc():
#     print('Python is ' + a)

# myfunc()

# def kk():
#     global e
#     e = "How"
# kk()

# print('Me ' + e)

# import array

# arr = array.array('i', [1,2,3,4,5])

# lst = [1,2,'three', 4.0,[5]]

# print('ARR index 2:', arr[2])

# print('List index 2:', lst[2])

# arr.append(6)

# lst.append(6)

# a = 'Hi'
# print(len(a))

# for i in 'Ban':
#     print(i)

# t = 'The best friend!'
# if 'The' in t: print('Yes it is!')
# else: print('No')

# b = 'Hello, World!'
# print(b[-5:-2])

# a = 'heh'
# b = "GVG"
# print(a.upper())
# print(b.lower())

# a = ' Hello, World!      '
# print(a.strip())

# a = 'Hello'
# print(a.replace('H','o'))

# a = 'Hello, Bestie!'
# print(a.split(","))

# age = 90
# kg = 65
# txt = 'My age is {} and kg is {}'
# print(txt.format(age, kg))


class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        print(f"{amount} has been deposited to ypur account. Current balnce is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print('Available')
        else:
            self.balance -= amount
             print(f"{amount} has been withdrawn from your account. Your current balance is {self.balance}.")
    def owner_name(self,name)
        self.name = name
account = BankAccount('Tursynhan')

account.deposit(int(input()))
account.deposit(int(input()))

account.withdraw(int(input()))
account.withdraw(int(input()))

try:
  n1 = int(input('Enter n1 :'))
except ValueError:
  print('The first number is incorrect')
try:
  n2 = int(input('Enter n2 :'))
except ValueError:
  print('The second number is incorrect')

op = input("Enter an operation")

if op == 'Division':
  try:
    print(n1/n2)
  except ZeroDivisionError:
    print('The seconde number is 0!')
  elif op == 
else:
  print('I don\'t know this operation')








