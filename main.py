#module
import cmath
from colorama import Fore

#inputs
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

#error checks
if a==0:
    print("a can't be 0")
    a=int(input("a:"))

#equation
print("quadratic equation is "+Fore.YELLOW+str(a)+"x²+"+str(b)+"x+"+str(c),"= 0")
print(Fore.WHITE)

#calculation of discriminant
D=(b*b)-4*a*c
sqrtcalc=cmath.sqrt(int(D))

#calculating roots
x1=(-b+sqrtcalc)/2*a
x2=(-b-sqrtcalc)/2*a
print("roots are "+Fore.RED+str(x1)+Fore.WHITE+" and "+Fore.RED+str(x2))

