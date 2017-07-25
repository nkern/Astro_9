import matplotlib.pyplot as plt
import numpy as np

# Define simpson integrator
def simp_int_err(f, a, b, N=10):
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

def gauss(x):
	return np.exp(-(x-mu)**2/2/sig**2) / np.sqrt(2*np.pi*sig**2)

def gauss_inf(z):
	x = z / (1-z**2)
	return gauss(x) * (1+z**2) / (1-z**2)**2

if __name__ == "__main__":

	### (1) ###
	# choose err tolerance
	err_tol = 1e-4

	# choose starting N
	N = 10

	# choose gaussian parameters
	mu = 0
	sig = 2

	# loop
	while True:
		# Calculate Integral
		I, err = simp_int_err(gauss_inf, -1, 1, N=N)

		# Check error tolerance
		if err < err_tol:
			break

		else:
			N += 10

	print("Integral should be 1, we find {:.8f} using {} slices".format(I, N))


	### (2) ###
	# Integrate Gaussian from -sig to sig
	I, err = simp_int_err(gauss, -sig, sig, N=N)

	print("Integral of Gaussian from -sig < x < sig is {:.6f}".format(I))
	print("This represents the probability of a single draw falling within this range")


	### Bonus ###
	I, err = simp_int_err(gauss, -5*sig, 5*sig, N=N*5)
	prob = 1 - I

	print("The probability of single draw falling outside of -5sigma < x < 5sigma is {:.9f}".format(prob))
	draws = 1/prob
	print("Statistically speaking, to get a single sample outside of this range, we need to make {:.0f} draws".format(draws))

