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
   
    # create weights
    w = np.ones(len(y))
    # add multiplicative factors
    w[1:-1:2] *= 4
    w[2:-2:2] *= 2
    
    # Compute sum
    I = (h/3.) * np.dot(y, w)
    
    return I

def trap_int(f, a, b, N=10):
    # Define x-values
    x = np.linspace(a, b, N+1)

    # Get y-values
    y = f(x)

    # Define slice width
    h = (b-a)/float(N)

    # approximate integral
    I = h * (0.5*y[0] + 0.5*y[-1] + sum(y[1:-1]))

    return I

if __name__ == "__main__":
	# Perform comparison
	N = 16

	true_ans = 1.6181944437
	simp_ans = simp_int(func, 0, 15, N=N)
	trap_ans = trap_int(func, 0, 15, N=N)

	print("Simpson w/ {:d} slices accurate to {:.8f}".format(N, simp_ans-true_ans))
	print("Trapezoidal w/ {:d} slices accurate to {:.8f}".format(N, trap_ans-true_ans))


