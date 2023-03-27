# Author : Pavankumar Hegde
# Question : Print Name and age
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118797/offering/1467363?leftPanelTab=0
# Solution


class Person:
    
    def __init__(self):
        self.name = ""
        self.age = ""
        
    def setValue(self,name,age):
        self.name = name
        self.age = age
        
    def getValue(self):
        print("The name of the person is " + self.name + " and the age is " + age + ".")
        

    

    
P = Person()
name = input()
age = input()
P.setValue(name,age)
P.getValue()
        
        
