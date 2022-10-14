class listaItens: #Efeitos utilizados para skills, items, ataques, etc. Exemplos seriam Dano, Cura, AplicarStatus
    def __init__(self, lista = []):
        self.lista = lista
    
    def search(self, nome):
        for item in self.lista:
            if item.nomeunico == nome:
                return item
        return None
    
    def getLista(self):
        return(self.lista)
  
    def addLista(self, obj):
        self.list.append(obj)
