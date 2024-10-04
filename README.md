# Transformação Linear - Projeto Python

Este projeto é um exemplo de como calcular transformações lineares usando Python, utilizando uma interface gráfica criada com a biblioteca `Tkinter`. O projeto também oferece funcionalidades para calcular diversos aspectos de uma transformação linear, como matriz, kernel, imagem, e autovalores, além de verificar se a transformação é injetora, sobrejetora ou bijetora.

## Funcionalidades

- Verificação se uma transformação é linear.
- Cálculo da matriz associada à transformação linear.
- Determinação do kernel e imagem da transformação.
- Verificação se a transformação é injetora, sobrejetora ou bijetora.
- Cálculo de autovalores para operadores lineares.
- Interface gráfica para input e visualização dos resultados.

## Requisitos

- Python 3.x
- Bibliotecas necessárias:
  - `numpy`
  - `scipy`
  - `sympy`
  - `tkinter` (para interface gráfica)

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu_usuario/transformacao-linear.git
cd transformacao-linear
pip install -r requirements.txt
```

## Utilização

Modo Console: Execute o script Python diretamente para visualizar os resultados de uma transformação linear no console.

```python
import Transform as tf

transformacao_linear = "T:R2 -> R2, T(x, y) = (2*x + y, x - y)"
matriz = tf.TransformacaoLinear(transformacao_linear)
print("Matriz: \n", matriz.isTransformacaoLinear())
```
