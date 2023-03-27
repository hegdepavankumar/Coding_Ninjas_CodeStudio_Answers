# Author : Pavankumar Hegde
# Question : Last index of element
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118794/offering/1461403?leftPanelTab=0
# Solution 




def firstIndex(arr,n,target):
    
    index = -1
    
    for i in range(n - 1,-1,-1):
        
        if arr[i] == target:
            index = i
            break
        
        
    return index






length = int(input())
arr = [int(i) for i in input().split()]
target = int(input())

print(firstIndex(arr,length,target))



