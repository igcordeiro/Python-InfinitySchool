def recebe_lista(x):
    tamanho_lista=len(x)
    soma_lista=0
    for position in range(tamanho_lista):
        soma_lista+=x[position]
    print(f'{soma_lista}')
lista1=[123,15,80,798,1]
recebe_lista(lista1)
