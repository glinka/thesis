import numpy as np
import matplotlib.pyplot as plt

npts = 5000
mean = np.array((0,0))
cov = np.array([[ 5.5,  4.5], \
            [ 4.5,  5.5]])

x1, x2 = np.random.multivariate_normal(mean, cov, npts).T

A = np.array((x1, x2)).T

u, s, vT = np.linalg.svd(A)
print s, vT
print np.linalg.eig(cov)

s /= 50
fig = plt.figure(figsize=(16,16))
ax = fig.add_subplot(111)
ax.scatter(x1, x2, c='b', alpha=0.1)
ax.arrow(0, 0, s[0]*vT[0,0], s[0]*vT[0,1], color='r', lw=2, head_width=0.2)
ax.arrow(0, 0, s[1]*vT[1,0], s[1]*vT[1,1], color='r', lw=2, head_width=0.2)
ax.set_xlabel(r'$x_1$')
ax.set_ylabel(r'$x_2$')
fig.subplots_adjust(bottom=0.18, left=0.18)
plt.show()
