import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

def gerar_outra_senha():
    while True:
        comprimento_senha = int(input("Digite o comprimento da senha desejada: "))
        senha_gerada = gerar_senha(comprimento_senha)
        print("Senha gerada:", senha_gerada)
        continuar = input("Deseja gerar outra senha? (s/n): ")
        if continuar.lower() != 's':
            break

gerar_outra_senha()
