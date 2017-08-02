import numpy as np
import matplotlib.pyplot as plt

# define derivative function
def f(r, t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -g*np.sin(theta)/ell
    return np.array([ftheta, fomega])

# Define RK4 algorithm with error estimate
def RK4_adaptive(f, r1, t1, t2, dt=1e-3, err_tol=1e-4):

    # Define initial condition
    r = r1.copy()

    # define a function for RK4 update
    def rk4_update(r, t, dt):
        # update value using RK4
        k1 = dt * f(r, t)
        k2 = dt * f(r+0.5*k1, t+0.5*dt)
        k3 = dt * f(r+0.5*k2, t+0.5*dt)
        k4 = dt * f(r+k3, t+dt)
        return r + (k1 + 2*k2 + 2*k3 + k4)/6.0

    # Iterate RK4 Method
    t = t1
    theta_points = []
    tpoints = []
    while t < t2:
        # append value of x to xpoints
        theta_points.append(r[0])
        tpoints.append(t)

        # Enter error tolerance loop
        while True:
            ## Calculate estimated error ##
            # double step
            r1_a = rk4_update(r, t, dt)
            r1 = rk4_update(r1_a, t+dt, dt)
            # big step
            r2 = rk4_update(r, t, 2*dt)

            # calculate total error
            eps = np.abs(r1[0] - r2[0])/30.0

            # calculate rho
            rho = (dt*err_tol/eps)**(1./4)

            # evaluate ideal step size
            if rho >= 1.0:
                if rho >= 2.0:
                    rho = 2.0
                break
            else:
                if rho < 0.5:
                    rho = 0.5
                dt *= 0.99*rho

        # update dt
        dt *= 0.99*rho

        # update r to the single step
        r = r1_a.copy()

        # update t
        t += dt
        
    theta_points = np.array(theta_points)
    tpoints = np.array(tpoints)
    
    # fit a line to get exact value when t=t2
    # theta = m*t + b
    m = (theta_points[-2]-theta_points[-1])/(tpoints[-2] - tpoints[-1])
    b = theta_points[-1]-m*tpoints[-1]
    theta_final = m*t2 + b
    tfinal = t2

    return tfinal, theta_final


if __name__ == "__main__":

    # Initial Conditions
    ell = 1.0
    g = 9.81
    r1 = np.array([np.pi/3, 0])

    # create root function
    def angle(v_mag):
	r1 = np.array([np.pi/3, v_mag])

	# run solver
	tfinal, theta_final = RK4_adaptive(f, r1, 0, 3, dt=1e-6, err_tol=1e-12)
	return theta_final

    # Let's just plot the function to get an idea of what it looks like
    v = np.linspace(0,5,100)
    y = np.array(list(map(angle, v)))

    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(1, 1, 1)
    ax.grid(True)
    ax.plot(v, y, linewidth=2)
    ax.set_xlabel('initial angular velocity [rad/s]', fontsize=16)
    ax.set_ylabel(r'$\theta_f(t=3)$', fontsize=18)
    plt.show()

    # use binary search to get root within 4 sig figs
    # define starting points and starting values
    x1 = 0
    x2 = 4
    y1 = angle(x1)
    y2 = angle(x2)

    # define root solution tolerance
    tol = 1e-4

    # binary search!
    while abs(x2-x1) > tol:
	# get midpoint
	xprime = (x1+x2)/2.0
	yprime = angle(xprime)
	# change starting points depending on parity
	if yprime * y1 < 0:
	    x2 = xprime
	    y2 = yprime

	else:
	    x1 = xprime
	    y1 = yprime

    xroot = (x1+x2)/2
    yroot = angle(xroot)

    print("Optimal initial velocity is {:.4f} m/s".format(xroot))


