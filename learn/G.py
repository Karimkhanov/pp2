#First taks(Function1.md)

# def convert_to_ounces():
#     grams = float(input('Enter Gramm to convert to Ounce:'))
#     ounce =  grams / 28.3495231
#     print(ounce)
# convert_to_ounces()



#Second task (Function1.md)

# def convert_to_fahrenheit():
#     F = float(input('Enter Fahrenheit temperature to convert Celsius:'))
#     C = (5 / 9) * (F - 32)
#     print(C)
# convert_to_fahrenheit()



#Third task (Function1.md)

# def solve(numheads, numlegs, chicken, rabbit, error = "No Solution!"):
#     numheads = int(input("Enter heads number:"))
#     numlegs = int(input("Enter legs number:"))
#     #4 legs in rabbit
#     #2 legs in chicken

#     if(numheads>=numlegs):
#         print(error)

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    
    if(heads>=legs):
        print(error_msg)
    elif(legs%2!=0):
        print(error_msg)
    else:
        rabbit_count=(legs-2*heads)/2
        chicken_count=heads-rabbit_count
        print(int(chicken_count),int(rabbit_count))
solve(35,94)





