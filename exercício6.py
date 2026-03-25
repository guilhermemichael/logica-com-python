"""
6.Ler dois valores para as variáveis A e B e efetuar a troca dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores após a efetivação do processamento da troca.
Insira sua resposta
"""
# Solicitar ao usuário os valores para as variáveis A e B
a = input("Digite o valor para a variável A: ")
b = input("Digite o valor para a variável B: ")

# Efetuar a troca dos valores usando uma variável temporária
temp = a
a = b
b = temp

# Apresentar os valores após a troca
print(f"Após a troca, o valor da variável A é: {a}")
print(f"Após a troca, o valor da variável B é: {b}")