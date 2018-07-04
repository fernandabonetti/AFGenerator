import numpy as np
import finiteAutomata as lfa
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
lines.remove('')
initialState = 0
state = 64
states['S'] = {}

# Creates the finite automata structure
for i in range(0, len(lines)):                          #reads until the end of input
    if lines[i][0] != "<":                              # Insert the language tokens
        for j in range(0, len(lines[i])):
            if not initialState:
                state += 1
                initialState = 1
                states['S'].setdefault(lines[i][j],[]).append(chr(state))
                states[chr(state)] = {}
            else:
                states[chr(state)].setdefault(lines[i][j],[]).append(chr(state+1))
                states[chr(state+1)] = {}
                state +=1
        initialState = 0
    else:                                             # Inserting the grammars
        rule = lines[i].replace(' ::= ', ' | ').split(' | ')
        print(rule)
        inputState = rule[0][1]
        for m in range(1, len(rule)):
            if rule[m][0] != 'ε':
                states[inputState].setdefault(rule[m][0],[]).append(rule[m][2])
            else:
                states[inputState].setdefault(None,[]).append('ε')

print("Non-Deterministic Finite Automata:\n")
lfa.orderedStates(states)
