import numpy as np
import matplotlib.pyplot as plt

def dft(y):
    # get number of points
    N = len(y)
    
    # initialize empty array for coefficients
    c = np.zeros(N, dtype=np.complex)
    
    # loop over coefficients, then loop over sum
    for k in range(N):
        for n in range(N):
            # Perform DFT sum
            c[k] += y[n] * np.exp(-1j*2*np.pi*k*n/N)
            
    return c

def idft(c):
    # get number of points
    N = len(c)
    
    # initialize empty array for coefficients
    y = np.zeros(N, dtype=np.complex)
    
    # loop over coefficients, then loop over sum
    for n in range(N):
        for k in range(N):
            # Perform DFT sum
            y[n] += c[k] * np.exp(1j*2*np.pi*k*n/N) / N
            
    return y


if __name__ == "__main__":

    #########################################
    ### Fourier Smoothing with Pitch Data ###
    #########################################

    # load data
    d = np.loadtxt('data/pitch.txt')
    
    # take dft
    c = dft(d)    

    # figure
    fig = plt.figure(figsize=(12,5))
    # axes
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    # plot1
    ax1.plot(d)
    ax1.set_title('pitch', fontsize=14)
    ax1.set_xlabel('time', fontsize=14)
    ax1.set_ylabel('amplitude', fontsize=14)
    # plot 2
    ax2.plot(np.abs(c))
    ax2.set_title('Fourier Transform of pitch', fontsize=14)
    ax2.set_xlabel('k index', fontsize=14)
    ax2.set_ylabel('absolute value of Fourier Coefficients', fontsize=14)
    ax2.set_xlim(-5,500)
    
    plt.show()


    # set low-level coefficients to zero
    select = np.where(np.abs(c) < 100)
    c[select] = 0.0
    d_idft = idft(c).real

    # plot
    fig = plt.figure(figsize=(10,5))
    ax = fig.add_subplot(1,1,1)
    ax.grid(True)
    p1, = ax.plot(d, color='steelblue', alpha=0.75)
    p2, = ax.plot(d_idft, color='darkred', alpha=0.75, linewidth=2)
    ax.set_xlabel('time', fontsize=14)
    ax.set_ylabel('amplitude', fontsize=14)
    ax.legend([p1, p2], ['pitch', 'filtered-pitch'], fontsize=12)

    plt.show()


    #########################################
    ### Detecting Periodicity of Sunspots ###
    #########################################

    # load data
    d = np.loadtxt('data/sunspots.txt')
    c = dft(d[:, 1])

    # plot
    fig = plt.figure(figsize=(13,6))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    ax1.plot(d[:, 1])
    ax1.set_xlabel('months', fontsize=14)
    ax1.set_ylabel('observed sunspots', fontsize=14)
    ax2.plot(np.abs(c))
    ax2.set_xlabel('k index', fontsize=14)
    ax2.set_ylabel('fourier amplitude', fontsize=14)
    ax2.set_xlim(0,100)

    print("period of strongest sinusoid is {:.2f} years".format(len(c)/24.0/12))

    plt.show()

