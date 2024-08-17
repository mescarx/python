class rectangle:
 def __init__(self,l,b):
  self.l=l
  self.b=b
 def rarea(self):
  return(self.l*self.b)
 def rperi(self):
  return(2*(self.l+self.b))
len=int(input("enter length : "))
bre=int(input("enter breadth : "))
r=rectangle(len,bre)
ar=r.rarea()
pe=r.rperi()
print("area of rectangele = ",ar)
print("perimeter of rectangle =",pe)

