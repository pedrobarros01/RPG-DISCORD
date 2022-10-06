class Item:
  def __init__(self, nomeunico = "default_item", 
    nomevisual = "Item Padrão", #tipo = "consumivel", 
    quantidade = 1, desc = "Descrição Padrão! Você provavelmente não deveria ter esse item.",
    slot = "consumivel"
    ) -> None:
    self.nomeunico = nomeunico
    self.nomevisual = nomevisual
    self.desc = desc
    self.quantidade = quantidade
    self.slot = slot
    self.requerimentos = []
    self.parente = None

    self.efeitos = []
      
    #usados apenas por armas
    self.escalamentos = []

  def getTipo(self):
    return(self.__class__.__name__)


  def examinar(self):
    print(f"""{self.nomevisual}
{self.desc}
""")
    #self.tipo = tipo #Listagem de tipos de items: consumivel, armadura (capacete, peitoral, etc.), arma, missaoitem