def readFonte():
    arquivo = open('../testcases/fonte.txt', 'r')
    token_in = []
    for token in arquivo:
        i = token.strip().split(' ')
        token_in.append(i)
    return token_in

def recognize(token_in, states):
    current = 'S'
    for line in token_in:
        for token in line:
            for i in token:
                if i in states[current].keys():
                    current = states[current][i][0]
        if 'ε' in states[current].keys():
            print("ACEITEI")        
