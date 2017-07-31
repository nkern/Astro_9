import matplotlib.pyplot as plt
import numpy as np

# Define first derivative
def f(x, t):
        return -x**3 + np.sin(t)

def RK4(f, x1, t1, t2, N=10):
    # Define bounds and step-sizes
    dt = float(t2 - t1) / N

    # Make t-points
    tpoints = np.linspace(t1, t2, N+1)

    # Define initial condition
    x = x1

    # Iterate Euler's Method to get x(t)
    xpoints = []
    for t in tpoints:
        # append value of x to xpoints
        xpoints.append(x)

        # update value using RK4
        k1 = dt * f(x, t)
        k2 = dt * f(x+0.5*k1, t+0.5*dt)
        k3 = dt * f(x+0.5*k2, t+0.5*dt)
        k4 = dt * f(x+k3, t+dt)

        x += (k1 + 2*k2 + 2*k3 + k4)/6.0
    
    xpoints = np.array(xpoints)
    return tpoints, xpoints

# define ode solve
def ode_solve(f, x1, t1, t2, N=100):
    # Define bounds and step-sizes
    dt = float(t2 - t1) / N

    # Make t-points
    tpoints = np.linspace(t1, t2, N+1)

    # Define initial condition
    x = x1

    # Iterate Euler's Method to get x(t)
    xpoints = []
    for t in tpoints:
	# append value of x to xpoints
	xpoints.append(x)

	# update value using Euler's method
	x += dt * f(x, t)

    return tpoints, xpoints



if __name__ == "__main__":

    # plot
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(1, 1, 1)

    ax.grid(True)
    ax.set_xlim(-1,11)
    ax.set_ylim(-1.2, 1.2)

    ax.plot(*RK4(f, 0, 0, 10, N=20), color='b')
    ax.plot(*ode_solve(f, 0, 0, 10, N=200), color='r')

    ax.set_xlabel('t', fontsize=20)
    ax.set_ylabel('x(t)', fontsize=20)

    # display
    plt.show()


