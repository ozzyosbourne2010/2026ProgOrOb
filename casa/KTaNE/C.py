print('BOMBA YIPEEEE 1 = sim 0 = nao alem dos numeros obvio')
pilhas = input('Quantas pilhas?:')

serie = input('Insira o número de série:') 
serie = list(serie)
serienum = []
serienump = 0
for i in serie:
    if i.isdigit():
        serienum.append(i)
seriev = 0
for i in serie:
    if i in 'AEIOUaeiou':
        seriev = 1
if int(serienum[-1]) / 2 == int(serienum[-1]) // 2:
    serienump = 1

paralela = int(input('Tem entrada paralela?'))
print('sobre os indicadores')
car = int(input('Tem CAR aceso?:'))
frk = int(input('Tem FRK aceso?:'))