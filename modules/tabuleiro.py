


class Tabuleiro:
    def __init__(self, coluna, linhas, tipoMundo) -> None:
        self.tabuleiro = []
        for i in range(0, linhas):
            listaAux = []
            for j in range(0, coluna):
                self.tabuleiro.append(listaAux)
        self.tipoMundo = tipoMundo

    def mostrarTabuleiro(self):
        for campo in self.tabuleiro:
            print(campo)
    '''
    def renderizarTabuleiro(self):
        # pode ser 3 mundos diferentes de si
        if self.tipoMundo == 1:
            for linha in self.tabuleiro:
                for coluna in linha:
                    pass
    ''' 