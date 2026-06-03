# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
nome = input ("| Digite o nome do usuario: ")
idade = input("| Digite sua idade: ")
email = input ("| Digite  seu email:  ")
senha = input ("| Digite sua senha: ")


print("\n--- DADOS CADASTRADOS ---")
print("Nome:", nome)
print("Idade:", idade)
print("E-mail:", email)
print("Senha:", senha)

print("\n| ------------------------------ |")
print("| ----- USUÁRIO CADASTRADO ----- |")
print(f"| Seja bem vindo(a) {nome}!")
print(f"| Email: {email}")
print("| ------------------------------ |")
