# Author : Pavankumar Hegde
# Question : Swap Two Numbers
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118790/offering/1461386?leftPanelTab=0
# Solution 

'''
    Time complexity: O(1)
    Space complexity: O(1).
'''

def swap(a, b):
    temp = 0
    # Store the value of a in temp.
    temp = a
    # Make a equal to b.
    a = b
    # Make b equal to temp.
    b = temp
    
    return a, b