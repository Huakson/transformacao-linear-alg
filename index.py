import Transform as tf

transformacao_linear = "T: R3 -> R3, T(x, y, z) = (x, y, z)"

matriz  = tf.TransformacaoLinear(transformacao_linear)

print("Matriz: \n", matriz.get_matriz())
print("Dimensão: ", matriz.get_dimensao())
print("Kernel: \n", matriz.get_kernel())
print("Dimensão do Kernel \n", matriz.dimension_kernel())
print("Sobrejetora: ", matriz.is_sobrejetora())
print("Injetora: ", matriz.is_injetora())
print("Bijetora: ", matriz.is_bijetora())
print("Vetores da combinação linear: ", matriz.get_vetores_combinacao())
print("Imagem: ", matriz.get_imagem())
print("Dimensão: ", matriz.dimension_imagem())

try:
    if matriz.is_operador(): 
        print("Autovalores: ", matriz.get_autovalores())
except ValueError as e:
    print(e)
