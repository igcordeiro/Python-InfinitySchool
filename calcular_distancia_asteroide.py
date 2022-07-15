###########################PROGRAMA CALCULO DE DISTANCIA DE ASTEROIDE

distancia=[]
def nasa():
    nome=input('Digite o nome do Asteiroide que será calcualda a distância:\n')
    count=0
    for _ in range(0,5):
        dicionario={'Nome Asteiroide':nome}
        count+=1
        distancias=input(f'Digite a {count}ª distancia do asterioride {nome} até a terra:\n')
        dicionario[f'{count}ª Distancia']=distancias
        distancia.append(dicionario)
    print(distancia)
nasa()
