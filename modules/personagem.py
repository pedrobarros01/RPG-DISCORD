
class Personagem:
    def __init__(self, nome, forca, fortitude, agilidade, inteligencia, vontade, carisma) -> None:
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

    
    def atacar(self) -> float:
        pass

    def habilidade(self):
        pass

    def equiparArma(self):
        pass

    def consumirItem(self):
        pass