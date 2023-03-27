# Author : Pavankumar Hegde
# Question : Reverse String Word Wise
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118795/offering/1461410?leftPanelTab=0
# Solution



def reverseStringWordWise(string):
    
    string = string.split(' ')
    
    
    i = 0
    j = len(string) - 1
    
    while i < j:
        
        string[i],string[j] = string[j],string[i]
        i += 1
        j -= 1
        
        
    answer = ""
    for i in string:
        answer += i
        answer += " "
        
    return answer


string = input()
ans = reverseStringWordWise(string)
print(ans)
        
