# Author : Pavankumar Hegde
# Question : First index of element
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118794/offering/1461402
# Solution 

def firstIndex(arr,n,target):
    
    index = -1
    
    for i in range(n):
        
        if arr[i] == target:
            return i
        
        
    return -1






length = int(input())
arr = [int(i) for i in input().split()]
target = int(input())

print(firstIndex(arr,length,target))

