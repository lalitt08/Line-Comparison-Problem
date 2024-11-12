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
        return self.calculate_length() == other.calculate_length()

    def __lt__(self, other):
        return self.calculate_length() < other.calculate_length()

    def __gt__(self, other):
        return self.calculate_length() > other.calculate_length()

    def shorter_or_equal(self, other):
        return self.calculate_length() <= other.calculate_length()

    def greater_or_equal(self, other):
        return self.calculate_length() >= other.calculate_length()
    

p1 = Point(1, 2) 
p2 = Point(4, 6) 
p3 = Point(1, 2)
p4 = Point(4, 6)

line1 = Line(p1, p2)
line2 = Line(p3, p4)

print("Line 1 length:", line1.calculate_length())
print("Line 2 length:", line2.calculate_length())
print("Is Line 1 equal to Line 2?", line1 == line2)
print("Is Line 1 less than Line 2?", line1 < line2)
print("Is Line 1 greater than Line 2?", line1 > line2)