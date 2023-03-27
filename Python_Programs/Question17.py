# Author : Pavankumar Hegde
# Question : Reverse the array
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118794/offering/1461404?leftPanelTab=0
# Solution 




def reverseArray(arr,start,end,length):
    
    while start < end:
        
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
        
        

        
            


length = int(input())
arr = [int(i) for i in input().split()]

reverseArray(arr,0,length - 1,length)
print(*arr)

