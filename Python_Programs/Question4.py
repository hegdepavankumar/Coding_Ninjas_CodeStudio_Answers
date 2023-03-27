# Author : Pavankumar Hegde
# Question : Calculate Simple Interest
# Question Link : https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118790/offering/1461387?leftPanelTab=0
# Solution 

#Take the input.

principal = int(input())
rate = float(input())

time = int(input())

#calculating the si using mathematical formula si = (p * r * t) / 100
si = int((principal * rate * time) / 100)


print(si)
