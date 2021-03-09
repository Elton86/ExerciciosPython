"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações."""

nome = str(input("Digite o nome de usuario: "))
while True:
    senha = str(input("Digite a senha: "))
    if senha == nome:
        print("Digite uma senha diferente de seu nome!")
    else:
        print("Senha aceita.")
        break
