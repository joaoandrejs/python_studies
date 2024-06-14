from random import choice
choices = ['pedra', 'papel', 'tesoura']

def userChoice():
    escolhasStr = ', '.join(choices)
    escolha = input(f'O que deseja jogar ({escolhasStr}): ').lower()
    if escolha not in choices:
        print(f'Opção inválida, escolha uma das opções')
        userChoice()
    return escolha

def winner(user_choice, client_choice):
    if user_choice == client_choice:
        return 'EMPATE!'
    elif (
        user_choice == 'pedra' and client_choice == 'tesoura' or \
        user_choice == 'tesoura' and client_choice == 'papel' or \
        user_choice == 'papel' and client_choice == 'pedra'):
        return 'GANHOU!'
    else:
        return 'PERDEU!'

def game():
    print('-'*20)
    print("Pedra, Papel ou Tesoura")
    user_choice = userChoice()
    client_choice = choice(choices)
    print(f'Você escolheu: {user_choice}\nBOT escolheu: {client_choice}')
    print(winner(user_choice, client_choice))

    resultado = input('\nQuer jogar novamente? (S/N): ').lower()
    if resultado == 's':
        game()
    else:
        print('Tchau, Obrigado por jogar!')
        print('-'*20)

game()
