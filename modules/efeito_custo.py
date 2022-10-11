from xmlrpc.client import Boolean
from modules.efeito import Efeito
from modules.funcoes import send_text


class Custo(Efeito): 
    def __init__(self, delay = 0, origem = None, hitcancela = False, alvo = None, custo="ether", quantidade=0
        ) -> None:
        self.custo = custo
        self.quantidade = quantidade
        self.delay = delay 
        self.origem = origem 
        self.hitcancela = hitcancela 
        self.alvo = alvo
    
    def efeito(self) -> Boolean:
        if(self.alvo[self.custo] and self.alvo[self.custo] >= self.quantidade):
            self.alvo[self.custo] = self.alvo[self.custo] - self.quantidade
            return True
        else:
            return False