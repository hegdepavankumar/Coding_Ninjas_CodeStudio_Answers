# Author : Pavankumar Hegde
# Question : Complex Number Class
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118797/offering/1467359
# Solution

class ComplexNumbers:
    
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def plus(self,c):
        
        real = self.real + c.real
        imaginary = self.imaginary + c.imaginary
        
        self.real = real
        self.imaginary = imaginary
        
    def multiply(self,c):
        
        real = (self.real * c.real) - (self.imaginary * c.imaginary)
        imaginary = (self.real * c.imaginary) + (self.imaginary * c.real)
        
        self.real = real
        self.imaginary = imaginary
        
    def print(self):
        
        print(str(self.real) + " + " + "i" + str(self.imaginary))

        
real1,imaginary1 = map(int,input().split(' '))
real2,imaginary2 = map(int,input().split(' '))

C1 = ComplexNumbers(real1,imaginary1)
C2 = ComplexNumbers(real2,imaginary2)
choice = int(input())

if(choice == 1):
    C1.plus(C2)
    C1.print()
    
elif choice == 2:
    C1.multiply(C2)
    C1.print()
    
else:
    pass



