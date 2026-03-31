class circulo():
    def __init__(self):
        self.radius = 0
    def calcarea(self):
        return self.radius * self.radius * 3.14
    def calcareapi(self):
        areapi = self.radius * self.radius
        return areapi, 'π'
x = circulo()
x.radius = float(input('diz o raio '))
a = x.calcarea()
api = x.calcareapi()
print(f'area em com pi = 3.14: {a}')
print(f'area em com pi irracional: {api}')