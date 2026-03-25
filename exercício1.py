"""
1. Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é F <- (9 * C + 160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura  em Celsius.
cole o código Python abaixo.
"""
# Solicitar ao usuário a temperatura em Celsius
c = float(input("Digite a temperatura em graus Celsius: "))

# Calcular a temperatura em Fahrenheit usando a fórmula de conversão
f = (9 * c + 160) / 5

# Apresentar o resultado
print(f"A temperatura em graus Fahrenheit é: {f:.2f} °F")