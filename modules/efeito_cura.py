from modules.efeito import Efeito
from modules.funcoes import send_text


class Cura(Efeito): 
    def __init__(self, delay = 0, origem = None, hitcancela = False, alvo = None, tipo_cura = "magica", #natural, magica, vazia
                 cura = 0
        ) -> None:
        self.delay = delay 
        self.origem = origem 
        self.hitcancela = hitcancela 
        self.alvo = alvo
        self.tipo_dano = tipo_cura
        self.cura = cura
    
    def efeito(self):
        resist = 1
        total_cura = self.cura * resist
        send_text(self.alvo.nome + " recebeu " + str(total_cura) + " de cura " + self.tipo_dano + "!")
        self.alvo.vida = self.alvo.vida + total_cura
