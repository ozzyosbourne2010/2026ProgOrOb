from os import kill


meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
num = int(input('Insira o número do mês '))
if num >= 13 or num <= 0:
    print('Tem esse mes nao gld')
    quit()
num -= 1
tri1 = meses[:3]
tri2 = meses[3:6]
tri3 = meses[6:9]
tri4 = meses[9:]
mes = meses[num]
if mes in tri1:
    print(f'O mês de {mes} esta no primeiro trimestre')
elif mes in tri2:
    print(f'O mês de {mes} esta no segundo trimestre')
elif mes in tri3:
    print(f'O mês de {mes} esta no terceiro trimestre')
elif mes in tri4:
    print(f'O mês de {mes} esta no quarto trimestre')