class Token:
    def __init__(self, rotulo, linha, id, state, erro, pointer):
        self.linha = linha
        self.rotulo = rotulo
        self.id = id
        self.state = state
        self.erro = erro
        self.pointer = pointer
        self.type = None

    def printToken(self):
        print(str(self.linha)+' '+self.rotulo+' '+self.id+' '+self.state+' '+str(self.erro)+ ' '+ str(self.pointer)+' '+ str(self.type))
