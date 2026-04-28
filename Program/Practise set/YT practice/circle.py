
class Circle :
    def __init__ (self,radius):
        self.radius = radius

    def Area(self):
        return 3.14 * self.radius **2
    
    def Perimeter(self):
        return 3.14 * self.radius

c1 = Circle(5)
print("The area of circle",c1.Area())
print(int("The perimeter of circle is",c1.Perimeter()))


