class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width

length, width = map(int, input("Enter length and width: ").split())
rectangle = Rectangle(length, width)
print("Rectangle area:", rectangle.area())

# class Rectangle():
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width

# length, width = map(int, input('Len and width').split())
# rectangle = Rectangle(length, width)
# print('area is equal to', rectangle.area())

