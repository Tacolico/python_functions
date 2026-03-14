def gauss_legendre(
        f, # Function f = lambda x: x**2
        a, # Lower limit
        b, # Upper limit
        n  # Gauss points
        ):
    import numpy as np
    from numpy.polynomial.legendre import leggauss
    x, w = leggauss(n)
    xp = (b - a)/2 * x + (a + b)/2
    fx = f(xp)
    I = (b - a)/2 * np.sum(w * fx)
    return I
