from modules import personagem
from modules.efeito import Efeito
from modules.funcoes import send_text


class Dano(Efeito): 
    def __init__(self, delay = 0, origem = None, hitcancela = False, alvo = None, tipo_dano = "fisico", subtipo_dano = "na", dano = 0
        ) -> None:
        self.delay = delay 
        self.origem = origem 
        self.hitcancela = hitcancela 
        self.alvo = alvo
        self.tipo_dano = tipo_dano
        self.subtipo_dano = subtipo_dano
        self.dano = dano
    
    def efeito(self):
        resist = 1
        
        
        for resistencia in self.alvo.resistencias:
            if resistencia.tipo == self.tipo_dano:
                resist = resist + resistencia.valor
                
        total_dano = 0

                
        total_dano = self.dano * resist
        send_text(self.alvo.nome + " recebeu " + str(total_dano) + " de dano " + self.tipo_dano + "!")
        self.alvo.vida = self.alvo.vida - total_dano
        