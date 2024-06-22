import numpy as np


def generate_signal():
    """Generates a signal consisting of up to 5 random Gaussian peaks"""
    # x-scale
    x = np.linspace(0, 100, 500)

    # Gauss peak parameter ranges
    amps = (10, 100)
    wids = (2, 4)
    cens = (min(x) - max(wids), max(x) - max(wids))

    # Linear baseline
    a_base = np.random.uniform(0, 1)
    b_base = np.random.uniform(0, 0.1 * max(amps))
    baseline = a_base * x + b_base

    # Noise along x
    noise = np.random.normal(0.1 * min(amps), 1.1 * min(amps), x.size)

    # Number of peaks
    num_peaks = np.random.randint(1, 6)

    # Get peaks
    peaks = []
    for _ in range(num_peaks):
        # Get random parameters
        amp = np.random.uniform(*amps)
        wid = np.random.uniform(*wids)
        cen = np.random.uniform(*cens)

        peaks.append(amp * np.exp(-((x - cen) ** 2) / (2 * wid**2)))

    # Get total signal
    y = np.sum(peaks, axis=0) + baseline + noise

    return x, y, peaks, baseline


def gauss(x, *params):
    """Model Guassian peak mixture"""
    y = params[0] + params[1] * x
    for i in range(2, len(params), 3):
        amp = params[i]
        cen = params[i + 1]
        wid = params[i + 2]
        y += amp * np.exp(-((x - cen) ** 2) / (2 * wid**2))
    return y
