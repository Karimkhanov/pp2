# a = 5
# while a!= 51:
#     print(a, end = ' ')
#     a+=1


# number = int(input("Enter the number: "))

# print(number, end=' ')
# while number % 2 == 0:
#     number = number // 2
#     print(number, end=' ')


# input1 = input('Hello!')
# cnt = 0
# while input1 != 'Hello':
#     if cnt < 3:
#         input1 = input('I said hello, do you have something to say to me?')
#         cnt+=1
#     elif cnt < 6:
#         input1 = input('You have to say hello to me! ')
#         cnt+=1
#     else:
#         input1 = input('I SAID HELLO, ANSWER HELLO!')
#         cnt+=1
        
# print('Thank you, how are you? ')

# input1 = int(input('Enter the number: '))
# print(input1, end = ' ')
# while input1 % 2 == 0:
#     input1 = input1 // 2
#     print(input1, end = ' ')


# import math

# depth = int(input("Enter the depth of the well: "))
# climb_distance = int(input("Enter the daily distance climbed by the snail: "))
# slide_distance = int(input("Enter the night distance slide down by the snail: "))


# days = math.ceil((depth - climb_distance) / (climb_distance - slide_distance)) + 1
# #The math.ceil() 
# #function is used to round up the result of the division

# print("The snail will exit in", days, "days.")

# import math

# depth = int(input("Enter the depth of the well: "))
# climb_distance = int(input("Enter the daily distance climbed by the snail: "))
# slide_distance = int(input("Enter the night distance slide down by the snail: "))

# distance_climbed = 0
# days = 0

# while distance_climbed < depth:
#     days += 1
#     distance_climbed += climb_distance
#     if distance_climbed >= depth:
#         break
#     distance_climbed -= slide_distance

# print("The snail will exit in", days, "days.")



# Get the depth of the well from the user
while True:
    depth = input("Enter the depth of the well: ")
    if depth.isdigit():
        depth = int(depth)
        break
    else:
        print("Invalid input, please enter a positive integer.")

# Get the daily climbing distance and the nightly sliding distance from the user
while True:
    climb = input("Enter the daily distance climbed by the snail: ")
    slide = input("Enter the night distance slide down by the snail: ")
    if climb.isdigit() and slide.isdigit() and int(climb) > int(slide):
        climb = int(climb)
        slide = int(slide)
        break
    else:
        print("Sorry, the daily distance must be greater than the nightly distance. Please try again.")

# Calculate the number of days it takes for the snail to climb out of the well
days = 1
distance_climbed = climb

while distance_climbed < depth:
    distance_climbed -= slide
    if distance_climbed < 0:
        distance_climbed = 0
    distance_climbed += climb
    days += 1

# Print the result
print("The snail will exit in", days, "days.")

        















