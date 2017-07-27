import numpy as np
import matplotlib.pyplot as plt

def rosenbrock(x, y, a=1, b=100):
    return (a-x)**2 +b*(y - x**2)**2

def partial_x(func, x, y, h=1e-5):
	return (func(x+h/2, y) - func(x-h/2, y))/h

def partial_y(func, x, y, h=1e-5):
    return (func(x, y+h/2) - func(x, y-h/2))/h


if __name__ == "__main__":

	# Setup meshgrid
	x = np.linspace(-1, 1, 26)
	y = np.linspace(-1, 1, 26)
	X, Y = np.meshgrid(x, y)

	# iterate through grid cells and calculate derivative
	px = partial_x(rosenbrock, X, Y, h=1e-5)
	py = partial_y(rosenbrock, X, Y, h=1e-5)
	pmag = np.sqrt(px**2 + py**2)

	# Plot density plot
	fig = plt.figure(figsize=(8,6))
	ax = fig.add_subplot(1, 1, 1)
	cax = ax.imshow(pmag, extent=(-1, 1, -1, 1), cmap='coolwarm', origin='lower')
	fig.colorbar(cax)

	# Plot quiver
	ax.quiver(X, Y, px, py)

	# labels
	ax.set_xlabel('x', fontsize=16)
	ax.set_ylabel('y', fontsize=16)
	ax.set_title('Force vector field of Rosenbrock potential', fontsize=15)

	plt.show()
