import numpy as np

n = np.array([np.cos(10 * np.pi / 180), - np.sin(10 * np.pi / 180)])

sigma = np.array([[-30, -20],[-20, -40]])

tn = sigma.dot(n)
t_N = tn.dot(n)
t_S = np.sqrt(np.linalg.norm(tn)**2 - t_N**2)

w, V = np.linalg.eig(sigma)
u2 = V[:,0]
u1 = V[:,1]
theta = np.arcsin(u1[0]/np.linalg.norm(u1)) * 180/(np.pi)

print("n = " + str(n))
print("t(n) = " + str(tn))
print("t_N = " + str(t_N))
print("t_S = " + str(t_S))
print("Eigenvalues of stress are " + str(w))
print("Eigenvectors are ")
print(str(V))
print("azimuth is " + str(theta))
print("theta + 90 = " + str(theta + 90))
