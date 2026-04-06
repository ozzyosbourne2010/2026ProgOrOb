import C
copy = '''Faixa azul: solte quando o marcador de tempo tiver um 4 em qualquer
posição.
Faixa branca: solte quando o marcador de tempo tiver um 1 em qualquer
posição.
Faixa amarela: solte quando o marcador de tempo tiver um 5 em qualquer
posição.
Faixa de qualquer outra cor: solte quando o marcador de tempo tiver um 1 em
qualquer posição.'''
def resb():
    cor = input('Qual a cor do botão')
    pal = input('Qual a palavra do botão')
    if cor == 'AZUL' and pal == 'ABORTAR':
        print('Segure o botão')
        print(copy)
    elif C.pilhas > 1 and pal == 'DETONAR':
        print('Pressione e imediatamente solte o botão')
    elif cor == "BRANCO" and C.car == 1:
        print("Segura o bagulho, jão - ass Leonardo")
        print(copy)
    elif C.pilhas >= 2 and C.frk == 1:
        print("Pressione e imediatamente solte o botão.")
    elif cor == 'AMARELO':
        print('Segure o botão')
        print(copy)
    elif cor == 'VERMELHO' and pal == 'SEGURE':
        print('Pressione e solte o botão')
    else:
        print('Segure o botão')
        print(copy)