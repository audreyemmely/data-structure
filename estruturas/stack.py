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
      print(ver_conteudo.conteudo) # tava usando uma variavel numero que n tinha sido definida, simplesmente troquei por "conteudo" e lansei um \n pra ficar bonitinho
      print("\n")
      ver_conteudo = ver_conteudo.proximo
