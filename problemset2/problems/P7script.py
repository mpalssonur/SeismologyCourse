import numpy as np
import matplotlib.pyplot as plt

t = 0
dx = 1
dt = 0.1
tlen = 5
beta = 4
u1 = np.zeros(101)
u2 = np.zeros(101)
u3 = np.zeros(101)
fig, axs = plt.subplots(3,3, figsize=(10,10))
pltno = 0

while t <= 33:
    t += dt
    
    for i in range(1,100):
        rhs = (beta**2)*(u2[i+1] - 2*u2[i] + u2[i-1])/dx**2
        u3[i] = (dt**2)*rhs + 2*u2[i] - u1[i]
    
    u3[0] = u3[1]
    u3[100] = 0
    if t <= tlen:
        u3[50] = np.sin(np.pi * t / tlen)**2
    
    u1 = np.copy(u2)
    u2 = np.copy(u3)

    if np.abs((t % 4) - 1.0) < 1e-4:
        py = pltno // 3
        px = pltno % 3
        axs[px, py].plot(np.arange(101), u2)
        axs[px, py].set_title("t = " + str(np.round(t,decimals=0)) + "s")
        axs[px, py].set_ylim(-1.1, 1.1)
        pltno += 1

fig.tight_layout()
plt.savefig('problemset2/problems/figures/P7output.png')