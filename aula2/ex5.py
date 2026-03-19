v1 = int(input())
v2 = int(input())
v3 = int(input())
x = [v1, v2, v3]
maior = max(x)
menor = min(x)
x.remove(maior)
x.remove(menor)
meio = x[0]
x = [menor, meio, maior]
print(x)