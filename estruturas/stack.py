import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/audreyemmely/estrutura-de-dados/main/dados/USvideos.csv', encoding = "UTF-8")

class Elemento: 
  def __init__(self, c, p):
    self.conteudo = c
    self.proximo = p

class Pilha:
  def __init__(self):
    self.topo = None 

  def vazia(self): 
    if self.topo == None:
      print ("A pilha está vazia\n")
    else:
      print ("A pilha não está vazia\n")

  def empilhar(self, novo_conteudo): 
      novo_elemento = Elemento(novo_conteudo, self.topo)
      self.topo = novo_elemento
      print("Elemento {} foi inserido no topo da pilha\n".format(novo_elemento.conteudo))

  def desempilhar(self):
    if self.topo == None:
      print("A pilha está vazia\n")
    elemento_excluido = self.topo
    self.topo = self.topo.proximo
    exclusao_feita = elemento_excluido  # só removi o .conteudo
    del elemento_excluido
    print("Elemento ({}) foi excluído do topo da pilha\n".format(exclusao_feita))

  def tamanho(self):
    if (self.topo == None):
      return 0
    contador_pilha = 0
    conteudo_pilha = self.topo
    while conteudo_pilha != None:
      contador_pilha += 1
      conteudo_pilha = conteudo_pilha.proximo
    return contador_pilha

  def listar(self):
    if self.topo == None:
      print("A pilha está vazia\n")
    ver_conteudo = self.topo
    while ver_conteudo != None:
      print(ver_conteudo.conteudo)
      print("\n")
      ver_conteudo = ver_conteudo.proximo

def stackMenu(data):
      minha_pilha = Pilha()
      while(True):
          print("---Menu da Pilha---")
          print("1 - Checar se está vazia ou não")
          print("2 - Empilhar")
          print("3 - Desempilhar")
          print("4 - Informar tamanho da pilha")
          print("5 - Listar pilha")

          opcao = int(input("\nInforme a opção: "))

          if opcao == 1:
              minha_pilha.vazia()
          elif opcao == 2: 
              conteudo_informado = int(input("\nDigite o índice do elemento que você deseja inserir: "))
              data = data.sample(100)
              minha_pilha.empilhar(data.iloc[conteudo_informado]) 
          elif opcao == 3:
              minha_pilha.desempilhar() 
          elif opcao == 4:
              print("Tamanho da pilha é de {} elementos\n".format(minha_pilha.tamanho())) 
          elif opcao == 5:
              minha_pilha.listar()
          else:
              print("Opção inválida, digite uma opção mostrada no menu!\n")

while(True):
  stackMenu(data)