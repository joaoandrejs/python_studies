from random import choice
replies = [
    'Sim',
    'Não',
    'OBVIAMENTE, NÃO',
    'OBVIO QUE SIM',
    'Claramente que sim',
    'Certamente',
    'Claro',
    'NUNCA!!!',
    'Deve',
    'NAAAAOOO!!!!!',
    'Acho que não',
    'Não sei',
    'Acho que sim',
    'Sim senhor',
    'Não senhor',
    'SIMMMMMMMMM!!!'
]

def main():
    input('Faça sua pergunta:\n')
    print(f'> {choice(replies)}')
    return 

while True:
    main()

    continuar = input('Perguntar novamente? (S/N): ')
    if continuar.lower() == 's': 
        continue
    else: 
        break

