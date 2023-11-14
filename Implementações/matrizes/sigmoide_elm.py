import numpy as np

# Suponha que SH seja uma matriz NumPy
SH = np.array([[2.5, 2], [1.1, -5.2]])

# Calcule a matriz H
H = 1 / (1 + np.exp(-SH))

print("Matriz H:")
print(H)