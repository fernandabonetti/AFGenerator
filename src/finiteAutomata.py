#prints the ordered states
def orderedStates(states):
    for key, value in sorted(states.items()):
        print("{} : {}".format(key, value))

#insert and ε transition in empty final states
def fillFinal(states):
    for key, value in sorted(states.items()):
        if not states[key]:
            states[key].setdefault('ε',[])

#Determinize a given automata
def determinize(states):
    m = len(states)                                         #initial number of states
    for j in range(0, m):
        for key, value in sorted(states.items()):
            for symbol in value:
                if len(value[symbol]) > 1:                  #if it is indeterminized
                    newState = ''.join(value[symbol])
                    states[newState] = {}                   #creates a new state to determinize
                    for l in range(0, len(value[symbol])):
                        for k, v in states[value[symbol][l]].items():
                            for p in range(0, len(v)):
                                states[newState].setdefault(k,[]).append(v[p])
                    for old in value[symbol]:               #remove the indeterminized state
                        del[old]
                    value[symbol] = [newState]
        m = len(states)                                     #update the size of the states structure

#Iterates from the initial state to see if its reachable
def unreachable(stateList, initial, reachState, transitions):
    if transitions < 100:
        for symbol, state in stateList[initial].items():
            if state[0] == reachState or state[0] == 'ε':
                return False
            else:
                unreachable(stateList, state[0], reachState, transitions+1)
        return True
    return True

#Remove the unreachable states, from the initial state
def removeUnreachable(states):
    initialState = 'S'
    nstates = len(states)
    stateList = list(sorted(states.keys()))

    for i in range(0, len(stateList)):
        if i != initialState:
            reachState = stateList[i]
        for symbol, state in states[initialState].items():
            if state[0] != reachState and state[0] != 'ε':
                print(reachState)
                hue = unreachable(states, state[0], reachState, 0)
                print(hue)
                if hue:
                    print("State {} is unreachable. It shall be removed!\n", reachState)
                    states.pop(reachState)                  #the unreachable is removed from the automaton
