import numpy as np


def forward_diff(func, x, h=1e-4):

    return (func(x+h) - func(x)) / h
    
    
def backward_diff(func, x, h=1e-4):
    
    return (func(x) - func(x-h)) / h

def central_diff(func, x, h=1e-4):
    
    return (func(x+h/2) - func(x-h/2)) / h

def func(x):
	return x**3 - 4*x**2 + 2*x

if __name__ == "__main__":
	## Take Derivative ##
	h = 1e-4
	print("Forward Diff w/ h={} is {:.8f}".format(h, forward_diff(func,1,h=h)))
	print("Backward Diff w/ h={} is {:.8f}".format(h, backward_diff(func,1,h=h)))
	print("Central Diff w/ h={} is {:.8f}".format(h, central_diff(func,1,h=h)))
