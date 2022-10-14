from modules.ataque import Ataque
from modules.efeito_dano import Dano


class listaAtaques: #Efeitos utilizados para skills, items, ataques, etc. Exemplos seriam Dano, Cura, AplicarStatus
    def __init__(self, lista = []):
        self.lista = lista
        lista.append(Ataque(efeitos_sucesso=[Dano(origem="self",dano=5) ],alvo="unico_inimigo"))
    
    def search(self, nome):
        for item in self.lista:
            if item.nome == nome:
                return item
        return None
    
    def getLista(self):
        return(self.lista)
  
    def addLista(self, obj):
        self.list.append(obj)
