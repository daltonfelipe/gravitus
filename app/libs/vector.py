from math import sqrt

class Vector:

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    
    def add(self, vector):
        self.x += vector.x
        self.y += vector.y
        return self

    
    def sub(self, vector):
        self.x -= vector.x
        self.y -= vector.y
        return self

    
    def mult(self, factor_x, factor_y=None):
        if not factor_y:
            factor_y = factor_x
        self.x *= factor_x
        self.y *= factor_y
        return self

    
    def magnitude(self):
        return sqrt(self.x**2 + self.y**2)


    def normalize(self):
        magnitude = self.magnitude()
        self.x /= magnitude
        self.y /= magnitude
        return self

    
    def copy(self):
        return Vector(self.x, self.y)


    def __repr__(self):
        return "[{}, {}]".format(self.x, self.y)