class Semanthic:

    def __init__(self,TS):
        self.TS = TS

    def verificaTipo(self):
        list_type = []
        for j,i in enumerate(self.TS): #percorre a TS procurando o symbolo de atribuicao
            if i.rotulo == '=':
                linha = i.linha
                sentenca = self.getSentenca(linha)
                for var in range(j-1,j+len(sentenca)):
                    if self.TS[var].type not in list_type and self.TS[var].type:
                        list_type.append(self.TS[var].type)
                if len(list_type) > 1:
                    print('erro semantico: Inconsistência de tipos linha: ', linha, list_type)
                    break
                del list_type[:]         
            

    def getSentenca(self,linha):
        sentenca = []
        for i in self.TS:
            if i.linha == linha and i.id == 'Id' or i.linha == linha and i.id == '=':
                sentenca.append(i.rotulo)
        return sentenca
