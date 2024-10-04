perguntas = [
{
    'pergunta' : 'Quanto é 2+2?',
    'opções': ['1','3','4','5'],
    'resposta': '4',
},
{
    'pergunta' : 'Quanto é 5x5?',
    'opções': ['25','55','10','51'],
    'resposta': '25',
},
{
    'pergunta' : 'Quanto é 10/2?',
    'opções': ['4','5','2','1'],
    'resposta': '5',
},
]

for pergunta in perguntas:
    print(pergunta['pergunta'])
    print()
    for i, opcao in enumerate(pergunta['opções']):
        print(f'{i}) {opcao}')
    resposta = input('Escolha uma opção: ')
    if resposta == pergunta['resposta']:
        print('Acertou')
    else:
      print("Errou")
    print()
