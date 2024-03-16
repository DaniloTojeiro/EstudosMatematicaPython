# Ler um número em metros e converter para cm e mm

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000

print('A medida de {}m corresponde a {}cm e {}mm' .format(medida, cm, mm))