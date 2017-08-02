import matplotlib.pyplot as plt
import numpy as np

# define derivative function
def f(r, t):
    # unpack array
    x = r[0]
    vx = r[1]
    y = r[2]
    vy = r[3]
    # assign derivatives
    fx = vx
    fvx = -np.pi*R**2*RHO*C/2/m*vx*np.sqrt(vx**2 + vy**2)
    fy = vy
    fvy = -g - np.pi*R**2*RHO*C/2/m*vy*np.sqrt(vx**2 + vy**2)
    # repack
    return np.array([fx, fvx, fy, fvy], dtype=np.float)

# Define RK4 algorithm with error estimate
def RK4_adaptive(f, r1, t1, y2, dt=1e-3, err_tol=1e-4):

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
    xpoints = []
    ypoints = []
    tpoints = []
    while r[2] >= y2:
        
        # append value of x to xpoints
        xpoints.append(r[0])
        ypoints.append(r[2])
        tpoints.append(t)

        # Enter error tolerance loop
        while True:
            ## Calculate estimated error ##
            # double step
            r1_a = rk4_update(r, t, dt).copy()
            r1 = rk4_update(r1_a, t+dt, dt).copy()
            # big step
            r2 = rk4_update(r, t, 2*dt).copy()
            
            # calculate total error
            eps_x = np.abs(r1[0] - r2[0])/30.0
            eps_y = np.abs(r1[2] - r2[2])/30.0
            eps_tot = np.sqrt(eps_x**2 + eps_y**2)
            
            # calculate rho
            rho = (dt*err_tol/eps_tot)**(1./4)

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
        
    xpoints = np.array(xpoints)
    ypoints = np.array(ypoints)
    tpoints = np.array(tpoints)
    return tpoints, xpoints, ypoints



