import finiteAutomata as lfa
import Lexic as al
import Syntax as syntax
import Semantic as se
import json
import sys

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print('Usage: python %s <input (full path)>' % sys.argv[0])
        exit(0)
    try:
        data = open(sys.argv[1])
    except:
        print('Could not open', sys.argv[1])
        exit(0)

states = {}
reserved = []
lines = data.read().splitlines()
lines = list(filter(lambda a: a != '', lines))

#Creates the finite automata structure
lfa.createAF(states, lines, reserved)
lfa.fillFinal(states)
lfa.determinize(states)
lfa.removeUnreachable(states)
lfa.insertErrorState(states)

with open('../testcases/automaton.json', 'w') as fp:
    json.dump(states, fp,  ensure_ascii=False, sort_keys=False)

#lexical analysis
output = al.Lexic(states, reserved)
if output.getError() == True:
    output.printErrors()
else:
    syntaxInput = output.getTS()
    syntaxOutput = syntax.Syntax(syntaxInput)
    result,semanthicInput = syntaxOutput.getResultAnalizer()
    if result:
        semanticOutput = se.Semanthic(semanthicInput)
        semanticOutput.declaraVar()
        semanticOutput.verificaTipo()
