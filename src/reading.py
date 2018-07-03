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

for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if lines[i][0] != '<':                      #checks if it's a token or grammar
            if not initialState:
                states['S'] = {}
                state+= 1
                initialState = 1
                states['S'].setdefault(lines[i][j],[]).append(chr(state))
                states[chr(state)] = {}
            else:
                states[chr(state)].setdefault(lines[i][j],[]).append(chr(state+1))
                states[chr(state+1)] = {}
                state +=1
    initialState = 0
