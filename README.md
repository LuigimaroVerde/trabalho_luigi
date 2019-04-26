# trabalho_luigi

8 locais
do local inicial sai para dois caminhos um pro lado e um pra cima, vai seguind ate um camiho onde cai no porao, o destino final é a torre para poder pular para outro navio.

class Local:

    def __init__ (self, descricao = "",monstro  = "", tesouro = "", cabineAcima = "", cabineAbaixo =""):
       self.descricao = descricao
       self.monstro = monstro
       self.tesouro = tesouro
       self.cabineAcima = cabineAcima
       self.cabineAbaixo = cabineAbaixo
    def cabines(self):
       print("Boas vindas jogador")


cabine1 = cabine("eh uma cabine bem iluminada", "nao tem", "poucas moedas")
cabine2 = cabine("eh uma cabine sombria, sem janela", "Um pirata!", "muitas moedas")
cabine3 = cabine("eh uma cabine labirintica", "goblins, muitos sacanas", "muitas moedas, com barras de ouro em")

cabine1.cabineAbaixo = cabine2
#cabine1.cabineMeio = cabine1
cabine1.cabineAcima = cabine3

cabine3.cabineAbaixo = cabine1
cabine2.cabineAcima = cabine1

cabine1.cabines()

cabineAtual = cabine1

print("descricao, monstro, tesouro, cabineAcima, cabineAbaixo")
inpt = ""
while( inpt !="q"):
   print(cabineAtual.descricao)
   inpt = input("para onde queres ir? cima ou baixo?\n")
   if( inpt =="cima"):
       cabineAtual = cabineAtual.cabineAcima
   elif( inpt =="baixo"):
       cabineAtual = cabineAtual.cabineAbaixo

