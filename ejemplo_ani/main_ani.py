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
    ax1.plot(q[-20:])
    
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

# Dudas obligatorias jueves 19
#  fecha correcta! -> Para el viernes 20 de Marzo
