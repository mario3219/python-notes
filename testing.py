import numpy as np
from matplotlib import pyplot as plt
import sympy as sym

def f(x):
    return np.sin(x)
x = np.linspace(1, 10, 50)

plt.plot(x, f(x))
plt.show()