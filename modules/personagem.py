import random
from modules.ataque import Ataque

from modules.funcoes import scaling
from modules.item import Item
from modules.mundo import Mundo


class Personagem:

  def __init__(self, nome = "Pedrungas "+str(random.randint(0, 1000)), forca = 0, fortitude = 0, agilidade = 0, inteligencia = 0, vontade = 0,
               carisma = 0) -> None:
    self.nome = nome
    self.forca = forca
    self.fortidude = fortitude
    self.agilidade = agilidade
    self.inteligencia = inteligencia
    self.vontade = vontade
    self.carisma = carisma
    self.vida = 100
    self.ether = 100
    self.etherMax = 100
    self.fome = 100
    self.sede = 100
    self.sangue = 100
    
    self.desvio = 0
    
    self.resistencias = [] # Resistencias ou fraquezas a dano
    self.passivas = []
    self.status = [] # Status como queimado, congelado, etc
    self.inventario = []
    self.equipado = []
    self.ataques = []
    
    self.mundo = None
    self.time = "neutro"
    self.ai = "console"

  def setMundo(self, mundo):
    self.mundo = mundo
    pass
  
  def getMundo(self) -> Mundo:
    return self.mundo

  def getTime(self):
    return self.time
  
  def setTime(self, time):
    self.time = time
    pass
  def getNivel(self) -> int:
    soma = 0
    soma += scaling(stat = self.forca + self.fortidude + self.agilidade + self.inteligencia + self.vontade + self.carisma, scaling = 5)
    return soma

  def atacar(self, ataque):
    ataque.setOrigem(self)
    ataque.rolar(personagem=self)
    pass

  def habilidade(self):
    pass

  def aprenderAtaque(self, ataque):
    atk = Ataque(ataque)
    self.ataques.append(atk)
    pass

  def getTipo(self):
    return(self.__class__.__name__)

  def desequipar(self, item):   
    self.inventario.append(item)
    item.parente.remove(item)
    item.parente = self.inventario
    pass
  
  def receberItem(self, item):
    ite = Item(item)
    self.inventario.append(ite)
    pass
  
  def equipar(self, item):
    if item.getTipo() == "Item":
      for citem in self.equipado:
        if citem.slot == item.slot:
          self.desequipar(citem)

      self.equipado.append(item)
      item.parente = self.equipado
    pass

  def consumirItem(self):
    pass
