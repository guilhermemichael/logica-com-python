"""
4. Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel que faz 12 quilômetros por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto (variável TEMPO) e a velocidade média (variável VELOCIDADE) durante a viagem. Desta forma, será possível obter a distância percorrida com a fórmula DISTÂNCIA <- TEMPO * VELOCIDADE. A partir do valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a fórmula LITROS_USADOS <- DISTÂNCIA/ 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a  quantidade de litros utilizada na viagem.
Insira sua resposta
"""
# Solicitar ao usuário o tempo gasto e a velocidade média durante a viagem
t = float(input("Digite o tempo gasto na viagem (em horas): "))
v = float(input("Digite a velocidade média durante a viagem (em km/h): "))

# Calcular a distância percorrida usando a fórmula DISTÂNCIA <- TEMPO * VELOCIDADE
d = t * v

# Calcular a quantidade de litros de combustível utilizada na viagem com a fórmula LITROS_USADOS <- DISTÂNCIA/ 12
litros_usados = d / 12

# Apresentar os resultados
print(f"Velocidade média: {v:.2f} km/h")
print(f"Tempo gasto na viagem: {t:.2f} horas")
print(f"Distância percorrida: {d:.2f} km")
print(f"Litros de combustível utilizados: {litros_usados:.2f} litros")