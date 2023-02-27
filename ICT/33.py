# num = int(input('Enter a number:'))
# prime = True
# for i in range(2, num, 1):
#     if num%i == 0:
#         prime = False
#         print('It is not a prime number because', i, 'x', num//i, '=', num)
#         break

# if prime: print('prime')

# a = int(input('Enter a number:'))
# while a!=5:
#     print('Hello')
#     a+=1

# n = int(input('Enter a number: '))
# total = 0
# a = -1
# while a < n:
#   a += 1
#   total += a
#   print(a, end = ' ')
# print('\nSum of all numbers:', total)



'''Ask for user input and print the lowest number which is bigger to this number when factorial (using while function).

Input: 563, Output: "6, because 6! > 563"

Input: 8, Output: "4, because 4! > 8"

Input: 51963, Output: "9, because 9! > 51963"'''

# num = int(input('Enter a number: '))

# factorial = 1
# i = 1

# while factorial <= num:
#     i += 1
#     factorial *= i # factorial = factorial * i

# print(i, "because", i, "! >", num)




# for i in range(0, 20):
#     print(i, end = ' ')
#     if i ==10:
#         break
# else:
#     print('The loop has finished!')




# a = 0

# while a != 3:
#   a+= 1
#   input1 = input('enter: ')
#   print(input1*2)


# i = 0
# while i < 20:
#   print(i, end = ' ')
#   i += 1
#   # if i == 10:
#   #   break
# else:
#   print('The loop has finished')



'''While loop exercise (10 min)
Ask user inputs, continue to ask user input until the number is between 0 and 10.

Example:

Enter a number between 0 and 10: 20

No, I said between 0 and 10: -6

No I said between 0 and 10: 5

Thank you!'''

# n = int(input("Enter a number between 0 and 10: "))

# while n < 0 or n > 10:
#   n = int(input("No, I said between 0 and 10: "))
# print('Thank you!')



# my_list = [12, 21, 478]

# print(my_list[1])
    

bot_said_hello = False

while not bot_said_hello:
    user_input = input("Say hello to start the conversation: ")
    if user_input.lower() == "hello":
        bot_said_hello = True
        print("Thank you, how are you?")
    else:
        print("I said hello, do you have something to say to me?")
        # Generate a random response to make the bot sound crazier
        import random
        craziness_levels = [
            "You have to say hello to me!", 
            "I can't hear you, speak up!", 
            "HELLO?!?!?", 
            "Are you ignoring me?", 
            "HELLOOOOOOOOOOOOOOOOOOOOOOOO", 
            "I think I'm going insane...",
            "I SAID HELLO, ANSWER HELLO!"
        ]
        print(random.choice(craziness_levels))











