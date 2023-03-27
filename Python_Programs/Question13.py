# Author : Pavankumar Hegde
# Question : Print all Divisors of a number
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118793/offering/1461396
# Solution 


def printDivisors(n):
    
    for i in range(1,n + 1):
        if n % i == 0:
            print(i,end = " ")




            
n = int(input())
printDivisors(n)

