from matplotlib import pyplot as plt
import numpy as np

if __name__=='__main__':
	###CONSTANTS###
	A = 1.0 # amplitude
	k = 20.0 # spring constant
	m = 5.0 # mass
	total_time = 10.0
	timesteps = 10000
	time_size = total_time/timesteps
	###CONSTANTS###
	
	t = np.linspace(0, total_time, timesteps)
	a = [-1*A*k/m]
	v = [0]
	x = [A]
	
	i = 1
	while i < len(t):
		x.append(v[-1] * time_size + 0.5 * a[-1] * time_size ** 2 + x[-1])
		a.append(-1 * k * x[-1] / m)
		v.append(v[-1] + a[-2] * time_size)
		i += 1	

	plt.plot(t, x)
	plt.yscale('linear')
	plt.show()
