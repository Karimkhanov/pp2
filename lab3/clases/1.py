
class StringHandler:
    def __init__(self):
        self.string = ""
        
    def getString(self):
        self.string = input("Enter a string: ")
        
    def printString(self):
        print(self.string.upper())

sh = StringHandler()
sh.getString()
sh.printString()
