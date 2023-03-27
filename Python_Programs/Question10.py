# Author : Pavankumar Hegde
# Question : N-th Fibonacci Number
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118792/offering/1461392?leftPanelTab=0
# Solution 

'''
    Time complexity: O(2^N)
    Space complexity: O(N) 

    Where 'N' reprents the "Nth" number .
'''

def fibonacciNumber(n):
    
    mod = int(1e9 + 7)

    # Base Case
    if (n <= 1):
        return n
    
    # Recursive call
    return (fibonacciNumber(n - 1) + fibonacciNumber(n - 2)) % mod
