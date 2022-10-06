class Personagem:

  def __init__(self, nome, forca, fortitude, agilidade, inteligencia, vontade,
               carisma) -> None:
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
    self.inventario = []
    self.equipado = []

  def atacar(self) -> float:
    pass

  def habilidade(self):
    pass

  def getTipo(self):
    return(self.__class__.__name__)

  def desequipar(self, item):   
    self.inventario.append(item)
    item.parente.remove(item)
    item.parente = self.inventario
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
