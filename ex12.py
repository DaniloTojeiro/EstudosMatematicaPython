# Programa que leia um salário e aumente 15%

salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario + (salario * 15 / 100)

print('Um funcionário que ganhava R${:.2f}, passou a receber R${:.2} com 15% de aumento.' .format(salario, novo))