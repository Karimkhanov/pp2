# class Words():
#     def __init__(self):
#         pass

#     def long_word(self,long):
#         return long + long

# sh = Words()
# print(sh.long_word(str(input())))

import math

def degree_to_radian(degree):
    radian = (degree * math.pi) / 180
    return radian

degree = 15
radian = degree_to_radian(degree)

print("Input degree:", degree)
print("Output radian:", radian)


    
    