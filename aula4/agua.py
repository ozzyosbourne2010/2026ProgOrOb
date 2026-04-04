class agua():
    def __init__(self):
        self.a = 0
        self.m = None
        self.ano = None
        self.v = 0
    def calc(self):
        if self.a <= 10:
            self.v = 38
        elif self.a <= 20:
            n = self.a - 10
            self.v = 38 + (n*5)
        elif self.a > 20:
            n1 = self.a - 20
            self.v = 38 + 50 + (n1 * 6)
        return self.v
c = agua()
c.a = int(input('Insira o consumo em m³: '))
c.m = str(input('Insira o mês: '))
c.ano = str(input('Insira o ano: '))
vf = c.calc()
print(f'O valor a ser pago da conta de água referente ao mês {c.m} do ano {c.ano} é de: R${vf}')