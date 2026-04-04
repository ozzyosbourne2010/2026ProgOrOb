import C
def resf1():
    fios = input('Quais os fios? (primeira letra em ingles e preto = K)')
    numf = len(fios)
    fios = list(fios)
    ty = 0
    tr = 0
    tb = 0
    tk = 0
    tw = 0
    for i in fios:
        if i == 'W':
            tw += 1
    for i in fios:
        if i == 'Y':
            ty += 1
    for i in fios:
        if i == 'K':
            tk += 1
    for i in fios:
        if i == 'B':
            tb += 1
    for i in fios:
        if i == 'R':
            tr += 1
    if numf == 3:
        if tr == 0:
            print('Corta o primeiro')       
        elif fios[-1] == 'W':
            print('Corta o último fio')
        elif tb > 1:
            print('corte o ultimo azul')
        else:
            print('corta o ultimo fio')
    elif numf == 4:
        if tr > 1 and C.serienump == 0:
            print('Corte o último fio vermelho')
        elif tr == 0 and fios[-1] == 'Y':
            print('Corte o primeiro fio')
        elif tb == 1:
            print('Corte o primeiro fio')
        elif ty > 1:
            print('Corte o último fio')
        else:
            print('Corte o segundo fio')
    elif numf == 5:
        if fios[-1] == 'K' and C.serienump == 0:
            print('Corte o quarto fio')
        elif tr == 1 and ty > 1:
            print('Corte o primeiro fio')
        elif tk == 0:
            print('Corte o segundo fio')
        else:
            print('Corte o primeiro fio')
    elif numf == 6:
        if ty == 0 and C.serienump == 0:
            print('Corte o terceiro fio')
        elif ty == 1 and tw > 1:
            print('Corte o quarto fio')
        elif tr == 0:
            print('Corte o último fio')
        else:
            print('Corte o quarto fio')