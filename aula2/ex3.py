import math
v1 = int(input('Valor 1 '))
v2 = int(input('Valor 2 '))
v3 = int(input('Valor 3 '))
v4 = int(input('Valor 4 '))
x = [v1, v2, v3, v4]
vida = 2
a= 4
while a > 0:
    for i in x:
        if i == v1:
            vida -= 1
    
if vida <= 0:
    print('tem que ser diferentes dog')
    quit()
maior = max(x)
menor = min(x)
x.remove(maior)
x.remove(menor)
soma =  x[0] + x[1]
print(f'Maior valor {maior}')
print(f'Menor valor {menor}')
print(f'Soma dos 2 valores restantes {soma}')
