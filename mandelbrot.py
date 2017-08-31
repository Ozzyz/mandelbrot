import functools
import matplotlib.pyplot as plt


class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __mul__(self, other):
        # (a+ib)(c+id) = ac-bd+i(ad+bc)
        real_part = self.real*other.real - self.imaginary*other.imaginary
        imaginary_part = self.real*other.imaginary + self.imaginary*other.real
        return ComplexNumber(real_part, imaginary_part)

    def __add__(self, other):
        if(isinstance(other, ComplexNumber)):
            return ComplexNumber(self.real+other.real, self.imaginary + other.imaginary)
        if(isinstance(other, float) or isinstance(other, int)):
            return ComplexNumber(self.real + other, self.imaginary)
        raise ValueError('Illegal addition to complexnumber!')

    def __eq__(self, other):
        return (self.real, self.imaginary) == (other.real, other.imaginary)

    # This is needed in order to use functools.lru_cache
    def __hash__(self):
        return hash((self.real, self.imaginary))

    def __len__(self):
        return float(self.real**2 + self.imaginary**2)

    def __repr__(self):
        return "%s %si" % (self.real, self.imaginary)

    
@functools.lru_cache(maxsize=1024)
def mandelbrot(z, c):
    return z*z + c

def mandelbrot_seq(x,y, max_iter, max_len, max_x, max_y):
    # The number of iterations a number go through decide the pixel intensity
    num_iters = 0
    # TODO: Scale numbers to match mandelbrot range
    # X : (-2.5,1)
    # Y: (-1,1)
    x = (((x-max_x*0.5)*(3.5/(max_x*0.5)))-1.5)/2
    y = (y-(max_y*0.5))/(max_y*0.5)
    z_n = ComplexNumber(0,0)
    c = ComplexNumber(x,y)
    
    while(True): # and num_iters <= max_iter):
        z_n = mandelbrot(z_n, c)
        num_iters += 1
        if(num_iters > max_iter or len(z_n) > max_len):
            break
    return num_iters



def plot():
     
    plt.figure()
    Z = []
    X = []
    Y = []
    max_x = 1<<13
    max_y = 1<<13
    for x in range(max_x):
        for y in range(max_y):
            res = mandelbrot_seq(x,y, 255, 2, max_x, max_y)
            X.append(x)
            Y.append(y)
            Z.append(res)
        print("(%s, %s) Num iters: %s " % (x,y,res))
    Z = [(1-x/255) for x in Z]
    plt.scatter(X, Y, c=Z)
    plt.savefig("mandelbrot.png")
    plt.show()


plot()
