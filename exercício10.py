"""
10. Ler dois valores numéricos inteiros (representados pelas variáveis A e B) e apresentar o resultado do quadrado da soma dos dois valores lidos: $(A + B)^2$.
"""
# Solicitar ao usuário os dois valores numéricos inteiros para as variáveis A e B
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

resultado = (A + B) ** 2

print(f"O quadrado da soma de A e B é: {resultado}")