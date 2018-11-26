import xml.etree.ElementTree as ET

class Syntax:
    def __init__(self, TS):
        self.TS = TS
        self.fita = []
        self.symbols = {}
        self.LALRTable = {}
        self.productions = {}
        self.getFita()
        self.parseLALR()
        self.syntaxAnalizer()

    def getFita(self):
        for token in self.TS:
            self.fita.append(token.id)

    def parseSymbols(self, msymbols):
        for symbol in msymbols:
            for i in symbol:
                self.symbols[i.attrib['Name']] = (i.attrib['Index'], i.attrib['Type'])

    #saves the production number as key and the rule name and rule size as value
    def parseProd(self, mproductions):
        for prod in mproductions:
            for i in prod:
                self.productions[i.attrib['Index']] = (i.attrib['NonTerminalIndex'], i.attrib['SymbolCount'])

    def parseTable(self, mtable):
        for state in mtable:
            for action in state:
                self.LALRTable[action.attrib['Index']] = {}
                for i in action:
                    self.LALRTable[action.attrib['Index']][i.attrib['SymbolIndex']] = (i.attrib['Action'], i.attrib['Value'])

    def parseLALR(self):
        tree = ET.parse('../testcases/JulianaDeJulho.xml')
        root = tree.getroot()

        print([(x.tag, x.attrib) for x in root]) # Lista os elementos filhos: nome e atributos
        msymbols = root.iter('m_Symbol')
        mproductions = root.iter('m_Production')
        mtable = root.iter('LALRTable')

        self.parseSymbols(msymbols)
        self.parseProd(mproductions)
        self.parseTable(mtable)

    def syntaxAnalizer(self):
        stack = []
        stack.append('0')
        stateFita = 0 #localizacao do simbolo analisado
        statePilha = -1
        symbol = self.fita[stateFita] #symbol index
        index = self.symbols[symbol][0]
        action,value = self.LALRTable[stack[statePilha]][index]    
        while action != '4':
            symbol = self.fita[stateFita] #symbol index
            index = self.symbols[symbol][0]
            action,value = self.LALRTable[stack[statePilha]][index]
            print(action,value)
            if action == '1':
                stack.append(index)
                stack.append(value)
                stateFita += 1
            elif action == '2':
                #desempilha o dobro do tamanho da qtd produções
                 prod, size = self.productions[value]
                 size = int(size)*2
                 del stack[len(stack)-size:]
                #empilha o nome da producao reduzida + o local indicado 
                 stack.append(prod)
                 statePilha = -2
                 action,value = self.LALRTable[stack[statePilha]][stack[-1]]
                 if action == '3': #salto
                    stack.append(value)
                    statePilha = -1
            elif action == '4':
                print('ACEITA')

        '''for symbol in self.fita:
            print(stack)
            print(symbol)
            index = self.symbols[symbol][0]
            #action, value = self.LALRTable[stack[-1]][index]
            #print(action,value)
            print(index)
            if action == '1':
                stack.append(index)
                stack.append(value)
            elif action == '2':
                prod, size = self.productions[value]
                size = int(size) * 2
                del stack[len(stack)-size:]
                ac, salto = self.LALRTable[stack[-1]][prod]
                print('pilha depois de eliminada',stack)
                print(ac,salto)    
                stack.append(prod)
                stack.append(salto)
                action, value = self.LALRTable[stack[-1]][index]
               '''        

