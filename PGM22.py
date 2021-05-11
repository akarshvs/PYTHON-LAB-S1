# 22. Create Rectangle class with attributes length and breadth and methods to find area and
# perimeter. Compare two Rectangle objects by their area.

class Rectangle:
    def __init__(self ,n):
        self.n = n
        self.l = float(input(f'\nLENGTH OF {n}: '))
        self.b = float(input(f'BREADTH OF {n}: '))
    def area(self):
        return float(self.l * self.b)
    def peri(self):
        return  float(2 * (self.l + self.b)) 

r1 = Rectangle('R1')
r2 = Rectangle('R2')

print(f'\nAREA OF R1: {r1.area():.2f} cm^2')
print(f'PERIMETER OF R1: {r1.peri():.2f} cm')

print(f'\nAREA OF R2: {r2.area():.2f} cm^2')
print(f'PERIMETER OF R2: {r2.peri():.2f} cm')


if (r1.area() == r2.area()):
    print('\nAREA OF R1 AND AREA OF R2 ARE EQUAL')
else:
    print('\nAREA OF R1 AND AREA OF R2 ARE NOT EQUAL')
    print({True: "R1 HAS GREATER AREA", False: "R2 HAS GREATER AREA"}[r1.area() > r2.area()])

