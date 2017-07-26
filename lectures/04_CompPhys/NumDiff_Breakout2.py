import numpy as np
import matplotlib.pyplot as plt
from NumDiff_Breakout1 import *

if __name__ == "__main__":
	## Calculate Error
	H = np.logspace(-2, -12, 400)

	for_err = []
	bac_err = []
	cen_err = []
	for h in H:
		for_err.append( np.abs(-3 - forward_diff(func, 1.0, h=h) ) )
		bac_err.append( np.abs(-3 - backward_diff(func, 1.0, h=h) ) )
		cen_err.append( np.abs(-3 - central_diff(func, 1.0, h=h) ) )


	## Plot

	# Figure
	fig = plt.figure(figsize=(7,7))
	ax = fig.add_subplot(1, 1, 1)
	ax.grid(True)

	# Errors
	p1 = ax.plot(H, for_err, color='steelblue', linewidth=5, alpha=0.9)
	p2 = ax.plot(H, bac_err, color='darkorange', linewidth=2, alpha=0.9)
	p3 = ax.plot(H, cen_err, color='indianred', linewidth=3, alpha=0.9)

	# labels
	ax.set_xlabel(r'$h$', fontsize=18)
	ax.set_ylabel(r'$\epsilon$', fontsize=18)
	ax.set_xscale('log')
	ax.set_yscale('log')
	ax.set_title(r'Finite Difference Derivative Error', fontsize=14)
	ax.legend([p1[0], p2[0], p3[0]], ['forward', 'backward', 'central'], fontsize=12)

	plt.show()
