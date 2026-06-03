# Atualize o código de aluguel de carros feito anteriormente. 
# Crie um programa em Python que simule o cálculo do valor total a ser pago pelo aluguel de um carro. O programa deve:
# 1- Perguntar ao usuário qual foi o modelo do carro alugado.
# 2- Perguntar por quantos dias o carro foi alugado.
# 3- Perguntar quantos quilômetros foram percorridos com o carro.
# 4- Usar uma tabela de preços (pré-definida pelo próprio aluno) para determinar o valor diário de aluguel de acordo com o modelo do carro.
# 5- Calcular o custo total com base:
# 6- No número de dias alugados × valor por dia
# 7- No total de quilômetros rodados × R$0,15 por km
# 8- Exibir o valor total a ser pago, com duas casas decimais.

# Os alunos são livres para definir quais modelos de carro o programa aceitará e o valor por dia de cada um.

# Se o modelo inserido pelo usuário não estiver na lista, o programa deve aplicar um valor padrão por dia.

# OUTPUT ESPERADO: 

# ----------------------------------------------------- EXEMPLO 1

# Qual foi o modelo do carro alugado? uno
# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 100
# Você andou 100.0km por 10 dias, então o preço a pagar é R$415.00.

# ----------------------------------------------------- EXEMPLO 2

# Qual foi o modelo do carro alugado? bmw
# Por quantos dias o carro foi alugado: 10 
# Quantos km o carro rodou: 100 
# Você andou 100.0km por 10 dias, então o preço a pagar é R$10015.00.

# ----------------------------------------------------- EXEMPLO 3(PREÇO PADRÃO)

# Qual foi o modelo do carro alugado? fox
# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 100 
# Você andou 100.0km por 10 dias, então o preço a pagar é R$615.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

# Tabela de preços dos carros por dia
precos_carros ={
    "pagani": 1000,
    "bmw": 1000,
    "audi": 150,
    "civic ": 350
}

# Preço padrão para modelos não encontrados
preco_padrao = 60

# Solicita ao usuário o modelo do carro, dias e quilômetros
modelo = input("Qual foi o modelo do carro alugado? ").lower()
dias = int(input("Por quantos dias o carro foi alugado: "))
km = float(input("Quantos km o carro rodou: "))

# Obtém o preço do carro (usa padrão se modelo não encontrado)
preco_diario = precos_carros.get(modelo, preco_padrao)

# Calcula o valor total: (dias × preço diário) + (km × 0.15)
preco_total = dias * preco_diario + km * 0.15

# Exibe o resultado formatado
print(f"Você andou {km}km por {dias} dias, então o preço a pagar é R${preco_total:.2f}.")
