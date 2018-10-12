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

#Check if a state is reachable by the initial state 'S'
def isUnreachable(stateList, states, current, reachState, transitions):
    lookupStates = []
    if transitions > 100:
        return True

    #check if its reachable in the current state
    if not any([reachState == state[0] for state in states[current].values()]):
        for symbol, state in states[current].items():
            if reachState not in state:
                for st in state:
                    if st not in lookupStates and st != 'ε':
                        heapq.heappush(lookupStates, st)

    #check  each of the children if it reaches
    while(len(lookupStates) > 0):
        new = heapq.heappop(lookupStates)
        if not isUnreachable(stateList, states, new, reachState, transitions+1):
            return False
        else:
            return True


#Remove the unreachable states, from the initial state
def removeUnreachable(states):
    initialState = 'S'
    nstates = len(states)
    stateList = list(sorted(states.keys()))
    stateList.remove('S')

    for i in range(0, len(stateList)):
        reachState = stateList[i]
        if not any([reachState == state[0] for state in states[initialState].values()]):
            if isUnreachable(stateList, states, initialState, reachState, 0):
                print("State {} is unreachable. It shall be removed!\n".format(reachState))
                states.pop(reachState)

def insertErrorState(states):
    states['ERROR'] = {}
    for symbol, state in states.items():
        states[symbol].setdefault('err', []).append('ERROR')
