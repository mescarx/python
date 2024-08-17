#execption handling
'''
try:
 
  a=eval(input("enter the first no: "))
  b=eval(input("enter the first no: "))
  c=a+b
  print("sum = ",c)
except NameError:
  print("enter numbers only ")
'''
a=eval(input("enter the first no: "))
b=eval(input("enter the first no: "))
c=a/b
print("divide = ",c)
'''
except NameError:
  print("enter numbers only ")
except ZeroDivisonError:
  print("bhai tum pogo dekho")
finally:
  print("way down we go")
'''