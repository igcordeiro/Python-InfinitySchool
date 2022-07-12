def player_registration():
    registro=input('Deseja cadastrar um jogador?\n')
    list_players=[]
    Dicitonary_players={}
    while True:
        if registro in "SIMsimSsSimsIM":
            list_players=[]
            Dicitonary_players={'Nome Jogador':[],'Qtd Gols Marcados':[]}
            name=str(input('Digite o nome do jogador a ser cadastrado:\n'))
            goals_scored=input(f'Quantos gols foram marcados nesta temporada por {name}?\n')
            Dicitonary_players['Nome Jogador'].append(name)
            Dicitonary_players['Qtd Gols Marcados'].append(goals_scored)
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

player_registration()
