                                            #GENERATORS
    
    #yield- выход /return
    
# def f():
#     yield 1
#     yield 2
#     yield 3

#print(f()) adress
# for i in f(): 
#     print(i)  output 1 2 3

# print(next(f()))
# print(next(f()))
# print(next(f()))  output 1 1 1 

# g1 = f()
# print(next(g1))
# print(next(g1))
# print(next(g1))  #Output 1 2 3





# def f(n):
#     a, b = 0, 1
#     cnt = 2
#     while cnt < n:
#         yield b
#         c = a + b
#         a = b
#         b = c
#         cnt = cnt + 1

# for i in f(50):
#     print(i)


                                            #RegEx

#import re  Library of RegEx

# import re
# txt  = input()
# pattern = "t.*t"
# x = re.search(pattern, txt)

# print(x)


# import re
# txt  = input()
# pattern1 = "[0-9]+"
# pattern2 = "\d"

# x1 = re.search(pattern1, txt)

# print(x1)

# x2 = re.search(pattern2, txt)

# print(x2)



# import re

# txt = "The rain in Spain Seatle"
# x = re.findall(r"\bS\w+", txt)
# print(x)



# import re

# #Replace all white-space characters with the digit "9":

# txt = "Th   e rain in     Spain"
# x = re.sub("\s", "9", txt)
# print(x)


# import datetime
# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))
# print(x.hour,":",x.minute)


# import datetime
# x = datetime.datetime(2023, 2, 25, 15, 40, 12)
# print(x)


# import datetime

# x = datetime.datetime.now()
# print(x.strftime("%X"))
# print(x.strftime("%A"))



import datetime

# create two datetime objects
start_time = datetime.datetime(2023, 2, 25, 12, 0, 0)
end_time = datetime.datetime(2024, 2, 25, 12, 0, 0)

# calculate the difference in seconds
time_diff = (end_time - start_time).total_seconds()

# print the result
print("The time difference is", time_diff, "seconds.")



















