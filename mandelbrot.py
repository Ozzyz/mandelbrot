import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image

from numba import jit

@jit
def mandelbrot(X, Y, max_iters, max_len):

    iters = np.zeros((X.size, Y.size), dtype=np.uint)

    for i in range(X.size):
        for j in range(Y.size):
            num_iters = 0
            c = X[i] + 1j*Y[j]
            z = c
            while(abs(z) < max_len and num_iters < max_iters):
                z = z**2 + c
                num_iters += 1
            iters[i, j] = num_iters
        print(i,',',j)
    return iters


def main():
    # Width and height in pixels
    num_pixels = 7500
    min_x, max_x = 0, 0.002
    min_y, max_y = -0.823, -0.821
    X = np.linspace(min_x, max_x, num_pixels)
    Y = np.linspace(min_y, max_y, num_pixels)
    max_len = 4
    max_iters = 255

    start = time.time()
    iters = mandelbrot(X, Y, max_iters, max_len) 
    end = time.time()
    print("%sx%s sized image finished in %s seconds" % (num_pixels, num_pixels,end-start))
    #plt.axis('off')
    #plt.imshow(iters, cmap=cm.hot)
    plt.imsave('mandelbrot_zoomed2.png', iters)
    #plt.show()


main()
