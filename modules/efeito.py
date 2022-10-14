class Efeito: #Efeitos utilizados para skills, items, ataques, etc. Exemplos seriam Dano, Cura, AplicarStatus
  def __init__(self, delay = 0, origem = None, hitcancela = False, alvo = None
    ) -> None:
    self.delay = delay #Quantos segundos/10 (100?), depois esse efeito ativará. (Pode ser baseado no contador de batalha, caso seja 0 ele ativa, caso seja > 0 delay -= 1
    self.origem = origem #De onde surgiu esse efeito. Poderia ser um personagem (ou uma string? Poderiamos colocar coisas como "Ambiente" para dano de ambiente ou traps, etc
    self.hitcancela = hitcancela #Só funcionaria com o Delay. Quando um personagem tomar um hit, escaneiam se todos os efeitos e caso hitcancela = true cancele hitcancela.
    self.alvo = alvo #O alvo do efeito.
    
    
  def getOrigem(self):
    return(self.origem)
  
  def setOrigem(self, origem):
    self.origem = origem
    
  def getTipo(self):
    return(self.__class__.__name__)
    
  def efeito(self):
    print("Nada pode estar 100% puro, nem mesmo efeitos. (class efeito sem inherit)") #mensagem de erro lul
    print("Delay ",self.delay)
    print("Origem ",self.origem)
    print("alvo ",self.alvo)  
