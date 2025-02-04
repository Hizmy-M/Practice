class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(10, 20)
v2 = Vector(20, 40)
v3 = v1 + v2
print(f'{v3.x} {v3.y}')