class triangulo:
    #atributo
    def __init__(self):
        self.b = 0
        self.h = 0
    #metodo
    def calc_area(self):
        return self.b * self.h / 2
        
x = triangulo()
print(x.b, x.h)
x.b = float(input('diz a base '))
x.h = float(input('diz a altura '))
a = x.calc_area()
print(f'areae {a}')

y = triangulo()
print(y.b, y.h)
y.b = float(input('diz a base '))
y.h = float(input('diz a altura '))
a = y.calc_area()
print(f'area2e {a}')

print('tudo')
print(f'Primeiro triang base{x.b} alt{x.h}')
print(f'Segundo triang base{y.b} alt{y.h}')