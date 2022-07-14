def player_registration():
    registro=input('Deseja cadastrar um jogador?\n')
    list_players=[]
    while True:
        if registro in "SIMsimSsSimsIM":
            Dicitonary_players={}
            name=str(input('Digite o nome do jogador a ser cadastrado:\n'))
            goals_scored=input(f'Quantos gols foram marcados nesta temporada por {name}?\n')
            Dicitonary_players['Nome Jogador']=name
            Dicitonary_players['Qtd Gols Marcados']=goals_scored
            list_players.append(Dicitonary_players)
            registro=input('Deseja cadastrar um jogador?\n')
            if registro in "SIMsimSsSimsIM":
                continue
            else:
                print(list_players)
                print('Saindo do programa.\n')
                break
        else:
            print('Saindo do programa.\n')
            break
player_registration()
