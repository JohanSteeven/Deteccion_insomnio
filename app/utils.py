import numpy as np

# Función para calcular la distancia entre dos puntos
def compute(pt_a, pt_b):
    return np.linalg.norm(pt_a - pt_b)

# Función para determinar si los ojos están parpadeando
def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)

    if ratio > 0.25:
        return 2  # Abiertos
    elif ratio > 0.21 and ratio <= 0.25:
        return 1  # Semi-cerrados
    else:
        return 0  # Cerrados
