# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# APÓS A SOPA - A SACADA DA CASA - A TORRE DA DERROTA - O LOBO AMA O BOLO - ANOTARAM A DATA DA MARATONA

# frase = str(input('Digite uma frase:    ')).strip().upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''
# for letra in range(len(junto) - 1, -1, -1):
#     inverso += junto[letra]
# if inverso == junto:
#     print('Temos um palíndromo!')
# else:
#     print('A frase digitada não é um palíndromo!')

#2ª forma de resolver

frase = str(input('Digite uma frase:    ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')