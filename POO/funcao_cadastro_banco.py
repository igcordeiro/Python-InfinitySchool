from main import DadosBancarios as banco

def cadastrar_favorecidos():
    lista=[]
    dicio={'Nome Cliente':'','Conta':'','Saldo':'','VIP':''}
    while True:
        question=input('Deseja cadastrar um usuário? Digite sim ou nao.\n')
        if question in 'SIMsimSimsIM':
            nome=input('Digite o nome do cliente:\n')
            conta=input('Digite a conta do cliente. Apenas numeros, sem o digito\n')
            saldo=float(input(f'Digite o Saldo disponível para o cliente{nome}\n'))
            if saldo > 250000:
                    vip=True
                
            else:
                    vip=False
        
            dados=banco(nome,conta,saldo,vip)
            dicio=dados
            lista.append(dicio)
            continue
        else:
            
            print('Segue abaixo usuários cadastrados:\n')
            print(lista)
            break