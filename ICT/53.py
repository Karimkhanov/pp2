                                 #Lecture 7 LISTS
            
# my_list = [1, 53, 786, 4 ]
# print(my_list)



# my_list = [1, 53, 53, 53, 53, 786, 4 ]
# print(my_list)


# list_  = []
# print(list_)



# my_list = [5432, 6953.5796541, True, False, 'jhgdfvbk']
# print(my_list[0])
# print(my_list[2])



# my_list = [5432, 6953.5796541, True, False, 'jhgdfvbk']
# print(my_list[-1])
# print(my_list[-2])




# my_list = ['apple', 'banana', 'mango', 'grape']
# print('Here is the list', my_list)
# a =  int(input('Which on do you want to print: '))

# print(my_list[a - 1])





# my_list = ['apple', 'banana', 'mango', 'grape', 'Pear', 'Kiwi']
# print(my_list[1:4])


# my_list = ['apple', 'banana', 'mango', 'grape', 'Pear', 'Kiwi']
# print(my_list[4:])


# my_list = ['apple', 'banana', 'mango', 'grape', 'Pear', 'Kiwi']
# print(my_list[:3])



# my_list = ['apple', 'banana', 'mango', 'grape', 'Pear', 'Kiwi']
# print(my_list[1])
# my_list[1] = 'Peach'
# print(my_list)



# fruits =  ['Apple', 'Banana', 'Mango', 'Grape', 'Pear', 'Kiwi']
# print(fruits[1])
# fruits[1:3] = ['Peach', 'Cucumber']
# print(fruits)


# fruits =  ['Apple', 'Banana', 'Mango', 'Grape', 'Pear', 'Kiwi']
# fruits.insert(3, 'Pineapple')
# print(fruits)
# fruits.insert(0, 'Carrot')
# print(fruits)



# veg1_list = ['Carrot', 'Cucumber']
# print('Here is the list of vegetable: ', veg1_list)

# item = input('Which vegetable do you want to add: ')
# index = int(input('Where: '))
# veg1_list.insert(index, item)
# print('Here is the new list: ', veg1_list)



# fruits = []
# for i in range(5):
#     fruits.append('kiwi')
# print(fruits)


# fruits =  ['Apple', 'Banana', 'Mango', 'Grape', 'Pear', 'Kiwi']
# fruits.append('Pineapple')
# print(fruits)



# fruits = []

# f_to_add = input('Enter a fruit: ')

# while f_to_add != 'stop':

#   fruits.append(f_to_add)
#   f_to_add = input('Enter a fruit: ')
# print(fruits)



# fruits =  ['Apple', 'Banana', 'Mango', 'Grape', 'Pear', 'Kiwi', 'Banana']
# fruits.remove('Banana') # removes 1st item
# fruits.remove('Banana') #removes 2st item
# print(fruits)




# fruits =  ['Apple', 'Banana', 'Mango', 'Grape', 'Pear', 'Kiwi', 'Banana']
# item_removed = fruits.pop(3)
# print(fruits)
# print(item_removed)



# list_of_sport = ['tennis', 'ping-pong', 'kayak', 'foot']
# list_of_removed_sport = []

# index = int(input('What item do you want to remove? '))

# item_removed = list_of_sport.pop(index)
# list_of_removed_sport.append(item_removed)

# print(list_of_sport)
# print(list_of_removed_sport)



# list_of_sport = ['tennis', 'ping-pong', 'kayak', 'foot']
# list_of_removed_sport = []

# index = int(input('What item do you want to remove? '))

# item_removed = list_of_sport.pop(index)
# list_of_removed_sport.append(item_removed)
# print(list_of_sport)
# print(list_of_removed_sport)





# list_of_sport = ['tennis', 'ping-pong', 'kayak', 'foot']
# list_of_removed_sport = []

# item = input('What item do you want to remove? ')
# list_of_sport.remove(item)

# list_of_removed_sport.append(item)
# print(list_of_sport)
# print(list_of_removed_sport)




# fruits =  ['Apple', 'Banana', 'Mango', 'Grape', 'Pear', 'Kiwi', 'Banana']
# for i in fruits:
#   print(i)




# fruits =  ['Apple', 'Banana', 'Mango', 'Grape', 'Pear', 'Kiwi', 'Banana']
# for i in range(len(fruits)):
#   print(i)


# fruits =  ['Apple', 'Banana', 'Mango', 'Grape', 'Pear', 'Kiwi', 'Banana']
# for index, item in enumerate(fruits):
#   print(index, item)




# fruits =  ['Apple', 'Banana', 'Mango', 'Grape', 'Pear', 'Kiwi', 'Banana']
# if 'Grape' in fruits:
#     print('Yes')



fruits =  ['Apple', 'Banana', 'Mango', 'Grape', 'Pear', 'Kiwi','Apple','Apple','Apple','Apple', 'Banana']
while 'Apple' in fruits:
  fruits.remove('Apple')
print(fruits)





























                                        #Practice 6
# a = 5
# while a <= 50:
#     print(a, end = ' ')
#     a+=1



# a = int(input('Enter the number:'))
# while a % 2 == 0:
#     print(a, end = ' ')
#     a = a // 2
    
# print(a, end = ' ')



# answer = input('Hello ')
# cnt = 0
# while answer != 'Hello':
#   if cnt < 3:
#     answer = input('I said hello, do you have something to say to me? ')
#   elif cnt < 6:
#     answer = input('You have to say hello to me! ')
#   else:
#     answer = input('I SAID HELLO, ANSWER HELLO! ')
#   cnt += 1

# print('Thank you, how are you?')




# depth = int(input('Enter the depth'))
# up = int(input('Enter the up'))
# down = int(input('Enter the down'))
# day = 1
# position = 0 + up
# while position <= depth:
#   position -= down
#   day += 1
#   position += up
# print(day)









