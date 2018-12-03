
class Semanthic:


    def __init__(self,TS):
        self.TS = TS

    def verificaTipo(self):
        list_type = []
        for j,i in enumerate(self.TS): #percorre a TS procurando o symbolo de atribuicao
            if i.rotulo == '=':
                linha = i.linha
                sentenca = self.getSentenca(linha)
                for var in range(j-1, j+len(sentenca)):
                    if self.TS[var].type not in list_type:
                         if self.TS[var].id == 'Id':
                             list_type.append(self.TS[var].type)
                         elif self.TS[var].id == 'digit':
                            num = self.TS[var].rotulo.split('.')
                            if len(num) > 1:
                                self.TS[var].type = '%f'
                            else:
                                self.TS[var].type = '%d'
                            if self.TS[var].type not in list_type:
                                list_type.append(self.TS[var].type)
                if len(list_type) > 1:
                    print('SemanticError: Inconsistência de tipos, linha: ', linha, list_type)
                del list_type[:]

    def declaraVar(self):
        for i in self.TS:
            if i.id == 'Id' and i.type == None:
                print('SemanticError: variável não declarada {}, linha: {}'.format(i.rotulo,i.linha))

    def getSentenca(self,linha):
        sentenca = []
        for i in self.TS:
            if i.linha == linha and i.id == 'Id' or i.linha == linha and i.id == '=':
                if i.rotulo not in sentenca:
                    sentenca.append(i.rotulo)
        return sentenca
