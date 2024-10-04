import random
import os
def baralho():
    baralho = [cartas for cartas in range(1,11)]
    baralho = random.choice(baralho)
    return baralho
resp = 'S'
while resp == 'S':
    maquina_qtd = 0
    player_qtd = 0
    print(f'você está com:{player_qtd}')
    while True:
        player_escolha = input("Deseja pegar mais uma carta [S/N]: ").upper()
        if player_escolha == 'S':
            player_qtd = player_qtd + baralho()
            os.system('cls')
            print(f'você tem {player_qtd}')
            maquina_qtd = maquina_qtd + baralho()
        elif player_escolha == 'N':
            os.system('cls')
            print(f'você tem {player_qtd}')
            maquina_qtd = maquina_qtd + baralho()
        else:
            print("Digite um valor válido!")
        
        if maquina_qtd == 21:
            print('A maquina ganhou!')
            print(f'A maquina tem: {maquina_qtd}')
            break
        elif player_qtd == 21:
            print('Você ganhou!')
            print(f'A maquina tem: {maquina_qtd}')
            break
        elif player_qtd > 21 and maquina_qtd > 21:
            print('Empate')
            print(f'A maquina tem: {maquina_qtd}')
            break
        elif player_qtd > 21 and maquina_qtd < 21:
            print('A maquina ganhou!')
            print(f'A maquina tem: {maquina_qtd}')
            break
        elif maquina_qtd > 21 and player_qtd < 21:
            print('Você ganhou!')
            print(f'A maquina tem: {maquina_qtd}')
            break
        else:
            print('Ambos estão com menos que 21!')
    resp = input("deseja jogar novamente [S/N]: ").upper()
    if resp == 'N':
        break
    elif resp == 'S':
        continue
    else:
        print('Digite uma entrada válida!')


