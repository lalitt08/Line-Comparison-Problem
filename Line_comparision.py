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
    
p1 = Point(1, 2) 
p2 = Point(4, 6) 

line = Line(p1, p2)
print("Length of the line:", line.calculate_length())