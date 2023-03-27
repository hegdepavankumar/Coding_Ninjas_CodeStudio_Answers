# Author : Pavankumar Hegde
# Question : Count Words
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118795/offering/1461408
# Solution


from sys import stdin


def countWords(string) :
	# Your code goes here
    
    if len(string) == 0:
        return 0
    
    count = 0
    for i in string:
        if i == ' ':
            count += 1
            
            
    return count + 1



#main
string = stdin.readline().strip();
count = countWords(string)

print(count)


