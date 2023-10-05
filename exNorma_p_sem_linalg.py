import numpy as np

def norma_p_matriz_2por2(matriz, p):
    a, b, c, d = matriz[0, 0], matriz[0, 1], matriz[1, 0], matriz[1, 1]
    norma = (abs(a)**p + abs(b)**p + abs(c)**p + abs(d)**p)**(1/p)
    return norma

matriz_2por2 = np.array([[1, 2], [3, 4]])
p = 2  # Define o valor de p
resultado = norma_p_matriz_2por2(matriz_2por2, p)
print("Norma-{} da matriz:".format(p), resultado)
