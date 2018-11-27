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
        tree = ET.parse('../testcases/LALRTable.xml')
        root = tree.getroot()

        print([(x.tag, x.attrib) for x in root]) # Lista os elementos filhos: nome e atributos
        msymbols = root.iter('m_Symbol')
        mproductions = root.iter('m_Production')
        mtable = root.iter('LALRTable')

        self.parseSymbols(msymbols)
        self.parseProd(mproductions)
        self.parseTable(mtable)

    def findLine(self, index):
        return self.TS[index].linha

    def addTS(self, stateFita):
        print("oi", self.fita)
        if self.fita[stateFita-1] == 'int':
            self.TS[stateFita].type = "%d"
        elif self.fita[stateFita-1] == 'float':
            self.TS[stateFita].type = "%f"
        elif self.fita[stateFita-1] == 'char':
            self.TS[stateFita].type = "%c"
        for i in self.TS:
            i.printToken()

    def syntaxAnalizer(self):
        stack = []
        stack.append('0')
        stateFita = 0 #localizacao do simbolo analisado
        statePilha = -1
        symbol = self.fita[stateFita] #symbol index
        index = self.symbols[symbol][0]

        if index not in self.LALRTable[stack[statePilha]].keys():
            print("Erro Sintático. Linha:", self.findLine(stateFita))
            action = '5'
        else:
            action, value = self.LALRTable[stack[statePilha]][index]

        while action != '4':
            symbol = self.fita[stateFita] #symbol index
            index = self.symbols[symbol][0]
            print(stack)
            if index not in self.LALRTable[stack[statePilha]].keys():
                print("Erro Sintático. Linha:", self.findLine(stateFita))
                action = '5'
                break
            else:
                action, value = self.LALRTable[stack[statePilha]][index]

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
                 action, value = self.LALRTable[stack[statePilha]][stack[-1]]
                 self.addTS(stateFita)
                 if action == '3': #salto
                    stack.append(value)
                    statePilha = -1
            elif action == '4':
                print('ACEITA')
