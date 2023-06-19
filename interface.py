import tkinter as tk
from tkinter import messagebox

from Transform import TransformacaoLinear


def format_matrix(matrix):
    return '\n'.join(['[' + ' '.join(map(str, row)) + ']' for row in matrix])


def show_results():
    # Obtendo a transformação linear a partir do texto do campo de entrada
    transformacao_linear = transformacao_entry.get()

    try:
        # Criando a transformação linear
        transformacao = TransformacaoLinear(transformacao_linear)

        # Extraindo os resultados
        matriz = transformacao.get_matriz()
        dimensao = transformacao.get_dimensao()
        kernel = transformacao.get_kernel()
        sobrejetora = transformacao.is_sobrejetora()
        injetora = transformacao.is_injetora()
        bijetora = transformacao.is_bijetora()
        vetores_combinacao = transformacao.get_vetores_combinacao()
        imagem = [list(tup) for tup in transformacao.get_imagem()]  # Convertendo o objeto sympy.Matrix para lista aninhada
        dimensao_imagem = transformacao.dimension_imagem()

        # Atualizando os rótulos com os resultados
        matriz_label.configure(text="Matriz:\n{}".format(format_matrix(matriz)))
        dimensao_label.configure(text="Dimensão: {}".format(dimensao))
        kernel_label.configure(text="Kernel:\n{}".format(format_matrix(kernel)))
        dimensao_kernel_label.configure(text="Dimensão do Kernel:\n{}".format(transformacao.dimension_kernel()))
        sobrejetora_label.configure(text="Sobrejetora: {}".format(sobrejetora))
        injetora_label.configure(text="Injetora: {}".format(injetora))
        bijetora_label.configure(text="Bijetora: {}".format(bijetora))
        vetores_combinacao_label.configure(text="Vetores da combinação linear:\n{}".format(format_matrix(vetores_combinacao)))
        imagem_label.configure(text="Imagem:\n{}".format(format_matrix(imagem)))
        dimensao_imagem_label.configure(text="Dimensão da Imagem: {}".format(dimensao_imagem))

    except Exception as e:
        # Mostrando a mensagem de erro em uma caixa de mensagem
        messagebox.showerror("Erro", str(e))


# Criando a janela principal
root = tk.Tk()
root.geometry('500x500')
root.title("Transformação Linear")

# Adicionando um label para o campo de entrada
transformacao_label = tk.Label(root, text="Digite a transformação linear:")
transformacao_label.pack()

# Adicionando um campo de entrada para a transformação linear
transformacao_entry = tk.Entry(root, width=50)
transformacao_entry.pack()

# Adicionando um botão para exibir os resultados
btn = tk.Button(root, text="Calcular", command=show_results)
btn.pack()

# Adicionando rótulos para mostrar os resultados
matriz_label = tk.Label(root, wraplength=400, justify='left')
matriz_label.pack()

dimensao_label = tk.Label(root, wraplength=400, justify='left')
dimensao_label.pack()

kernel_label = tk.Label(root, wraplength=400, justify='left')
kernel_label.pack()

dimensao_kernel_label = tk.Label(root, wraplength=400, justify='left')

dimensao_kernel_label.pack()

sobrejetora_label = tk.Label(root, wraplength=400, justify='left')
sobrejetora_label.pack()

injetora_label = tk.Label(root, wraplength=400, justify='left')
injetora_label.pack()

bijetora_label = tk.Label(root, wraplength=400, justify='left')
bijetora_label.pack()

vetores_combinacao_label = tk.Label(root, wraplength=400, justify='left')
vetores_combinacao_label.pack()

imagem_label = tk.Label(root, wraplength=400, justify='left')
imagem_label.pack()

dimensao_imagem_label = tk.Label(root, wraplength=400, justify='left')
dimensao_imagem_label.pack()

# Iniciando o loop da interface gráfica
root.mainloop()
