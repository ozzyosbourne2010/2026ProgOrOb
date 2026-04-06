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
r = x.calc()
r = round(r, 2)
print(f'A densidade demográfica {x.n} é de {r} hab/km2')