# Author : Pavankumar Hegde
# Question : Reverse Each Word
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118795/offering/1461413?leftPanelTab=0
# Solution

from sys import stdin



def reverseWord(string, start, end) :

    reverse = ""

    while start < end :
        reverse = string[start] + reverse
        start += 1
        
    

    return reverse


def reverseEachWord(string) :
    
    n = len(string)
    previousSpaceIndex = -1

    ans = ""

    i = 0
    while i < n :
        if string[i] == ' ' :
            ans += (reverseWord(string, previousSpaceIndex + 1, i) + " ")
            previousSpaceIndex = i

        i += 1

    ans += (reverseWord(string, previousSpaceIndex + 1, i) + " ")

    return ans



#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
