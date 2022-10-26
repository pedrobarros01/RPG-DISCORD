from modules import personagem, item, efeito
from modules.ataque import Ataque
from modules.efeito_dano import Dano
from modules.itens import listaItens
from modules.mundo import Mundo
from modules.ataques import listaAtaques
from modules.tabuleiro import Tabuleiro

'''Personagem = personagem.Personagem
Efeito = efeito.Efeito
Item = item.Item

def getStat(entity, stat):
  if (entity[stat]):
    return entity[stat]

def setStat(entity, stat, value):
  if (entity[stat]):
    entity[stat] = value

entitybase = {
  "name":"John",
  "forca":0,
  "fortitude":0,
  "agilidade":0,
  "inteligencia":0,
  "vontade":0,
  "carisma":0,

  "armasleves":0,
  "armasmedias":0,
  "armaspesadas":0,

  "vida":100,
  "vidamax":100,

  "ether":100,
  "ethermax":100,

  "fome":100,
  "sede":100,
  "sangue":100,

  "skills":{},
  "cartas":{},
  "rep":{
    "Etrea":0,
    "Colmeia":0,
    "Autoridade":0,
    "Bandidos":-20,
  },

  "inventario":{},

  "capacete":None,
  "ombreiras":None,
  "sapatos":None,

  "aneis":{},

  "maodireita":None,
  "maoesquerda":None,

  "armadura":None,

  "efeitosdestatus":{},

  "attacktime":0
}'''



'''bot = Personagem("BOT FORTE", 100, 0, 0, 0, 0, 0)
espada = Item()
bot.equipar(espada)
bot.desequipar(espada)
bot.setTime("Time 2")
espada.examinar()

inimigo = Personagem(nome = "BOT 2")

mundot = Mundo("Mundo de Teste",[bot, inimigo])
bot.setMundo(mundot)
inimigo.setMundo(mundot)
inimigo.setTime("Time 1")

listaAtaques = listaAtaques()
ataquebasico = listaAtaques.search("soco")

inimigo.aprenderAtaque(ataquebasico)
bot.aprenderAtaque(ataquebasico)


inimigo.atacar(ataquebasico)
bot.atacar(ataquebasico)

'''
# C representa o caminho a se seguir, A representa "paisagem"
tabuleiro = Tabuleiro(1)
tabuleiro.tipoMundo = 2
tabuleiro.inicializarTabuleiro()
tabuleiro.mostrarTabuleiro()

