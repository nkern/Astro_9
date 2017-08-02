## Boundary Value Problem, Breakout 1
import numpy as np

# define function
def f(r):
    return G*M/r**2 - G*m/(R-r)**2 - omega**2*r

G = 6.67e-11
M = 5.9e24
m = 7.34e22
R = 3.8e8
omega = 2.6e-6

# define starting points and starting values
x1 = R/100
x2 = R*0.999
y1 = f(x1)
y2 = f(x2)

# define root solution tolerance
tol = 1e-4

# binary search!
while abs(x2 - x1) >= tol:
    # get midpoint
    xprime = (x1 + x2)/2.0
    yprime = f(xprime)
    # change starting points depending on parity
    if yprime * y1 > 0:
        x1 = xprime
        y1 = yprime
    else:
        x2 = xprime
        y2 = yprime
        
xroot = (x1 + x2)/2
yroot = f(xroot)

print("Earth-Moon L1 point lies {:.0f} km away from center of Earth".format(xroot/1e3))
