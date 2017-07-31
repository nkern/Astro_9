import matplotlib.pyplot as plt
import numpy as np

# Define first derivative
def f(x, t):
    return -x**3 + np.sin(t)

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

    ax.plot(*ode_solve(f, 0, 0, 10, N=200), color='b')
    ax.plot(*ode_solve(f, -1, 0, 10, N=200), color='r')
    ax.plot(*ode_solve(f, 1, 0, 10, N=200), color='g')
    ax.plot(*ode_solve(f, 0, 2, 10, N=200), color='c')

    ax.set_xlabel('t', fontsize=20)
    ax.set_ylabel('x(t)', fontsize=20)

    # display
    plt.show()



