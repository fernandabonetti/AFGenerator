import numpy as np
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
symbols = {}
lines = data.read().splitlines()
initialState = 0
state = 64
states['S'] = {}
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if lines[i][0] != '<':                      #checks if it's not a grammar

            if not initialState:
                state += 1
                initialState = 1
                states['S'].setdefault(lines[i][j],[]).append(chr(state))
                states[chr(state)] = {}
            else:
                states[chr(state)].setdefault(lines[i][j],[]).append(chr(state+1))
                states[chr(state+1)] = {}
                state +=1
        else:
            rule = lines[i].replace(' ::= ', ' | ').split(' | ')
            print(rule)
            inputState = rule[0][1]
            print(inputState)
            for m in range(1, len(rule)):
                if rule[m][0] != 'eps':
                    states[inputState].setdefault(rule[m][0],[]).append(rule[m][2])
                else:
                    states[inputState].setdefault(None,[]).append('eps')

    initialState = 0

#prints the ordered states
for key, value in sorted(states.items()):
    print("{} : {}".format(key, value))
