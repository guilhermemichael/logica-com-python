"""
7.Ler quatro valores numéricos inteiros e apresentar o resultado das adições e das multiplicaçõesutilizando o mesmo raciocínio aplicado quando do uso de propriedades distributivas para amáxima combinação possível entre as quatro variáveis. Não é para calcular a propriedade distributiva,apenas para usar a sua forma de combinação. Considerando a leitura de valores para asvariáveis A, B, C e D, devem ser feitas seis adições e seis multiplicações, ou seja, deve ser combinadaa variável A com a variável B, a variável A com a variável C, a variável A com a variável D.Depois é necessário combinar a variável B com a variável C e a variável B com a variável D e,por fim, a variável C será combinada com a variável D.
Insira sua resposta
"""
# Solicitar ao usuário os quatro valores numéricos inteiros para as variáveis A, B, C e D
a = int(input("Digite o valor para a variável A: "))
b = int(input("Digite o valor para a variável B: "))
c = int(input("Digite o valor para a variável C: "))
d = int(input("Digite o valor para a variável D: "))

# Realizar as adições combinando as variáveis
soma_ab = a + b
soma_ac = a + c
soma_ad = a + d
soma_bc = b + c
soma_bd = b + d
soma_cd = c + d

# Realizar as multiplicações combinando as variáveis
produto_ab = a * b
produto_ac = a * c
produto_ad = a * d
produto_bc = b * c
produto_bd = b * d
produto_cd = c * d

# Apresentar os resultados das adições
print(f"Soma de A e B: {soma_ab}")
print(f"Soma de A e C: {soma_ac}")
print(f"Soma de A e D: {soma_ad}")
print(f"Soma de B e C: {soma_bc}")
print(f"Soma de B e D: {soma_bd}")
print(f"Soma de C e D: {soma_cd}")

# Apresentar os resultados das multiplicações
print(f"Produto de A e B: {produto_ab}")
print(f"Produto de A e C: {produto_ac}")
print(f"Produto de A e D: {produto_ad}")
print(f"Produto de B e C: {produto_bc}")
print(f"Produto de B e D: {produto_bd}")
print(f"Produto de C e D: {produto_cd}")