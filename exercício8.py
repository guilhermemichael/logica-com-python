"""
8.Elaborar um programa que calcule e apresente o valor do volume de uma caixa retangular, utilizando
a fórmula VOLUME= COMPRIMENTO* LARGURA* ALTURA.
"""
# Solicitar ao usuário o comprimento, largura e altura da caixa retangular
c = float(input("Digite o comprimento da caixa retangular: "))
l = float(input("Digite a largura da caixa retangular: "))
h = float(input("Digite a altura da caixa retangular: "))

# Calcular o volume da caixa retangular usando a fórmula VOLUME= COMPRIMENTO* LARGURA* ALTURA
v = c * l * h

# Apresentar o resultado
print(f"O volume da caixa retangular é: {v:.2f} unidades de volume")