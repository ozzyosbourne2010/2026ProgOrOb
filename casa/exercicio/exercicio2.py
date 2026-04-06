
a = input("Digite dois valores inteiros separados por um operador +, -, * ou /: ")

for op in ['+', '-', '*', '/']:
    if op in a:
        num1, num2 = a.split(op)
        num1 = int(num1)
        num2 = int(num2)

        if op == '+':
            r = num1 + num2
        elif op == '-':
            r = num1 - num2
        elif op == '*':
            r = num1 * num2
        elif op == '/':
            r = num1 / num2

        print(f'O resultado da operação é {r}')
else:
    print("Entrada Inválida")