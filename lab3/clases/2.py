class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
        
    def area(self):
        return self.length * self.length

# Create a Shape object
shape = Shape()
print("Shape area:", shape.area())

# Create a Square object
square = Square(int(input()))
print("Square area:", square.area())

