import heapq

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

def isUnreachable(stateList, states, actual, reachState, lookupStates, transitions):
    if transitions < 100:
        for symbol, state in states[actual].items():
            if reachState not in state:
                for st in state:
                    if st not in lookupStates and st != 'ε':
                        heapq.heappush(lookupStates, st)
                #check  each of the children if it reaches
                new = heapq.heappop(lookupStates)
                if not isUnreachable(stateList, states, new, reachState, lookupStates, transitions+1):
                    return False
                else:
                    return True
            return False
    return True

#Remove the unreachable states, from the initial state
def removeUnreachable(states):
    lookupStates = []
    initialState = 'S'
    nstates = len(states)
    stateList = list(sorted(states.keys()))

    for i in range(0, len(stateList)):
        if i != initialState:
            reachState = stateList[i]
        if reachState not in states[initialState]:
            if isUnreachable(stateList, states, initialState, reachState, lookupStates, 0):
                print("State {} is unreachable. It shall be removed!\n".format(reachState))
                states.pop(reachState)
