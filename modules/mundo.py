class Mundo():
    def __init__(self, nome = "Mundo", personagens = []):
        self.nome = nome
        self.personagens = personagens
        
    def getInimigos(self, time):
        inimigos = []
        for personagem in self.personagens:
            if personagem.getTime() != time:
                inimigos.append(personagem)
        return inimigos
    
    def getAliados(self, time):
        aliados = []
        for personagem in self.personagens:
            if personagem.getTime() == time:
                aliados.append(personagem)
        return aliados
        
    def getPersonagens(self):
        return self.personagens
    
    def addPersonagem(self, personagem):
        self.personagens.append(personagem)
        
    def removePersonagem(self, personagem):
        self.personagens.remove(personagem)