#prints the ordered states
def orderedStates(states):
    for key, value in sorted(states.items()):
        print("{} : {}".format(key, value))

#Determinize a given automata
def determinize(states):
    for key, value in sorted(states.items()):
        for symbol in value:
            if len(value[symbol]) > 1:
                print("determinizar")
