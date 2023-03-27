# Author : Pavankumar Hegde
# Question : Remove character
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118795/offering/1461414?leftPanelTab=0
# Solution




def removeAllOccurrencesOfChar(string,c):
    
    output = ""
    
    for i in string:
        
        if i != c:
            output += i
            
            
    return output



string = input()
c = input()
output = removeAllOccurrencesOfChar(string,c)
print(output)



