import numpy as np
from scipy.linalg import null_space
from sympy import Matrix

class TransformacaoLinear:
    def __init__(self, matriz):
        self.matriz = np.array(matriz)
        m, n = self.matriz.shape
        if m < 1 or m > 3 or n < 1 or n > 3:
            raise ValueError("A matriz deve ter dimensões entre 1x1 e 3x3")

    def aplica(self, vetor):
        vetor = np.array(vetor)
        if len(vetor) != self.matriz.shape[1]:
            raise ValueError("A dimensão do vetor deve ser igual ao número de colunas da matriz")
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
        m, n = self.matriz.shape
        if m != n:
            raise ValueError("A matriz precisa ser quadrada para calcular autovalores")
        return np.linalg.eigvals(self.matriz)

    def get_vetores_combinacao(self):
        return [self.matriz[:,i] for i in range(self.matriz.shape[1])]

    def get_imagem(self):
        return Matrix(self.matriz).columnspace()
# Exemplo de uso:

t = TransformacaoLinear([[ 1 , 1 ], [0 , 1], [2 , 0]])
print("Matriz: \n", t.get_matriz())
print("Dimensão: ", t.get_dimensao())
print("Kernel: \n", t.get_kernel())
print("Sobrejetora: ", t.is_sobrejetora())
print("Vetores da combinação linear: ", t.get_vetores_combinacao())
print("Imagem: ", t.get_imagem())
try:
    print("Autovalores: ", t.get_autovalores())
except ValueError as e:
    print(e)
