# Author : Pavankumar Hegde
# Question : Constructor in Square Class
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118797/offering/1467367?leftPanelTab=0
# Solution


class Square:
    
    def __init__(self,length = 10):
        
        self.length = length
         
    def printArea(self):
        
        print(self.length * self.length)
