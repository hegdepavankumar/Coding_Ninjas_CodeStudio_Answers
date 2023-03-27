# Author : Pavankumar Hegde
# Question : Fraction Class
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118797/offering/1467359
# Solution

import math

class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
        
    def print(self):
        print(str(self.numerator) + "/" + str(self.denominator))
        
    
    def simplify(self):
        
        gcd = math.gcd(self.numerator,self.denominator)
        
        self.numerator = self.numerator // gcd
        self.denominator = self.denominator // gcd
        
    def add(self,f2):
        
        lcm = self.denominator * f2.denominator
        x = lcm // self.denominator
        y = lcm // f2.denominator
        
        num = x * self.numerator + (y * f2.numerator)
        
        self.numerator = num
        self.denominator = lcm
        self.simplify()
        
    def multiply(self,f2):
        
        self.numerator = self.numerator * f2.numerator
        self.denominator = self.denominator * f2.denominator
        self.simplify();
        
        
        
        
#Driver's code.

num1,den1 = map(int,input().split(' '))
f = Fraction(num1,den1)
q = int(input())

for i in range(q):
    typ,num2,den2 = map(int,input().split(' '))
    
    if(typ == 1):
        f2 = Fraction(num2,den2)
        f.add(f2)
        f.print()
        
    elif typ == 2:
        f2 = Fraction(num2,den2)
        f.multiply(f2)
        f.print()
        
    else:
        pass
