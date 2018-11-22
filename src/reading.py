import finiteAutomata as lfa
import Lexic as al
import Syntax as syntax
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

# Creates the finite automata structure
lfa.createAF(states, lines, reserved)
print(reserved)
lfa.fillFinal(states)
lfa.determinize(states)
print("Determinized automata")
lfa.removeUnreachable(states)
lfa.insertErrorState(states)
lfa.orderedStates(states)

#lexical analysis
output = al.Lexic(states, reserved)
if output.getError() == True:
    output.printErrors()
else:
    syntaxInput = output.getTS()
    syntaxOutput = syntax.Syntax(syntaxInput)
