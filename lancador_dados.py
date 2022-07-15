#LANÇANDO DADOS 100 BEZES E CONTANDO QUANTAS VEZES CADA NÚMERO FOI SORTEADO

from random import randint

lances_dado=[]
for i in range (0,100):
    valor=randint(1,6)
    lances_dado.append(valor)
print(lances_dado)
count_1=0
count_2=0
count_3=0
count_4=0
count_5=0
count_6=0
lances_dado=str(lances_dado)
for numero in lances_dado:
    if numero in '1':
        count_1+=1
    elif numero in '2':
        count_2+=1
    elif numero in '3':
        count_3+=1
    elif numero in '4':
        count_4+=1
    elif numero in '5':
        count_5+=1
    elif numero in '6':
        count_6+=1
print(f'O número 1 apareceu {count_1} vezes!!\n')
print(f'O número 2 apareceu {count_2} vezes!!\n')
print(f'O número 3 apareceu {count_3} vezes!!\n')
print(f'O número 4 apareceu {count_4} vezes!!\n')
print(f'O número 5 apareceu {count_5} vezes!!\n')
print(f'O número 6 apareceu {count_6} vezes!!\n')
