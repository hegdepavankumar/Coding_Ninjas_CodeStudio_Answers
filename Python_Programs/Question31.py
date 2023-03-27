# Author : Pavankumar Hegde
# Question : Area of a Rectangle
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118797/offering/1467364?leftPanelTab=0
# Solution


'''

    Time Complexity: O(1)
    Space Complexity: O(1)
'''

class Rectangle:
    
    def __init__(self):
        self.length = 0
        self.breadth = 0
        
    def getArea(self):
        area = self.length * self.breadth
        return area
    
