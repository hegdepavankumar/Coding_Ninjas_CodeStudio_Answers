# Author : Pavankumar Hegde
# Question : All substrings
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118795/offering/1461409?leftPanelTab=0
# Solution




def printSubstrings(string) :

    n = len(string)

    for i in range(n) :
        for j in range(i, n) :
            for k in range(i, (j + 1)) :
                print(string[k], end = "")

            print()


            

            
            
            
#main
string = input();
printSubstrings(string)
