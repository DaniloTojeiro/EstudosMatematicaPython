# Faça um programa que calcule os m² de uma parede e calcule quanto litros de tinta será necessário

alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
area = larg * alt

print('Sua parede tem a dimensão de {:.1f}x{:.1f} e sua área é de {:.1f}m²' .format(larg, alt, area))
tinta = area / 2
print('Você precisa de {}l para pintar essa parede.' .format(tinta))