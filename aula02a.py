# Operadores Aritméticos

name = input('Qual o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(name)) # pula 20 caracteres
print('Prazer em te conhecer {:>20}!'.format(name)) # alinha jogando 20 caracteres a direita
print('Prazer em te conhecer {:<20}!'.format(name)) # alinha jogando 20 caracteres a esquerda
print('Prazer em te conhecer {:^20}!'.format(name)) # alinha jogando 20 caracteres centralizado
print('Prazer em te conhecer {:=^20}!'.format(name)) # alinha jogando 20 caracteres a centralizado com=

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f}' .format(s, m, d), end=' ') # end continua na mesma linha
print('Divisão inteira {} e potência {}' .format(di, e))
