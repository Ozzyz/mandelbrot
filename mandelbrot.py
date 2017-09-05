import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image
def mandelbrot(X, Y, max_iters, max_len, N):
    img = Image.new('RGBA', (N, N))
    pixels = img.load()
    
    Z = np.zeros((X.size, Y.size), dtype=np.complex_)
    
    for i in range(X.size):
        for j in range(Y.size):
            num_iters = 0
            c = X[i] + 1j*Y[j]
            Z[i][j] = c
            while(abs(Z[i][j]) < max_len and num_iters < max_iters):
                Z[i][j] = Z[i][j]**2 + c
                num_iters += 1
            rgba_arr = cm.hot(num_iters/max_iters)
            # Since PIL wants rgba from 0 to 255
            pixels[i,j] = tuple(int(x*255) for x in rgba_arr)
        print("(%s, %s) Num iters: %s" % (i, j, num_iters))
    return img
    
def main():
    # Width and height in pixels
    num_pixels = 3000
    min_x, max_x = -1.5 , 1
    min_y, max_y = -1, 1
    X = np.linspace(min_x, max_x, num_pixels)
    Y = np.linspace(min_y, max_y, num_pixels)
    max_len = 4
    max_iters = 128

    start = time.time()
    img = mandelbrot(X, Y, max_iters, max_len, num_pixels)
    end = time.time()
    print("%sx%s sized image finished in %s seconds" % (num_pixels, num_pixels,end-start))
    img.show()
    img.save("mandelbrot%sx%s.png" % (num_pixels, num_pixels))
    

main()
