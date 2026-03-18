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

def simpson(
        signal,     # Data to integrate
        sample_rate # Frequency [Hz]
        ):
    import numpy as np
    dt = 1 / sample_rate
    n = len(signal)
    integrated = [0 for i in range(len(signal))]
    integrated[1] = (signal[0] + signal[1]) / 2 * dt
    for i in range(2, n, 2):
        area = (signal[i-2] + 4*signal[i-1] + signal[i]) * dt / 3
        integrated[i] = integrated[i-2] + area
        integrated[i-1] = (integrated[i] + integrated[i-2]) / 2
    if n % 2 == 0:
        integrated[-1] = integrated[-2] + (signal[-2] + signal[-1]) / 2 * dt
    import data_process
    integrated = data_process.fft_filter(
    signal      = integrated,
    sample_rate = sampling,
    low_filter  = 0
    )
    return integrated

def trapezoidal_even(
        signal,     # Data to integrate
        sample_rate # Frequency [Hz]
        ):
    integrated=[0 for i in range(len(signal))]
    for i in range(1,len(signal)):
        integrated[i]=(signal[i]+signal[i-1])/2*1/sample_rate+integrated[i-1]
    import data_process
    integrated = data_process.fft_filter(
    signal      = integrated,
    sample_rate = sampling,
    low_filter  = 0
    )
    return integrated

def trapezoidal(
        y_data,     # Data to integrate
        x_data      # Frequency [Hz]
        ):
    if len(x_data)!=len(y_data):
        exit("Sampling error: missing x/y values")
    integrated=[0 for i in range(len(y_data))]
    for i in range(1,len(signal)):
        integrated[i]=(y_data[i]+y_data[i-1])/2*(x_data[i]-x_data[i-1])+integrated[i-1]
    import data_process
    integrated = data_process.fft_filter(
    signal      = integrated,
    sample_rate = sampling,
    low_filter  = 0
    )
    return integrated

