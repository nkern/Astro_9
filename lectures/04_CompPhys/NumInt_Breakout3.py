import numpy as np

# Define Function
def func(x):
	return np.sinc(x/np.pi)

# Define simpson integrator
def simp_int(f, a, b, N=10):
	# get width
	h = (b-a)/float(N)

	# generate x-values
	x = np.linspace(a, b, N+1)

	# get y-values
	y = f(x)

	# take half of them for error est
	y1 = y[::2].copy()
	h1 = (b-a)/float(N/2)

	# add multiplicative factors
	y[1:-1:2] *= 4
	y[2:-2:2] *= 2
	y1[1:-1:2] *= 4
	y1[2:-2:2] *= 2

	# Compute sum
	I = (h/3.)*np.nansum(y)
	I1 = (h1/3.)*np.nansum(y1)

	# Estimate error 
	err = np.abs(I-I1)/15.0

	return I, err


if __name__ == "__main__":

	# Define starting N and err tolerance
	N = 10
	err_tol = 1e-5

	# Loop
	while True:
		# Calculate Integral and error estimate
		I, err = simp_int(func, 0, 15, N=N)

		# Break if error tolerance is reached
		if err < err_tol:
			break
		else:
			N += 10


	# Print
	print("Integral of sinc from 0 < x < 15 w/ Simpsons Rule is {:.8f}, w/ estimated err of {:.8f}".format(I, err))

