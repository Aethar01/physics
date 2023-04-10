from matplotlib import pyplot as plt
import math

xrange = [x for x in range(1, 100, 1)]

fig = plt.figure()
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
axs = gs.subplots()
# fig.suptitle('$f(x)=x^{-\\frac{1}{2}} \\quad and \\quad g(x,\\epsilon)=x^{-(\\frac{1}{2}+\\epsilon)}}$')
axs[0, 0].plot(xrange, [x**(-1/2) for x in xrange])
axs[0, 0].set_title('$f(x)=x^{-\\frac{1}{2}}$')
axs[0, 1].plot(xrange, [math.log(x) for x in xrange])
axs[0, 1].set_title('$\\int{|x^{-\\frac{1}{2}}|^{2}}dx$')
axs[1, 0].plot(xrange, [x**(-(1/2 + 1)) for x in xrange])
axs[1, 0].set_title('$g(x,\\epsilon)=x^{-(\\frac{1}{2}+1)}}$')
axs[1, 1].plot(xrange, [x**(-(1/2 + 1/10))for x in xrange])
axs[1, 1].set_title('$x^{-(\\frac{1}{2}+1/10)}}$')
axs[1, 2].plot(xrange, [x**(-(1/2 + 1/100))for x in xrange])
axs[1, 2].set_title('$x^{-(\\frac{1}{2}+1/100)}}$')
axs[2, 0].plot(xrange, [(x**(2*1))/(2*1) for x in xrange])
axs[2, 0].set_title('$\\int{|x^{-\\frac{1}{2}+1}|^{2}dx}$')
axs[2, 1].plot(xrange, [(x**(2*1/10))/(2*1/10) for x in xrange])
axs[2, 1].set_title('$\\int{|x^{-\\frac{1}{2}+1/10}|^{2}dx}$')
axs[2, 2].plot(xrange, [(x**(2*1/100))/(2*1/100) for x in xrange])
axs[2, 2].set_title('$\\int{|x^{-\\frac{1}{2}+1/100}|^{2}dx}$')

for ax in axs.flat:
    ax.set(xlabel='x', ylabel='y')

for ax in axs.flat:
    ax.label_outer()

plt.savefig('QMPS2.pdf')
