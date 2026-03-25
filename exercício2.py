"""
2. Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius. A fórmula de conversão é C <- ((F - 32) * 5) / 9, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
Insira sua resposta
"""
# Solicitar ao usuário a temperatura em Fahrenheit
f = float(input("Digite a temperatura em graus Fahrenheit: "))

# Calcular a temperatura em Celsius usando a fórmula de conversão
c = ((f - 32) * 5) / 9

# Apresentar o resultado
print(f"A temperatura em graus Celsius é: {c:.2f} °C")
