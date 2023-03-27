# Author : Pavankumar Hegde
# Question : Fahrenheit to Celsius
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118792/offering/1461389
# Solution 

#Take the input of S,E and W.

S = int(input())
E = int(input())
W = int(input())

#Iterating over the loop with given step size as W. 

for currentFahrenhietValue in range(S,E + 1,W):

    celcius = int((currentFahrenhietValue - 32) * 5 /9)

    print(currentFahrenhietValue,celcius,sep = "\t")
    
