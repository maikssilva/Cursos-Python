# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual é o salário do Funcionário? R$'))
novo = salario + (salario * 15/100)
print('Um funcionário que ganhava R${:.2F}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))
