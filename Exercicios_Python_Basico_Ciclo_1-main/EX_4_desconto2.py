# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome_produto = input("Digite o nome do produto: ")
produto = float(input("Digite o preço do produto: "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto: "))

# cálculo do valor do desconto
valor_desconto = produto * (porcentagem_desconto / 100)

# cálculo do valor final
valor_final = produto - valor_desconto

# exibição dos dados
print(f"Produto: {nome_produto}")
print(f"Preço: {produto}")
print(f"Porcentagem de desconto: {porcentagem_desconto}")
print(f"O {nome_produto} com {porcentagem_desconto}% de desconto custará R$ {valor_final}")