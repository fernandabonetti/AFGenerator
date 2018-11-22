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

    def syntaxAnalizer(self):
        stack = []
        stack.append('0')
        #print(self.LALRTable)
        print(self.productions)
        for symbol in self.fita:
            print(stack)
            index = self.symbols[symbol][0]
            action, value = self.LALRTable[stack[-1]][index]
            if action == '1':
                stack.append(value)
            elif action == '2':
                prod, size = self.productions[value]
                size = int(size) * 2
                del stack[len(stack)-size:-1]
                print(stack)
