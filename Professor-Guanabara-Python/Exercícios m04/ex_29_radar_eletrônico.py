#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

radar = float(input('Qual a velocidade do carro? '))
if radar > 80:
    print('Você foi multado! Sua multa é de R${:.2f}'.format((radar - 80) * 7))
else:
    print('Você está dentro do limite de velocidade!')