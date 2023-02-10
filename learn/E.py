'''print("Printing current and previous number sum in range(10) ")
previous_num = 0
current_num = 0
sum_num = previous_num + current_num
for num in range(10):
    print("Current Number", f"{current_num}", "Previous Number ", f"{previous_num}", " Sum:", f"{sum_num}")
    current_num = current_num + 1
    sum_num = previous_num + current_num
    previous_num = previous_num + 1
    
print(current_num, sum_num, previous_num)'''

# print("Printing current and previous number and their sum in a range(10)")
# previous_num = 0

# # loop from 1 to 10
# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
#     # modify previous number
#     # set it to the current number
#     previous_num = i