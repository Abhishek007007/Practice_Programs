class RECTANGLE:
    def __init__(self,height,width,corner_x,corner_y):
        self.height = height
        self.width = width
        self.corner_x = corner_x
        self.corner_y = corner_y
    
    def center(self):
        center_x = self.corner_x + self.width / 2
        center_y = self.corner_y + self.height / 2
        return (center_x,center_y)
    
    def area(self):
        area1 = self.height * self.width
        return area1
    
    def perimeter(self):
        peri = 2 * (self.height + self.width)
        return peri
    

rect1 = RECTANGLE(5,7,0,0)
print("center = ",rect1.center())
print("Area = ",rect1.area())
print("Perimeter = ", rect1.perimeter())