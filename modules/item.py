class Item:
  def __init__(self, nomeunico = "default_item", 
    nomevisual = "Item Padrão", #tipo = "consumivel", 
    quantidade = 1, desc = "Descrição Padrão! Você provavelmente não deveria ter esse item."
    ) -> None:
    self.nomeunico = nomeunico
    self.nomevisual = nomevisual
    self.desc = desc
    self.quantidade = quantidade
    #self.tipo = tipo #Listagem de tipos de items: consumivel, armadura (capacete, peitoral, etc.), arma, missaoitem
