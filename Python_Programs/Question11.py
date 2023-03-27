# Author : Pavankumar Hegde
# Question : Total Prime
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118793/offering/1461401
# Solution 

def totalPrime(S,E):
    
    count = 0

    for i in range(S,E + 1):

        flag = True
        for j in range(2,i):
            
            #if i is divisble by j set the flag value to False and break.
            if i % j == 0:
                flag = False
                break
                
        #if flag is True increase the value of count by 1.
        if flag:
            count += 1

    return count
    
#Taking S and E space seperated input.
S,E = map(int,input().split(' '))
print(totalPrime(S,E))



