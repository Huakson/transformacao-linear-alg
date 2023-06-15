import Transform as tf

transformacao_linear = "T: R2 -> R2, T(x, y) = (x - y, 2*x + y)"

matriz  = tf.TransformacaoLinear(transformacao_linear)

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
