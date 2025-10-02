import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

def rooCMSShape(x, alpha, beta, gamma, peak):
    erf_term = erfc((alpha - x) * beta)
    u = (x - peak) * gamma
    # Handle numerical stability
    u_safe = np.where(u < -70, 1e20, np.where(u > 70, 0, np.exp(-u)))
    return erf_term * u_safe

def plot_rooCMSShape(acmsF, betaF, gammaF, peakF, x_min=60, x_max=120, n_points=1000):
    x_vals = np.linspace(x_min, x_max, n_points)
    y_vals = rooCMSShape(x_vals, acmsF, betaF, gammaF, peakF)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='RooCMSShape', color='blue')
    plt.title("RooCMSShape::bkgFail")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    acmsF = 64     # alpha
    betaF = 0.100    # beta
    gammaF = 0.041  # gamma
    peakF = 90     # peak

    plot_rooCMSShape(acmsF, betaF, gammaF, peakF)
