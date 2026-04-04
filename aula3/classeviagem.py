class viagem():
    def __init__(self):
        self.dist = 0
        self.timeh = 0
        self.timem = 0
    def calcspeed(self):
        tempo = (self.timeh * 60) + self.timem
        speed = self.dist / tempo
        return speed
x = viagem()
x.dist= float(input('diz a distancia '))
x.timeh = int(input('quantas horas '))
x.timem = int(input('quantos min '))
media = x.calcspeed() * 60
print(f'{media} medidas por hora')