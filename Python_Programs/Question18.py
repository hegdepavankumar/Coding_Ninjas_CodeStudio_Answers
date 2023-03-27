# Author : Pavankumar Hegde
# Question : Rotate array
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118794/offering/1461405?leftPanelTab=0
# Solution



def rotateArray(arr,n,k):
    
    for i in range(k):
        temp = arr[0]
        
        for j in range(n - 1):
            arr[j] = arr[j + 1]
            
        arr[n - 1] = temp
        
        

        
        
        
        
        


length = int(input())
arr = [int(i) for i in input().split()]
k = int(input())

rotateArray(arr,length,k)
print(*arr)
 