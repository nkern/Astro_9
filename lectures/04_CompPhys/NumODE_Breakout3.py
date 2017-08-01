import numpy as np
import matplotlib.pyplot as plt

def f(r, t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -g*np.sin(theta)/ell
    return np.array([ftheta, fomega])

def RK4(f, r1, t1, t2, N=10):
    # Define bounds and step-sizes
    dt = float(t2 - t1) / N
    
    # Make t-points
    tpoints = np.linspace(t1, t2, N+1)

    # Define initial condition
    r = r1.copy()

    # Iterate RK4 Method
    theta_points = []
    for t in tpoints:
        # append value of x to xpoints
        theta_points.append(r[0])

        # update value using RK4
        k1 = dt * f(r, t)
        k2 = dt * f(r+0.5*k1, t+0.5*dt)
        k3 = dt * f(r+0.5*k2, t+0.5*dt)
        k4 = dt * f(r+k3, t+dt)

        r += (k1 + 2*k2 + 2*k3 + k4)/6.0

    theta_points = np.array(theta_points)
    return tpoints, theta_points


if __name__ == "__main__":

    # set constants and initial conditions
    ell = 0.1
    g = 9.8
    r1 = np.array([np.pi/3, 0])

    # run method
    tpoints, theta_points = RK4(f, r1, 0, 5, N=300)

    # plot
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(1,1,1)
    ax.grid(True)
    ax.plot(tpoints, theta_points, marker='o')
    ax.set_xlabel('time [sec]', fontsize=18)
    ax.set_ylabel(r'$\theta$ [rad]', fontsize=18)

    # show
    plt.show()

    ## Change Initial Conditions ##
    tpoints1, theta_points1 = RK4(f, r1, 0, 5, N=150)
    tpoints2, theta_points2 = RK4(f, r1, 0, 5, N=60)
    tpoints3, theta_points3 = RK4(f, r1, 0, 5, N=30)

    # plot
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(1,1,1)
    ax.grid(True)
    p1, = ax.plot(tpoints1, theta_points1, marker='o', color='steelblue')
    p2, = ax.plot(tpoints2, theta_points2, marker='o', color='darkorange')
    p3, = ax.plot(tpoints3, theta_points3, marker='o', color='darkred')
    ax.set_xlabel('time [sec]', fontsize=18)
    ax.set_ylabel(r'$\theta$ [rad]', fontsize=18)
    ax.legend([p1, p2, p3], ['N=100', 'N=45', 'N=30'])
   
    # show
    plt.show()

    ## Change IC ##
    r1 = np.array([np.pi/1.01, 0])

    # run method
    tpoints, theta_points = RK4(f, r1, 0, 5, N=300)

    # plot
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(1,1,1)
    ax.grid(True)
    ax.plot(tpoints, theta_points, marker='o')
    ax.set_xlabel('time [sec]', fontsize=18)
    ax.set_ylabel(r'$\theta$ [rad]', fontsize=18)
    ax.set_title(r'$\theta_0 = \pi/1.01$', fontsize=16)
    
    # show
    plt.show()





