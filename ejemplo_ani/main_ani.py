import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(111)
q = []

def animate(i):
    n = np.random.normal()
    q.append(n)
    ax1.clear()
    ax1.plot(q)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

