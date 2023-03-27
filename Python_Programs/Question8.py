# Author : Pavankumar Hegde
# Question : Find power of a number
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118792/offering/1461391?leftPanelTab=0
# Solution 


x,n = map(int,input().split())

ans = 1

while n > 0:
    
    ans *= x
    
    n -= 1
    
print(ans)






