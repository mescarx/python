'''
wap to find  the factorial of given number.
'''
'''
num=int(input("enter the number :"))
fact=1
while num>0:
	fact=fact*num
	num=num-1
print("factorial=",fact)
'''
import math

num = int(input("Enter a number: "))
result = math.factorial(num)
print("The factorial of", num, "is", result)