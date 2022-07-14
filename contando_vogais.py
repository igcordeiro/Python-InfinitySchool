###################################################################### CONTANDO VOGAIS EM DOIS NOMES

def count_vogais(nome1,nome2):
    qtd_vogais=0
    total=str(nome1+nome2)
    for letras in (total):
        if letras in 'aeiouAEIOU':
            qtd_vogais+=1
    print(f'A quantidade de vogais em {nome1} e em {nome2} é igual a {qtd_vogais}!\n')
pessoa1=str(input('Digite o nome da pessoa1 para que se conte as vogais de seu nome:\n'))
pessoa2=str(input('Digite o nome da pessoa2 para que se conte as vogais de seu nome:\n'))
count_vogais(pessoa1,pessoa2)
