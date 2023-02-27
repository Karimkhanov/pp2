height = int(input("Enter the height of the pyramid: "))
top_char = input("Enter the character to use at the top of the pyramid: ")

# Print the top of the pyramid
print(' ' * (height) + top_char)

# Print the bottom half of the pyramid
for i in range(2, height+1):
    num_spaces = 2*i - 3
    print(' ' * (height - i + 1) + '/' + ' ' * num_spaces + '\\')

print('/'+ '_' * (2*height - 1) + '\\')

