# Author : Pavankumar Hegde
# Question : Factorial of a Number
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118792/offering/1461392?leftPanelTab=0
# Solution 



n = int(input())

if n < 0:
    print("Error")
    
elif n == 0:
    print(1)
    
else:
    i = n
    fact = 1
    
    while(n // i != n):
        
        fact = fact * i
        i -= 1
        
    print(fact)
