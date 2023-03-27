# Author : Pavankumar Hegde
# Question : Sum of even & odd
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118792/offering/1461390?leftPanelTab=0
# Solution 

n = int(input())
evenSum = 0
oddSum = 0

while n > 0:
    
    last = n % 10
    
    #Checking for even case.
    if n % 2 == 0:
        evenSum += last
        
    else:
        #if the number is odd.
        oddSum += last
        
    n = n // 10
    
print(evenSum,oddSum)
