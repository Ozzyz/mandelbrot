import matplotlib.cm as cm
import functools
import numpy as np
import matplotlib.pyplot as plt

def mand_zoom():
    N = 4096
    min_x, max_x = -2.5 , 1
    min_y, max_y = -1, 1
    X = np.linspace(min_x, max_x, N)
    Y = np.linspace(min_y, max_y, N)
    Z = np.zeros((X.size, Y.size), dtype=np.complex_)
    max_len = 4
    max_iters = 128
    Iters = np.zeros((X.size, Y.size), dtype=np.int)
    for x in range(X.size):
        for y in range(Y.size):
            num_iters = 0
            c = X[x] + 1j*Y[y]
            Z[x][y] = c
            while(abs(Z[x][y]) < max_len and num_iters < max_iters):
                Z[x][y] = Z[x][y]**2 + c
                num_iters += 1
            plt.scatter(X[x], Y[y], cm.hot(num_iters/max_iters))
            Iters[x][y] = num_iters
            print("(%s, %s) Num iters: %s" % (x, y, num_iters))
    #xx, yy = np.meshgrid(X,Y)
    #Iters = [cm.hot(x/max_iters) for x in Iters.flatten('F')]

    #plt.xlim((min_x, max_x))
    #plt.ylim((min_y, max_y))
    #plt.scatter(xx,yy, c=Iters)
    plt.savefig('testmandelbrot_255iters')
    plt.show()
    
mand_zoom()
