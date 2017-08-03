import numpy as np
import matplotlib.pyplot as plt

def sine_series(x, n=10):
    L = 1.0
    k_array = np.arange(1, n+1)
    beta_array = -1/(np.pi*k_array) * (-1)**(k_array)
    sine_array = np.sin(2*np.pi*k_array*x/L)
    return sum(beta_array * sine_array)

def sine_series_vec(x, n=10):
    L = 1.0
    k_array = np.arange(1, n+1)
    beta_array = -1/(np.pi*k_array) * (-1)**(k_array)
    sine_array = np.array(list(map(lambda t: np.sin(2*np.pi*t*x/L), k_array)))
    return np.dot(beta_array, sine_array)

if __name__ == "__main__":

    # generate x values
    x = np.linspace(-0.5, 0.5, 1000)

    # get yvalues for each sine series and sawtooth
    f = x
    y1 = sine_series_vec(x, n=1)
    y2 = sine_series_vec(x, n=3)
    y3 = sine_series_vec(x, n=5)
    y4 = sine_series_vec(x, n=10)
    y5 = sine_series_vec(x, n=100)

    # plot
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(1, 1, 1)
    ax.tick_params(labelsize=12)
    ax.grid(True)
    ax.set_xlabel('x', fontsize=18)
    ax.set_ylabel('y', fontsize=18)

    p0, = ax.plot(x, f, color='k', linewidth=2, alpha=0.75)
    p1, = ax.plot(x, y1, alpha=0.75)
    p2, = ax.plot(x, y2, alpha=0.75)
    p3, = ax.plot(x, y3, alpha=0.75)
    p4, = ax.plot(x, y4, alpha=0.75)
    p5, = ax.plot(x, y5, alpha=0.75)

    ax.legend([p1, p2, p3, p4, p5], ['n=1', 'n=3', 'n=5', 'n=10', 'n=100'], fontsize=12)

    plt.show()


