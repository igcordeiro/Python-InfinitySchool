###################################################################### SEQUENCIA FIBONACCI

valor=int(input('Digite um valor:\n'))
lista=[]
valor1=0
valor2=1
valor3=2
valor4=3
fibonacci=1
lista.append(valor1)
lista.append(valor2)
if valor==1:
    lista.append(valor2)
elif valor ==2:
    lista.append(valor2)
    valor=valor-1
    lista.append(2)
    valor=valor-1
elif valor>2:
    lista.append(valor2)
    valor=valor-1
    lista.append(2)
    valor=valor-1
    lista.append(3)
    valor=valor-1
    while valor>0:
        fibonacci=valor3+valor4
        lista.append(fibonacci)
        valor+=-1
        valor3=valor4
        valor4=fibonacci
else:
    print("ERROR!!!! Apenas digite valores inteiros positivos.")
        
print(lista)
