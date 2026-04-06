print('Digite uma sequência de números separados por vírgula:')
x = input()
xlista = x.split(',')
soma = 0
for i in xlista:
    soma += int(i)
print(f'Soma = {soma}')