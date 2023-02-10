import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


x1, y1 = map(int, input("Enter the x and y coordinates of point1: ").split())
x2, y2 = map(int, input("Enter the x and y coordinates of point2: ").split())

point1 = Point(x1, y1)
point2 = Point(x2, y2)

point1.show()
point2.show()

print("Distance between point1 and point2:", point1.dist(point2))

dx, dy = map(int, input("Enter the delta x and delta y values: ").split())
point1.move(dx, dy)
print("Point1 after moving:")
point1.show()


# Output:
# Point coordinates: (0, 0)
# Point coordinates: (3, 4)
# Distance between point1 and point2: 5.0
# Point1 after moving:
# Point coordinates: (1, 1)
