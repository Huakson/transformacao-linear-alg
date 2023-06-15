import Transform as tf

matriz  = tf.TransformacaoLinear([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

print("Matriz: \n", matriz.get_matriz())
print("Dimensão: ", matriz.get_dimensao())
print("Kernel: \n", matriz.get_kernel())
print("Sobrejetora: ", matriz.is_sobrejetora())
print("Vetores da combinação linear: ", matriz.get_vetores_combinacao())
print("Imagem: ", matriz.get_imagem())

try:
    print("Autovalores: ", matriz.get_autovalores())
except ValueError as e:
    print(e)
