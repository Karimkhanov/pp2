
'''Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have?'''

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens) + (4 * rabbits) == numlegs:
            return (chickens, rabbits)
    return (None, None)

numheads = int(input())
numlegs = int(input())
chickens, rabbits = solve(numheads, numlegs)
if chickens == None:
    print("There is no solution.")
else:
    print("There are", chickens, "chickens and", rabbits, "rabbits.")
