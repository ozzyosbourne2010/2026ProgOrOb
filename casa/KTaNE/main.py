import C
import fios1
import botao
running = True
while running:
    mod=input('diz o modulo. : ')
    if mod == 'FIOS1':
        fios1.resf1()
        print('\n'*20)
    if mod == 'BOTAO':
        botao.resb()
        print('\n'*20)