#Faça um programa que leia um número qualquer e mostre o seu fatorial.

# #solução com módulo
# from math import factorial
# n = int(input('Digite um número para calcular seu fatorial: '))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}')

#Modo tradicional

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1 
print(f'{f}')