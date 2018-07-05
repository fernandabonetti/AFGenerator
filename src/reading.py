#import numpy as np
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
lines = list(filter(lambda a: a != '', lines))
initialState = 0
state = 64
states['S'] = {}


def check(state):
    if state == 82:
        state+=2
    else:
        state+=1
    return state

# Creates the finite automata structure
for i in range(0, len(lines)):                          #reads until the end of input
    if lines[i][0] != "<":                              # Insert the language tokens
        for j in range(0, len(lines[i])):
            if not initialState:
                state = check(state)
                initialState = 1
                states['S'].setdefault(lines[i][j],[]).append(chr(state))
                states[chr(state)] = {}
            else:
                state = check(state)
                if state == 84:
                    states[chr(state-2)].setdefault(lines[i][j],[]).append(chr(state))
                else:
                    states[chr(state-1)].setdefault(lines[i][j],[]).append(chr(state))
                states[chr(state)] = {}
        initialState = 0
    else:                                        # Inserting the grammars
        rule = lines[i].replace(' ::= ', ' | ').split(' | ')
        if rule[0][1] == 'S':
            createState = 0
            inputState = rule[0][1]
            for m in range(1, len(rule)):
                if rule[m][0] != 'ε':
                    if rule[0][1] != rule [m][1]:
                        createState = 1
                    states[inputState].setdefault(rule[m][0],[]).append(chr(state+1))
                else:
                    states[inputState].setdefault(None,[]).append('ε')
            if createState == 1:
                state = check(state)
                states[chr(state)]={}
        else:
            inputState = chr(state)
            for m in range(1, len(rule)):
                if rule[m][0] != 'ε':
                    if rule[0][1] != rule[m][2]:
                        state = check(state)
                        states[chr(state)]={}
                    states[inputState].setdefault(rule[m][0],[]).append(chr(state))
                else:
                    states[inputState].setdefault(None,[]).append('ε')


print("Non-Deterministic Finite Automata:\n")
lfa.orderedStates(states)
lfa.determinize(states)
