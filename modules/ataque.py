import random

from modules.funcoes import debugconsole, escolherAlvo, rolar, scaling, send_text


class Ataque():
    def __init__(self, efeitos_sucesso = [], efeitos_fracasso = [], 
                 nome = "soco",
                 alvo = "unico_inimigo", #unico, todos, aleatorio, unico_aliado, todos_aliado, aleatorio_aliado, unico_inimigo, todos_inimigo, aleatorio_inimigo
                 foco = "na", #o ataque apenas pode dar dar alvo em personagens com esse status. Exemplo: "sangrando" ou "desmaiado"
                 tempo = 0, #tempo que o ataque leva para ser usado novamente
                 testeataque = "forca",
                 testedefesa = "desvio", #teste de resistencia que o alvo faz para evitar o ataque; Exemplo: "na" (nao tem teste, acerta sempre), "fortitude", "desvio" (soma metade do nivel)
                 ):
        self.alvo = alvo
        self.nome = nome
        self.originalnome = nome
        self.foco = foco
        self.efeitos_sucesso = efeitos_sucesso
        self.efeitos_fracasso = efeitos_fracasso
        self.tempo = tempo
        self.testeataque = testeataque
        self.testedefesa = testedefesa
        
        
    def getAlvo(self, personagem):
        if(personagem.getMundo() != None):
            if(self.alvo == "unico"):
                    alvos = personagem.mundo.getPersonagens()
                    calvo = escolherAlvo(alvos)
            elif(self.alvo == "unico_inimigo"):
                    alvos = personagem.mundo.getInimigos(personagem.getTime())
                    calvo = escolherAlvo(alvos)
            else:
                    alvos = personagem.mundo.getPersonagens()
                    calvo = escolherAlvo(alvos) 
            return calvo
                
        
    def rolar(self, personagem = None):
        ataqueroll = 0
        calvo = self.getAlvo(personagem)
        
        if(calvo == None):
            debugconsole("Nao ha alvos para o ataque")
            return
        
        if(getattr(personagem,self.testeataque,None) != None):
            atkatb = getattr(personagem,self.testeataque)
            ataqueroll = rolar(dados = 3+scaling(atkatb), modificador = personagem.getNivel())
        else:
            ataqueroll = rolar(dados = 3+scaling(personagem.forca), modificador = personagem.getNivel())
        
        if(self.testedefesa == "na" or self.testeataque == "na"):
            self.executar(self.efeitos_sucesso)
        
        elif(self.testedefesa == "desvio"):
            ddesvio = rolar(dados = 3+scaling(stat=calvo.agilidade,scaling=10), faces = 6, modificador = int(personagem.getNivel()/2))
            debugconsole("Ataque: "+str(ataqueroll)+" vs "+str(ddesvio))
            if(ddesvio < ataqueroll):
                send_text("O ataque de "+personagem.nome+" acertou "+calvo.nome)
                self.executar(self.efeitos_sucesso)
            else:
                send_text("O ataque de "+personagem.nome+" falhou em "+calvo.nome)
                self.executar(self.efeitos_fracasso)
    
    def executar(self, efeitos):
        for efeito in efeitos:
            if(efeito.getTipo() == "Custo"):
                if(efeito.efeito() == False):
                    break
                else:    
                    efeito.efeito()
                    
        pass