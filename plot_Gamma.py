import numpy as np
import matplotlib.pyplot as plt

# Parameters
a0 = 1.87
a1 = 15.7
a2 = 30

# Define the function
def bkgFail(x, a0, a1, a2):
    return a0 * x**a1 * np.exp(-a2 * x)

# x range (start from a small positive number to avoid 0^a1 issues)
x = np.linspace(0.001, 0.2, 1000)
y = bkgFail(x, a0, a1, a2)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$f(x) = {a0} \cdot x^{{{a1}}} \cdot e^{{-{a2} x}}$', color='darkblue')
plt.title("Gamma Background-like Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.yscale('log')  # Log scale to better see the shape
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
