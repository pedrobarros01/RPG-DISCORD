import random 

debugstatus = True

def send_text(texto):
    print(texto)

def debugconsole(texto):
    if(debugstatus == True):
        print("[D] "+texto)


def rolar(dados = 1, faces = 6, modificador = 0):
    resultado = 0
    for i in range(dados):
        resultado += random.randint(1, faces)
    
    debugconsole("Rolou " + str(dados) + "d" + str(faces) + " + " + str(modificador) + " e obteve " + str(resultado + modificador))    
    
    return resultado + modificador

def scaling(stat = 0, scaling = 5):
    return int(stat/scaling)

def perguntaArray(array):
    for i in range(len(array)):
        print("[" + str(i) + "] " + array[i])
    resposta = input(">>> ")
    
    if array[i] != None:
        return resposta
    else:
        return perguntaArray(array)
    
def escolherAlvo(array):
    for i in range(len(array)):
        print("[" + str(i) + "] " + array[i].nome)
    resposta = int(input(">>> "))
    
    if array[resposta] != None:
        return array[resposta]
    else:
        return escolherAlvo(array)