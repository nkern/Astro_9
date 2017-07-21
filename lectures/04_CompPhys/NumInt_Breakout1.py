import numpy as np

# Define Function
def function(x):
	return 4*x**3 - 2*x**2 + 2*x + 5

# Define trap integration 
def trap_int(f, a, b, N=5):
	# Define x-values
	x = np.linspace(a, b, N+1)

	# Get y-values
	y = f(x)

	# Define slice width
	h = (b-a)/float(N)

	# approximate integral
	I = h * (0.5*y[0] + 0.5*y[-1] + sum(y[1:-1]))

	return I


# Perform integration!
I_approx = trap_int(function, -1, 1, N=100)

# Exact value
I = 8 + 2./3

# Error
print("We recover I to an accuracy of {:.5f}".format(np.abs(I-I_approx)))

