# Author : Pavankumar Hegde
# Question : Set Bits
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118793/offering/1461399?leftPanelTab=0
# Solution 

def countBits(n):
    
    count = 0

    while (n > 0):
        
        r = n % 2
        if r == 1:
            count += 1
            
        n = n // 2
        
    return count



        
n = int(input())
print(countBits(n))

