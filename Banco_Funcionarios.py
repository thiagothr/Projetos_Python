'''
Criar um programa que gera 3 listas de acordo  com a necessidade logo abaixo:

Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham durante o dia
Lista3 = Funcionários que  não tem carro

'''

funcionarios = ['Ana','Marcos','Alice','Pedro','Sophia','Bruno','Melissa']
turno_dia = ['Ana','Marcos','Alice','Melissa']
turno_noite = ['Pedro','Sophia','Bruno']
tem_carro = ['Marcos','Alice','Bruno','Melissa']


l1 = set (tem_carro).intersection(turno_noite) 
print(l1)

l2 = set(tem_carro).intersection(turno_dia)
print(l2)


l3 = set(funcionarios).difference(tem_carro)
print(l3)

