'''
print("para testar o codigo, voce pode clicar no "
+"icone do inseto a esquerda, e depois um PLAY.")
'''

class Local:
    def __init__ (self, nome = "", descricao = "", opcoes = ""):
        self.nome = nome
        self.descricao = descricao
        self.opcoes = opcoes
    def local(self):
        print("----------------------")
        print("Sua localizacao: " + self.nome)
    def escreveMenu(self):
        global locais #consegue acesso a variavel locais
        print("Opcoes para voce escolher: ")
        for opcao in self.opcoes.split(","):
            if (opcao) : print(opcao + ") " + (locais[int(opcao)].nome))

locaisValidos = [1,2,3,4,5,6,7,8,9] #todas as escolhas possiveis - melhorar

locais = [0,1,2,3,4,5,6,7,8,9,10] #definicao da variavel e dos numeros dos ambientes - melhorar

locais[1] = Local("Deck" , #nome
               "eh um local bem iluminado, nao tem monstros, poucas moedas" , #descricao
               "2") #opcoes
locais[2] = Local("Mastro" , 
               "Oba, esse eh o seu mastro, agora pule no navio, que esta aqui do lado e voce tera conseguido, Parabens!" , 
               "1,3")
locais[3] = Local("Cabine do Capitao" , 
               "Meu deusss, essa eh o local do capitao!, que luta epica, um capitao e um soldado, de recompensa teremos, um bau, ta bom ne?",
               "2,4")
locais[4] = Local("Entrada do Porao",
               "Eh um local labirintico, goblins, bruxos, e fantasmas, muitas moedas, com barras de ouro",
               "3,5")
locais[5] = Local("Cozinha",
               "Nem eh um local, eh so uma cozinha, tem um polvo ali, voce viu ne?, uma faca ali no canto, pegue-a, nao tem ouro, tem comida quer?",
               "4,6")
locais[6] = Local("Dormitorio",
               "nem eh um local, eh so um quarto, tem dois piratas, uma espada ali no canto, usea-a, e veja se eles tem uns ourinhos",
               "5,7")
locais[7] = Local("Prisao",
               "eh um local com grades, tem prisioneiros, so voce os libertar que seram seus aliados, sem ouro",
               "6,8,9")
locais[8] = Local("Sala dos Canhoes",
               "agora voce nao tem pra onde ir ou volta tudo ou eh preso e tenta fugir!",
               "7")
locais[9] = Local("Ambiente Secreto",
               "haha! voce caiu na armadilha, os piratas foram mais espertos, agora eles viram te prender!",
               "7")

inicio = 7 # Onde comeca
localAtual = locais[inicio]
localAtual.local() #escreve a localizacao
print(localAtual.descricao) #mostra a descricao
localAtual.escreveMenu() #traz as opcoes

#reseta a escolha
escolha = "" #limpa a escolha
while( escolha !="q" ):
   escolha = int(input("Digite o numero de sua escolha: "))
   if escolha in locaisValidos: #se tem este ambiente configurado
        localAtual = locais[escolha]  #atualiza o local atual
        localAtual.local() #escreve a localizacao
        print(localAtual.descricao) #escreve a descricao
        localAtual.escreveMenu() #escreve o menu
   else:
        print("Localizacao nao encontrada") 
