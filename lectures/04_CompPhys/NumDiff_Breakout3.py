import numpy as np
from NumDiff_Breakout1 import func

def central_second_deriv(func, x, h=1e-5):
	return (func(x+h) - 2*func(x) + func(x-h)) / h**2


def central_second_deriv_sampled(fxph, fx, fxmh, h):
	"""
	fxph : f(x plus h)
	fx : f(x)
	fxmh : f(x minus h)
	"""
	return (fxph - 2*fx + fxmh)/h**2

if __name__ == "__main__":
	# Derivative
	h = 1e-5
	print("central-difference second derivative with h = {} has error = {}".format(h, -2-central_second_deriv(func, 1, h=h)))

	# load freefall data
	time, pos = np.loadtxt('freefall.txt', delimiter=',', unpack=True)
	dt = time[1] - time[0]

	# Get second derivative at three points
	sec_deriv = []
	for i in range(len(pos))[1:-1]:
		sec_deriv.append(central_second_deriv_sampled(pos[i-1], pos[i], pos[i+1], dt))

	print("The gravitational acceleration near the Earth's surface is roughly {:.5f} m/sec^2".format(np.mean(sec_deriv)))


