from random import randint

tentativas = 25
tentativas_counter = 0
minimo = randint(1, 100)
maximo = randint(100, 899)
random_number = randint(minimo, maximo)

def mensagem(tentativas):
    if tentativas <= 1: return 'CAGADA!'
    elif tentativas <= 5: return 'Deus!'
    elif tentativas <= 10: return 'Nada mal!'
    elif tentativas <= 15: return 'Muito bom!'
    elif tentativas <= 25: return 'Ok...'


print(' ACHE O NÙMERO!! '.center(45, '='))
print(f'\nO número está entre {minimo} e {maximo}\nVocê possui: {tentativas} tentativas\n')

while True:    
    guess = input(f'> Digite um número: ')
    try:
        guess = int(guess)

        if guess < minimo or guess > maximo:
            print(f'O número deve estar entre: {minimo} e {maximo}')
            continue

        if tentativas < 1:
            print(f'Você não conseguiu acertar o número! :(\nO número secreto era: {random_number}\nVocê tentou mais de: {tentativas_counter} vezes.')
            break
        elif guess == random_number:
            tentativas_counter += 1
            print(f'\n{mensagem(tentativas_counter)}!\nO número secreto era: {random_number}!\nVocê conseguiu em: {tentativas_counter} tentativas.')
            break
        elif guess < random_number:
            tentativas -= 1
            tentativas_counter += 1
            print(f'{guess} é MENOR que meu número - {tentativas} tentativas restantes\n')
        else:
            tentativas -= 1
            tentativas_counter += 1
            print(f'{guess} é MAIOR que meu número - {tentativas} tentativas restante\n')
            
    except ValueError:
        print('Digite apenas números inteiros!')
        continue
    
