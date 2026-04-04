print('Digite uma frase:')
texto = str(input())

soma = 0

for i in texto:
    if i.isdigit():  # check if it's a digit
        soma += int(i)

print(soma)