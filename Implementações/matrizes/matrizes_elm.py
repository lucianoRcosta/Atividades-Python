import numpy as np

# Suponha que H, H' e y sejam matrizes NumPy
H = np.array([[0.832, 1.033], [1.033, 1.000]])
y = np.array([0, 1])

# Calcule H'
H_transpose = H.T

# Calcule (H' * H)
HtH = np.dot(H_transpose, H)

# Calcule a inversa de (H' * H)
HtH_inv = np.linalg.inv(HtH)

# Calcule H' * y
Hty = np.dot(H_transpose, y)

# Calcule (H' * H)^-1 * H' * y
result = np.dot(HtH_inv, Hty)

print("Resultado:", result)
