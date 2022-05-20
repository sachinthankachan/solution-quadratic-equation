#module
from math import*

#inputs
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

#equation
print("quadratic equation is "+str(a)+"x²+"+str(b)+"x+"+str(c),"= 0")

#calculation
D=(b*b)-4*a*c
if (D)<0:
    sqrt=D*-1
else:
    sqrt=D
sqrtcalc=isqrt(int(sqrt))

#roots
x1=(-b+sqrtcalc)/2*a
x2=(-b-sqrtcalc)/2*a
print("roots are",x1,"and",x2)