if __name__ == "__main__":

    ### (1) Plot Trajectory w/ Air Resistance ###
    # initial conditions
    g = 9.81
    m = 1
    R = 0.08
    C = 0.47
    RHO = 1.22

    theta0 = 30.0 * np.pi/180
    v_mag = 100
    vx0 = v_mag * np.cos(theta0)
    vy0 = v_mag * np.sin(theta0)
    r1 = np.array([0, vx0, 0, vy0])

    # run solver
    tpoints, xpoints, ypoints = RK4_adaptive(f, r1, 0, 0, dt=1e-3, err_tol=1e-6)

    # figure
    fig = plt.figure(figsize=(8,6))

    # axes
    ax = fig.add_subplot(1, 1, 1)
    ax.tick_params(labelsize=14)
    ax.grid(True)
    ax.plot(xpoints, ypoints, marker='o')
    ax.set_xlabel(r'$x$ [meters]', fontsize=20)
    ax.set_ylabel(r'$y$ [meters]', fontsize=20)
    ax.set_title(r'Trajectory with Air Resistance', fontsize=18)

    ### (2) Plot trajectory w/ and w/o AR ###
    # initial conditions
    g = 9.81
    m = 1
    R = 0.08
    C = 0.47
    RHO = 1.22

    theta0 = 30.0 * np.pi/180
    v_mag = 100
    vx0 = v_mag * np.cos(theta0)
    vy0 = v_mag * np.sin(theta0)
    r1 = np.array([0, vx0, 0, vy0])

    # run solver
    tpoints1, xpoints1, ypoints1 = RK4_adaptive(f, r1, 0, 0, dt=1e-3, err_tol=1e-6)

    # run solver
    C = 0.0001
    tpoints2, xpoints2, ypoints2 = RK4_adaptive(f, r1, 0, 0, dt=1e-3, err_tol=1e-10)

    # figure
    fig = plt.figure(figsize=(8,6))

    # axes
    ax = fig.add_subplot(1, 1, 1)
    ax.tick_params(labelsize=14)
    ax.grid(True)
    p0, = ax.plot(xpoints1, ypoints1, marker='o', color='steelblue')
    p1, = ax.plot(xpoints2, ypoints2, marker='o', color='darkred')
    ax.set_xlabel(r'$x$ [meters]', fontsize=20)
    ax.set_ylabel(r'$y$ [meters]', fontsize=20)
    ax.set_title(r'Trajectory w/ and w/o Air Resistance', fontsize=18)
    ax.legend([p0, p1], ['w/ resistance', 'w/o resistance'], fontsize=16)

    ### (3) Plot Multiple Trajectories w/ AR ###

    # initial conditions
    g = 9.81
    m = 1
    R = 0.08
    C = 0.47
    RHO = 1.22

    theta0 = 10.0 * np.pi/180
    v_mag = 100
    vx0 = v_mag * np.cos(theta0)
    vy0 = v_mag * np.sin(theta0)
    r1 = np.array([0, vx0, 0, vy0])

    # run solver
    tpoints1, xpoints1, ypoints1 = RK4_adaptive(f, r1, 0, 0, dt=1e-3, err_tol=1e-8)

    # run solver
    theta0 = 20.0 * np.pi/180
    v_mag = 100
    vx0 = v_mag * np.cos(theta0)
    vy0 = v_mag * np.sin(theta0)
    r1 = np.array([0, vx0, 0, vy0])
    tpoints2, xpoints2, ypoints2 = RK4_adaptive(f, r1, 0, 0, dt=1e-3, err_tol=1e-8)

    # run solver
    theta0 = 30.0 * np.pi/180
    v_mag = 100
    vx0 = v_mag * np.cos(theta0)
    vy0 = v_mag * np.sin(theta0)
    r1 = np.array([0, vx0, 0, vy0])
    tpoints3, xpoints3, ypoints3 = RK4_adaptive(f, r1, 0, 0, dt=1e-3, err_tol=1e-8)

    # run solver
    theta0 = 35.0 * np.pi/180
    v_mag = 100
    vx0 = v_mag * np.cos(theta0)
    vy0 = v_mag * np.sin(theta0)
    r1 = np.array([0, vx0, 0, vy0])
    tpoints4, xpoints4, ypoints4 = RK4_adaptive(f, r1, 0, 0, dt=1e-3, err_tol=1e-8)

    # run solver
    theta0 = 40.0 * np.pi/180
    v_mag = 100
    vx0 = v_mag * np.cos(theta0)
    vy0 = v_mag * np.sin(theta0)
    r1 = np.array([0, vx0, 0, vy0])
    tpoints5, xpoints5, ypoints5 = RK4_adaptive(f, r1, 0, 0, dt=1e-3, err_tol=1e-8)

    # run solver
    theta0 = 50.0 * np.pi/180
    v_mag = 100
    vx0 = v_mag * np.cos(theta0)
    vy0 = v_mag * np.sin(theta0)
    r1 = np.array([0, vx0, 0, vy0])
    tpoints6, xpoints6, ypoints6 = RK4_adaptive(f, r1, 0, 0, dt=1e-3, err_tol=1e-8)

    # run solver
    theta0 = 60.0 * np.pi/180
    v_mag = 100
    vx0 = v_mag * np.cos(theta0)
    vy0 = v_mag * np.sin(theta0)
    r1 = np.array([0, vx0, 0, vy0])
    tpoints7, xpoints7, ypoints7 = RK4_adaptive(f, r1, 0, 0, dt=1e-3, err_tol=1e-8)

    # figure
    fig = plt.figure(figsize=(8,6))

    # axes
    ax = fig.add_subplot(1, 1, 1)
    ax.tick_params(labelsize=14)
    ax.grid(True)
    p0, = ax.plot(xpoints1, ypoints1, color='steelblue', alpha=0.5)
    p1, = ax.plot(xpoints2, ypoints2, color='darkred', alpha=0.5)
    p2, = ax.plot(xpoints3, ypoints3, color='darkorange', alpha=0.5)
    p3, = ax.plot(xpoints4, ypoints4, color='red', alpha=0.5)
    p4, = ax.plot(xpoints5, ypoints5, color='darkviolet', alpha=0.5)
    p5, = ax.plot(xpoints6, ypoints6, color='k', alpha=0.5)
    p6, = ax.plot(xpoints7, ypoints7, color='darkgreen', alpha=0.5)
    ax.set_xlabel(r'$x$ [meters]', fontsize=20)
    ax.set_ylabel(r'$y$ [meters]', fontsize=20)
    ax.set_title(r'Multiple Trajectories w/ Air Resistance', fontsize=18)
    ax.legend([p0, p1, p2, p3, p4, p5,p6], [r'$\theta=10^\circ$',r'$\theta=20^\circ$',
                                            r'$\theta=30^\circ$',r'$\theta=35^\circ$',
                                            r'$\theta=40^\circ$',r'$\theta=50^\circ$',
                                            r'$\theta=60^\circ$'], fontsize=15)




