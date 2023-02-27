# class Peolpe:
#     def __init__(person, surname, name, age, gender, gpa, school ):
#         person.surname = surname
#         person.name = name
#         person.age = age 
#         person.gender = gender
#         person.gpa =  gpa
#         person.school = school

# info = Peolpe(' Karimkanov', 'Tursynkhan', 17, "male", 2.2, "FIT")

# print(info.surname,'\n', info.name,'\n', info.age, '\n', info.gender,'\n', info.gpa, '\n', info.school,'\n')



# class ATM:
#     def __init__(money, tenge, euro, dollar, ruble):
#         money.tenge = tenge
#         money.euro = euro
#         money.dollar = dollar
#         money.ruble = ruble

#     def __str__(money):
#         return f"{money.tenge} tenge\t {money.euro} euro \t {money.dollar} dollar \t  {money.ruble} ruble\t"

# info = ATM(500, 1, 1, 71)
# print(info)

from datetime import datetime, timedelta

# get current date and time
current_time = datetime.now()

# subtract five days from current date
new_time = current_time - timedelta(days=5)

print("Current Time:", current_time)
print("New Time (five days ago):", new_time)

from datetime import datetime, timedelta

# get current date and time
current_time = datetime.now()

# calculate yesterday and tomorrow
yesterday = current_time - timedelta(days=1)
tomorrow = current_time + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%m/%d/%Y"))
print("Today:", current_time.strftime("%m/%d/%Y"))
print("Tomorrow:", tomorrow.strftime("%m/%d/%Y"))


from datetime import datetime

# get current date and time
current_time = datetime.now()

# drop microseconds
current_time = current_time.replace(microsecond=0)

print("Current Time without Microseconds:", current_time)


from datetime import datetime

# set the two dates to compare
date1 = datetime(2023, 2, 1, 12, 0, 0)
date2 = datetime(2023, 2, 15, 15, 30, 0)

# calculate the difference in seconds
difference_seconds = (date2 - date1).total_seconds()

print("Difference in Seconds:", difference_seconds)

print(date1)
print(date2)

from datetime import datetime

# get user input for first date and time
date1_str = input("Enter first date in YYYY-MM-DD HH:MM:SS format: ")
date1 = datetime.strptime(date1_str, '%Y-%m-%d %H:%M:%S')

# get user input for second date and time
date2_str = input("Enter second date in YYYY-MM-DD HH:MM:SS format: ")
date2 = datetime.strptime(date2_str, '%Y-%m-%d %H:%M:%S')

# calculate the difference in seconds
difference_seconds = (date2 - date1).total_seconds()

# print the difference in seconds
print("Difference in Seconds:", difference_seconds)


