import random
from tracemalloc import stop

print('INFORMATIVOS SOBRE O JOGO!!!\n')
print('Tirando 7 ou 11 na primeira jogada você vence o jogo!!\n')
print('Tirando 2,3 ou 12 na primeira rodada é craps e você perde o jogo!!!\n')
print("Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu Ponto.\n\nSeu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.\n")
print('VAMOS COMERÇAR O JOGO!!!\n')
jogador1=input('Digite seu nome:\n')
jogada=input(f"{jogador1} pressione ENTER para lançar os dados!\n")
dado1=random.randint(1,7)
dado2=random.randint(1,7)
pontos=dado1+dado2
resultado=print(f"Os numéros que você tirou foi {dado1} no dado1 e {dado2} no dado 2!!!\n")
if pontos==7 or pontos==11:
    print('Você é um natural!! PARABÉNS VOCÊ VENCEU!!!!!\n')
if  pontos==2 or pontos==3 or pontos==12:
    print('Ohh craps!!! Você PERDEU!!!')
else:
    pontos=pontos
ponto=pontos
if (ponto!=7 or ponto!=11 or ponto!=2 or ponto!=3 or ponto!=12):
    while True:
        ponto=pontos
        if ponto!=7:
            dado1=random.randint(1,7)
            dado2=random.randint(1,7)
            jogada=input(f"{jogador1} pressione ENTER para lançar os dados novamente!\n")
            resultado=print(f"Os numéros que você tirou foi {dado1} no dado1 e {dado2} no dado 2!!!\n")
            if dado1+dado2 == ponto:
                print('Você VENCEUUU!!\n')
                break
            elif dado1+dado2 == 7:
                print("Você PERDEU!!!!!\n")
                break
            else:
                print("Tente novamente!!!\n")
                
                continue
        else:
            break
