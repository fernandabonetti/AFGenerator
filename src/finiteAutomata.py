import heapq

def check(state):
    if state == 82:
        state+=2
    else:
        state+=1
    return state

def createAF(states, lines):
    initialState = 0
    state = 64
    states['S'] = {}

    for i in range(0, len(lines)):                          	# reads until the end of input
        if lines[i][0] != "<":                              	# Insert the language tokens
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
        else:                                             		 #Inserting the grammars
            rule = lines[i].replace(' ::= ', ' | ').split(' | ') #remove useless symbols from each grammar rule
            if rule[0][1] == 'S':                                #checks if it is the initial state 's'
                createState = 0
                inputState = rule[0][1]
                for m in range(1, len(rule)):
                    if rule[m][0] != 'ε':
                        if rule[0][1] != rule [m][1]:
                            createState = 1
                        states[inputState].setdefault(rule[m][0],[]).append(chr(state+1))
                    else:
                        states[inputState].setdefault('ε',[]).append('ε')
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
                        states[inputState].setdefault('ε',[]).append('ε')


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

#creates list of reachable states
def pushState(current,states,reachable):
    for i in states[current].values():
        if len(i) > 0 and i[0] not in reachable and i[0] != 'ε':
            reachable.append(i[0])
    return reachable


#Remove the unreachable states, from the initial state
def removeUnreachable(states):
    initialState = 'S'
    nstates = len(states)
    stateList = list(sorted(states.keys()))
    stateList.remove('S')
    reachable = []
    reachable = pushState(initialState,states,reachable)

    for i in reachable:
        reachable = pushState(i, states, reachable)

    for i in stateList:
        if i not in reachable:
            states.pop(i)


def insertErrorState(states):
    states['ERROR'] = {}
    for symbol, state in states.items():
        states[symbol].setdefault('err', []).append('ERROR')
