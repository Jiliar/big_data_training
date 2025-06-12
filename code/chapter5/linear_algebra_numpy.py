import numpy as np
from numpy import linalg


v = np.array([1, 2, 3])
m = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
print("Vector v:", v, sep="\n")
print("Matrix m:", m, sep="\n")

# Multiplicación de vecvtor por matriz
v_m = np.dot(v, m)
v_m_2 = v @ m  # Otra forma de hacer la multiplicación

print("Multiplicación de vector por matriz v * m:", v_m, sep="\n")
print("Multiplicación de vector por matriz v @ m:", v_m_2, sep="\n")

# iNversa de una matriz
m_inv = linalg.inv(m)
print("Inversa de la matriz m:", m_inv, sep="\n")
# Multiplicación de matriz por su inversa
m_inv_m = np.dot(m, m_inv)
print("Multiplicación de matriz por su inversa m * m_inv:", m_inv_m, sep="\n")