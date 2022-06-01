
class Rectangle:
    def __init__(self,width,height):
        self.name = self
        self.width = width
        self.height = height

    #define what should happen if the object is printed
    def __str__(self):
        return 'Rectangle(width=' + str(self.width)+ ', height=' + str(self.height) + ')'

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area 

    def get_perimeter(self):
        self.perimeter = ((2*self.width) + (2*self.height))
        return self.perimeter

    def get_diagonal(self):
        self.diagonal = (((self.width **2) + (self.height**2)) ** .5)
        return self.diagonal

    #generates a picture of asterisks equal to the height and width of the rectangle
    def get_picture(self):
        count = 0
        line = ""
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        else:
            while count < self.height:
                line += '*'*(self.width)+'\n'
                count +=1
            return line

    def get_amount_inside(self,shape):
        shape_count = int(self.get_area() / shape.get_area())
        return shape_count
        

#Square is a subclass of Rectangle, but always ensures provided dimensions retain same length on all four sides.
class Square(Rectangle):
    def __init__(self,length):
        self.name = self
        self.width = self.height = length
    
    def __str__(self):
        return 'Square(side=' + str(self.width)+')'

    def set_side(self,length):
        self.width = self.height = length
    
    def set_width(self,length):
        self.width = self.height = length

    def set_height(self,length):
        self.width = self.height = length



rect = Rectangle(100, 100)
print(rect.get_area())
print(rect.get_picture())

sq = Square(4)
print(sq.get_area())
sq.set_side(4)
sq.set_height(4)
print(sq.get_diagonal())
print(sq)

print(rect.get_amount_inside(sq))
