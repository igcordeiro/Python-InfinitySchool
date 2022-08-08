class Computador:
    def __init__(self, modelo, fabricante, processador, tamanho_do_hd,espaço_ocupado_hd, esta_ligado):
        self.modelo = modelo
        self.fabricante = fabricante
        self.processador = processador
        self.tamanho_do_hd = tamanho_do_hd
        self.espaço_ocupado_hd = espaço_ocupado_hd
        self.esta_ligado=esta_ligado

    def ligar(self):
      self.esta_ligado=True
            
    def desligar(self):
      self.esta_ligado=False

    def limparHD(self):
        qtd_limpar=input('Digite quantos GB deseja limpar do seu HD.')

        if qtd_limpar.isdigit() :
            qtd_limpar=int(qtd_limpar)
            if self.espaço_ocupado_hd - qtd_limpar < self.tamanho_do_hd:
                    print('Seu HD está completamente zerado!!!\n')
                    self.espaço_ocupado_hd=0
            else:
                    print(f'Foram removidos {qtd_limpar} GBs do seu HD!!\n')
                    self.espaço_ocupado_hd -= qtd_limpar
                
        else:
            print('ERROR!!!! Digite apenas um valor inteiro!!!\n')        
    def OcuparHD(self):
        qtd_ocupar=input('Digite quantos GB deseja ocupar do seu HD.')
        if qtd_ocupar.isdigit():
            qtd_ocupar=int(qtd_ocupar)
            if self.espaço_ocupado_hd + qtd_ocupar > self.espaço_ocupado_hd:
                    print('ESPAÇO DE ARMAZENAMENTO COMPLETAMENTE CHEIO!!!\n')
                    self.espaço_ocupado_hd=self.tamanho_do_hd
            else:
                    print(f'Foram Armazenados {qtd_ocupar} GBs do seu HD!\n')
                    self.espaço_ocupado_hd += qtd_ocupar
                
        else:
            print('ERROR!!! Apenas valores inteiros são permitidos, tente novamente!!!\n')
        
    def mostrar(self):
        print('Inicio de Informações de Máquina')
        print(self.modelo)
        print(self.fabricante)
        print(self.processador)
        print(self.tamanho_do_hd)
        print(self.espaço_ocupado_hd)
        print(self.esta_ligado)
        print('Termino de Informações de Máquina')


pc1 = Computador("WorkSpace Xlarge", 'AWS', 'Intel', 1000,250,False)
pc2 = Computador("Virtual Machine", 'Azure', 'AMD', 500,250,True)

pc1.ligar()

pc2.desligar()
pc2.limparHD()
pc1.OcuparHD()
pc1.mostrar()
pc2.mostrar()
