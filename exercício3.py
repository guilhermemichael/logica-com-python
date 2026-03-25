"""
3. Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula VOLUME <- 3.14159 * RAIO^2 * ALTURA.
Insira sua resposta
"""
# Solicitar ao usuário o raio e a altura da lata de óleo
r = float(input("Digite o raio da lata de óleo: "))
h = float(input("Digite a altura da lata de óleo: "))

# Calcular o volume da lata de óleo usando a fórmula de volume de um cilindro
v = 3.14159 * r**2 * h

# Apresentar o resultado
print(f"O volume da lata de óleo é: {v:.2f} unidades de volume")