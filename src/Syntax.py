import xml.etree.ElementTree as ET

class Syntax:
    def __init__(self, TS):
        self.TS = TS
        self.fita = []
        self.getFita()
        self.parseLALR()

    def getFita(self):
        for token in self.TS:
            self.fita.append(token.id)

    def parseSymbols(self, msymbols, symbols):
        for symbol in msymbols:
            for i in symbol:
                symbols[i.attrib['Index']] = (i.attrib['Name'], i.attrib['Type'])

    #saves the production number as key and the rule name and rule size as value
    def parseProd(self, mproductions, productions):
        for prod in mproductions:
            for i in prod:
                productions[i.attrib['Index']] = (i.attrib['NonTerminalIndex'], i.attrib['SymbolCount'])

    def parseTable(self, mtable, LALRTable):
        for state in mtable:
            for action in state:
                LALRTable[action.attrib['Index']] = {}
                for i in action:
                    LALRTable[action.attrib['Index']][i.attrib['SymbolIndex']] = (i.attrib['Action'], i.attrib['Value'])

    def parseLALR(self):
        symbols = {}
        LALRTable = {}
        productions = {}

        tree = ET.parse('../testcases/LALRTable.xml')
        root = tree.getroot()

        print([(x.tag, x.attrib) for x in root]) # Lista os elementos filhos: nome e atributos
        msymbols = root.iter('m_Symbol')
        mproductions = root.iter('m_Production')
        mtable = root.iter('LALRTable')

        symbols = self.parseSymbols(msymbols, symbols)
        productions = self.parseProd(mproductions, productions)
        LALRTable = self.parseTable(mtable, LALRTable)
