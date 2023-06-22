import numpy as np
from scipy.linalg import null_space
from sympy import Matrix, symbols, parse_expr, simplify
import re

class TransformacaoLinear:
    matriz = []
    def __init__(self, transformacao_linar_string):
        matriz = self.parse_transformacao(transformacao_linar_string)
        
        # explicitamente converter para float
        self.matriz = np.array(matriz,  dtype=int)
        m, n = self.matriz.shape
        if m < 1 or m > 3 or n < 1 or n > 3:
            raise ValueError("A matriz deve ter dimensões entre 1x1 e 3x3")


    
    def isTransformacaoLinear(self):
        matriz = np.array(self.matriz, dtype=int)
        m, n = matriz.shape

        # Verificar se a matriz é quadrada
        if m != n:
            return False
    
        # Verificar a preservação da soma
        for i in range(m):
            for j in range(n):
                u = np.zeros(n)
                v = np.zeros(n)
                u[i] = 1
                v[j] = 1
                soma_esperada = matriz[:, i] + matriz[:, j]
                soma_calculada = np.dot(matriz, u + v)
                if not np.allclose(soma_calculada, soma_esperada):
                    return False

        # Verificar a preservação da multiplicação por escalar
        for i in range(m):
            for c in range(5):  # Verificar até 5 escalares
                u = np.zeros(n)
                u[i] = 1
                escalar = c + 1
                mult_esperada = matriz[:, i] * escalar
                mult_calculada = np.dot(matriz, escalar * u)
                if not np.allclose(mult_calculada, mult_esperada):
                    return False

        return True
           
    def aplica(self, vetor):
        vetor = np.array(vetor)
        if len(vetor) != self.matriz.shape[1]:
            raise ValueError(
                "A dimensão do vetor deve ser igual ao número de colunas da matriz")
        return np.dot(self.matriz, vetor)

    def get_matriz(self):
        matriz = np.array(self.matriz).T.tolist()  
        return matriz

    def get_dimensao(self):
        return self.matriz.shape

    def get_kernel(self):
        matrix = Matrix(self.matriz.tolist())
        return matrix.nullspace()
    
    def dimension_kernel(self):
        matrix_rank = np.linalg.matrix_rank(self.matriz)
        input_dim, output_dim = self.matriz.shape
        kernel_dimension = input_dim - matrix_rank
        return kernel_dimension

    def is_sobrejetora(self):
        m, n = self.matriz.shape
        return np.linalg.matrix_rank(self.matriz) == m

    def get_vetores_combinacao(self):
        return [self.matriz[:, i] for i in range(self.matriz.shape[1])]

    def get_imagem(self):
        return Matrix(self.matriz).columnspace()
    
    def dimension_imagem(self):
        matrix_rank = np.linalg.matrix_rank(self.matriz)
        output_dim = self.matriz.shape[1]
        return matrix_rank, output_dim
    
    def is_operador(self):
        if not self.is_sobrejetora():
            return False
        try:
            autovalores = self.get_autovalores()
            return np.all(autovalores != 0)
        except ValueError:
            return False
        
    def is_injetora(self):
        m, n = self.matriz.shape
        return np.linalg.matrix_rank(self.matriz) == n
    
    def is_bijetora(self):
        return self.is_injetora() and self.is_sobrejetora()
    
    def get_autovalores(self):
        m, n = self.matriz.shape
        if m != n:
            raise ValueError(
                "A matriz precisa ser quadrada para calcular autovalores")
        return np.linalg.eigvals(self.matriz)

    def parse_transformacao(self, transformacao_str):
        # Extrai as dimensões de entrada e saída e as equações da string de transformação
        match = re.match(
            r"T[0-9]*\s*:\s*R(\d+)\s*->\s*R(\d+),\s*T[0-9]*\((.*?)\)\s*=\s*\((.*?)\)", transformacao_str)

        if match is None:
            print("Erro: a dimensão de entrada, a dimensão de saída ou as variáveis não foram encontradas na string de transformação.")
            return None

        # Extrai as dimensões de entrada e saída e as equações
        in_dim, out_dim = map(int, match.group(1, 2))
        input_vars = match.group(3).split(", ")
        eq_strs = match.group(4).split(", ")

        # Verifica se o número de variáveis de entrada corresponde à dimensão de entrada
        if len(input_vars) != in_dim:
            print(
                f"Erro: o número de variáveis de entrada ({len(input_vars)}) não corresponde à dimensão de entrada ({in_dim}).")
            return None

        # Cria símbolos para as variáveis de entrada
        var_symbols = [symbols(f'x{i+1}') for i in range(in_dim)]
        matriz = []
        for eq_str in eq_strs:
            temp_eq = parse_expr(eq_str, local_dict={
                                 input_var: var_symbol for input_var, var_symbol in zip(input_vars, var_symbols)})
            coef_list = []
            for var in var_symbols:
                coef = simplify(temp_eq.subs(
                    {v: (1 if v == var else 0) for v in var_symbols}))
                coef_list.append(coef if coef.is_number else 0)
            matriz.append(coef_list)

        # Convertendo numpy array para lista do Python
        matriz = np.array(matriz).T.tolist()
        return matriz
