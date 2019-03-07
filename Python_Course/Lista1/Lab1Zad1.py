#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)
import numpy as np
def y(x):
    return 2*x**2 + 2*x + 2

def y2(x):
    return np.absolute(x)
for i in range (-10,11):
    a=y2(i)
    print(a)

#a=2*(56**2)+(2*56)+2;
#b=2*(100**2)+(2*100)+2;
#print(a)
#print(b)