from itertools import permutations
inp=input()
for p in permutations(inp):
    p=''.join(p)
    print(p)
