#prints the ordered states
def orderedStates(states):
    for key, value in sorted(states.items()):
        print("{} : {}".format(key, value))

#Determinize a given automata
def determinize(states):
