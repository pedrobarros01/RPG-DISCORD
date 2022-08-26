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
}

def fight(actors):
  game = True;
  while(game):
    for i in actors:
      print(getStat(actors[i], "name"))
    

tempbattle = {}
tempbattle[1] = entitybase

fight(tempbattle)