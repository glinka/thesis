import numpy as np
import matplotlib
from matplotlib import colors, colorbar, cm, pyplot as plt, gridspec as gs, tri, patches
import dmaps

# matplotlib.rc('text', usetex = True)
# matplotlib.rc('font', **{'family' : "sans-serif"})
# params = {'text.latex.preamble' : [r'\usepackage{amsmath}']}
# plt.rcParams.update(params)


npts = 2000
data = np.power(np.random.uniform(size=(npts,2)), 2)*np.array((2.5, 1.0))
# data = np.random.multivariate_normal(mean=(1.25, 0.5), cov=((1,0),(0,1)), size=(npts,))
# data = data[data[:,0] > 0]
# data = data[data[:,1] > 0]
# data = data[data[:,0] < 2.5]
# data = data[data[:,1] < 1]

s=100
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(data[:,0], data[:,1], s=s)
ax.set_xlim((0,2.5))
ax.set_ylim((0,1))
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
plt.show()

k = 4
eps = 0.2

# eigvals, eigvects_un = dmaps.embed_data(data, k, epsilon=eps)
# eigvals, eigvects_norm = dmaps.embed_data(data, k, epsilon=eps, embedding_method=dmaps._compute_embedding_laplace_beltrami)
# data.dump('./data/dmapsii-data-non.pkl')
# eigvects_un.dump('./data/dmapsii-eigvects-un.pkl')
# eigvects_norm.dump('./data/dmapsii-eigvects-norm.pkl')

data = np.load('./data/dmapsii-data-non.pkl')
eigvects_un = np.load('./data/dmapsii-eigvects-un.pkl')
eigvects_norm = np.load('./data/dmapsii-eigvects-norm.pkl')

lw = 3
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(data[:,0], -eigvects_norm[:,1]/np.max(eigvects_norm[:,1]), c='b', label='$\phi_1$' + '(normalized)')
ax.scatter(data[:,0], -eigvects_un[:,1]/np.max(eigvects_un[:,1]), c='r', label='$\phi_1$' + '(unnormalized)')
dxs = np.sort(data[:,0])
ax.plot(dxs, np.cos(2*np.pi*dxs/5), linestyle='dashed', color='k', lw=lw, label='Analytical')
ax.set_xlim((0,2.5))
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$\phi$')
ax.legend(loc='upper right')
fig.subplots_adjust(bottom=0.18)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(data[:,1], -eigvects_norm[:,3]/np.max(eigvects_norm[:,3]), c='b', label='$\phi_3$' + '(normalized)')
ax.scatter(data[:,1], eigvects_un[:,3]/np.max(eigvects_un[:,3]), c='r', label='$\phi_3$' + '(unnormalized)')
dys = np.sort(data[:,1])
ax.plot(dys, np.cos(np.pi*dys), linestyle='dashed', color='k', lw=lw, label='Analytical')
ax.set_xlim((0,1))
ax.set_xlabel(r'$y$')
ax.set_ylabel(r'$\phi$')
ax.legend(loc='lower left')
fig.subplots_adjust(bottom=0.18)


plt.show()
