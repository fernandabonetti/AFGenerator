class Token:
    def __init__(self, rotulo, linha, id, state, erro):
        self.linha = linha
        self.rotulo = rotulo
        self.id = id
        self.state = state
        self.erro = erro

    def printToken(self):
        print(str(self.linha)+' '+self.rotulo+' '+self.id+' '+self.state+' '+str(self.erro))
