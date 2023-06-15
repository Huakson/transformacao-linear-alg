import numpy as np
from scipy.linalg import null_space

class TransformacaoLinear:
    def __init__(self, matriz):
        self.matriz = np.array(matriz)
        m, n = self.matriz.shape
        if m not in [1, 2, 3] or n not in [1, 2, 3]:
            raise ValueError("A matriz deve ter dimensões entre 1x1 e 3x3")

    def aplica(self, vetor):
        vetor = np.array(vetor)
        return np.dot(self.matriz, vetor)

    def get_matriz(self):
        return self.matriz

    def get_dimensao(self):
        return self.matriz.shape

    def get_kernel(self):
        return null_space(self.matriz)
    
    def is_sobrejetora(self):
        m, n = self.matriz.shape
        return np.linalg.matrix_rank(self.matriz) == m

    def get_autovalores(self):
        if not self.is_sobrejetora():
            raise ValueError("A matriz não é sobrejetora")
        return np.linalg.eigvals(self.matriz)


# Exemplo de uso:

t = TransformacaoLinear([[1, 2], [3, 4]])
print("Matriz: \n", t.get_matriz())
print("Dimensão: ", t.get_dimensao())
print("Kernel: \n", t.get_kernel())
print("Sobrejetora: ", t.is_sobrejetora())
if t.is_sobrejetora():
    print("Autovalores: ", t.get_autovalores())
