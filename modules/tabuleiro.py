

class Tabuleiro:
    def __init__(self, tipoMundo):
        self.tabuleiro = []
        self._tipoMundo = tipoMundo
        self.arq = open('files/mapasRPG.txt', 'r')
        self.auxArq = self.arq.read()
        self.auxArq = self.auxArq.split('MAPA ')
    
    @property   
    def tipoMundo(self):
        return self._tipoMundo

    @tipoMundo.setter
    def tipoMundo(self, tipoMundo):
        self._tipoMundo = tipoMundo

    def inicializarTabuleiro(self):
        mapa = self.auxArq[self._tipoMundo]
        mapa = mapa.splitlines()
        mapa = mapa[1:]
        self.tabuleiro = []
        for stringsMapa in mapa:
            self.tabuleiro.append(stringsMapa.split(' '))
    

    def mostrarTabuleiro(self):
        for linha in self.tabuleiro:
            for coluna in linha:
                print(coluna, end=' ')
            print()
    '''
    def renderizarTabuleiro(self):
        # pode ser 3 mundos diferentes de si
        if self.tipoMundo == 1:
            for linha in self.tabuleiro:
                for coluna in linha:
                    pass
    ''' 