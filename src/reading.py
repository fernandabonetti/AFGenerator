import finiteAutomata as lfa
import lexic as al
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
lines = data.read().splitlines()
lines = list(filter(lambda a: a != '', lines))
# Creates the finite automata structure
lfa.createAF(states, lines)
lfa.fillFinal(states)
lfa.determinize(states)
print("Determinized automata")
#lfa.orderedStates(states)
lfa.removeUnreachable(states)
lfa.insertErrorState(states)
lfa.orderedStates(states)

#lexical analysis
tokens = al.readFonte()
al.recognize(tokens, states)
