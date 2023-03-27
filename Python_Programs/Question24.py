# Author : Pavankumar Hegde
# Question : Check Permutation
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118795/offering/1461411?leftPanelTab=0
# Solution




def isPermutation(string1, string2) :
    
    if len(string1) != len(string2):
        return False
    
    string1 = sorted(string1)
    string2 = sorted(string2)
    
    i = 0
    j = 0
    
    while i < len(string1) and j < len(string2):
        
        if string1[i] != string2[j]:
            return False
        
        i += 1
        j += 1
        
        
    return True




#main
string1 = input()
string2 = input()

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

