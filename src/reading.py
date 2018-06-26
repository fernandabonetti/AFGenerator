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

tokens = {}
grammar = {}

lines = data.read().splitlines()
tokenteste = []

for line in lines:
    if line[:0] != '<':
        tokenteste = line

print(tokenteste)
