# Author : Pavankumar Hegde
# Question : Remove Consecutive Duplicates
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118795/offering/1461412?leftPanelTab=0
# Solution

from sys import stdin

def removeConsecutiveDuplicates(string) :
    n = len(string)

    if n == 0 :
        return string

    answer = string[0]
    i = 1
    
    while i < len(string):
        
        if string[i] != string[i - 1]:
            answer += string[i]
            
        i += 1
        
    return answer
            


#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
