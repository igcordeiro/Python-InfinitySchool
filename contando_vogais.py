###################################################################### CONTANDO VOGAIS EM UM NOMES

def count_vogais(nomes):
    qtd_vogais=0
    nomes=str(nomes)
    for letras in (nomes):
        if letras in 'aeiouAEIOU':
            qtd_vogais+=1
    print(f'A quantidade de vogais de todos os nomes digitados é igual a {qtd_vogais}!\n')
lista=[]
while True:
    resposta=input("Deseja cadastrar alguém para contar o número de vogais em seu nome?\n")
    pessoas={}
    if resposta in "sSsimSIMSimsIM":
        nome=str(input('Digite um nome:\n'))
        pessoas['N@m3']=nome
        lista.append(pessoas)
        continue
    else:
        break
count_vogais(lista)
