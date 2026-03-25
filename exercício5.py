"""
5.Efetuar o cálculo e apresentar o valor de uma prestação de um bem em atraso, utilizando a fórmula PRESTAÇÃO= VALOR+ (VALOR* (TAXA/100) * TEMPO).
Insira sua resposta
"""
# Solicitar ao usuário o valor da prestação, a taxa de juros e o tempo em atraso
valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa de juros (em %): "))
tempo = float(input("Digite o tempo em atraso (em meses): "))

# Calcular o valor da prestação em atraso usando a fórmula PRESTAÇÃO= VALOR+ (VALOR* (TAXA/100) * TEMPO)
prestacao = valor + (valor * (taxa / 100) * tempo)

# Apresentar o resultado
print(f"O valor da prestação em atraso é: {prestacao:.2f}")