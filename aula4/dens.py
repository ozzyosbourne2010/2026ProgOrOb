class País():
    def __init__(self):
        self.n = None
        self.p = 0
        self.a = 0
    def calc(self):
        d = self.p/self.a
        return d
x = País()
x.n = input('Digite o nome do país:')
x.p = int(input('Digite sua população:'))
x.a = int(input('Digite a área em km2:'))
rx = x.calc()
rx = round(rx, 2)

x1 = País()
x1.n = input('Digite o nome do país:')
x1.p = int(input('Digite sua população:'))
x1.a = int(input('Digite a área em km2:'))
rx1 = x1.calc()
rx1 = round(rx1, 2)

x2 = País()
x2.n = input('Digite o nome do país:')
x2.p = int(input('Digite sua população:'))
x2.a = int(input('Digite a área em km2:'))
rx2 = x2.calc()
rx2 = round(rx2, 2)

x3 = País()
x3.n = input('Digite o nome do país:')
x3.p = int(input('Digite sua população:'))
x3.a = int(input('Digite a área em km2:'))
rx3 = x3.calc()
rx3 = round(rx3, 2)

x4 = País()
x4.n = input('Digite o nome do país:')
x4.p = int(input('Digite sua população:'))
x4.a = int(input('Digite a área em km2:'))
rx4 = x4.calc()
rx4 = round(rx4, 2)

y = País()
y.n = input('Digite o nome do país:')
y.p = int(input('Digite sua população:'))
y.a = int(input('Digite a área em km2:'))
ry = y.calc()
ry = round(ry, 2)

y1 = País()
y1.n = input('Digite o nome do país:')
y1.p = int(input('Digite sua população:'))
y1.a = int(input('Digite a área em km2:'))
ry1 = y1.calc()
ry1 = round(ry1, 2)

y2 = País()
y2.n = input('Digite o nome do país:')
y2.p = int(input('Digite sua população:'))
y2.a = int(input('Digite a área em km2:'))
ry2 = y2.calc()
ry2 = round(ry2, 2)

y3 = País()
y3.n = input('Digite o nome do país:')
y3.p = int(input('Digite sua população:'))
y3.a = int(input('Digite a área em km2:'))
ry3 = y3.calc()
ry3 = round(ry3, 2)

y4 = País()
y4.n = input('Digite o nome do país:')
y4.p = int(input('Digite sua população:'))
y4.a = int(input('Digite a área em km2:'))
ry4 = y4.calc()
ry4 = round(ry4, 2)

valores = [rx, rx1, rx2, rx3, rx4, ry, ry1, ry2, ry3, ry4]
teste = [rx, rx1, rx2, rx3, rx4, ry, ry1, ry2, ry3, ry4]
teste.remove(max(valores))
if max(valores) == max(teste):
    print('Empate!')
else:
    if max(valores) == rx:
        print(f'O país com a maior densidade demográfica é {x.n} com uma população de {x.p}, área de {x.a}km² e densidade demográfica de {rx}hab/km²')
    elif max(valores) == rx1:
        print(f'O país com a maior densidade demográfica é {x1.n} com uma população de {x1.p}, área de {x1.a}km² e densidade demográfica de {rx1}hab/km²')
    elif max(valores) == rx2:
        print(f'O país com a maior densidade demográfica é {x2.n} com uma população de {x2.p}, área de {x2.a}km² e densidade demográfica de {rx2}hab/km²')
    elif max(valores) == rx3:
        print(f'O país com a maior densidade demográfica é {x3.n} com uma população de {x3.p}, área de {x3.a}km² e densidade demográfica de {rx3}hab/km²')
    elif max(valores) == rx4:
        print(f'O país com a maior densidade demográfica é {x4.n} com uma população de {x4.p}, área de {x4.a}km² e densidade demográfica de {rx4}hab/km²')
    elif max(valores) == ry:
        print(f'O país com a maior densidade demográfica é {y.n} com uma população de {y.p}, área de {y.a}km² e densidade demográfica de {ry}hab/km²')
    elif max(valores) == ry1:
        print(f'O país com a maior densidade demográfica é {y1.n} com uma população de {y1.p}, área de {y1.a}km² e densidade demográfica de {ry1}hab/km²')
    elif max(valores) == ry2:
        print(f'O país com a maior densidade demográfica é {y2.n} com uma população de {y2.p}, área de {y2.a}km² e densidade demográfica de {ry2}hab/km²')
    elif max(valores) == ry3:
        print(f'O país com a maior densidade demográfica é {y3.n} com uma população de {y3.p}, área de {y3.a}km² e densidade demográfica de {ry3}hab/km²')
    elif max(valores) == ry4:
        print(f'O país com a maior densidade demográfica é {y4.n} com uma população de {y4.p}, área de {y4.a}km² e densidade demográfica de {ry4}hab/km²')