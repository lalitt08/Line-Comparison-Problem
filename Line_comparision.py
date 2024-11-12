import math
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y  
    
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1  
        self.p2 = p2  

    def calculate_length(self):
        length = math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)
        return length
    
    def __eq__(self, other):
        if isinstance(other, Line):
            return (self.p1 == other.p1 and self.p2 == other.p2) or \
                   (self.p1 == other.p2 and self.p2 == other.p1)
        return False
    

p1 = Point(1, 2) 
p2 = Point(4, 6) 
p3 = Point(1, 2)
p4 = Point(4, 6)

line1 = Line(p1, p2)
line2 = Line(p3, p4)
print("lines are equal",line1==line2)