from itertools import permutations 
def Permutations(inp): 
    p=permutations(inp)
    for per in list(p):
        print(''.join(per)) 
inp=input()
Permutations(inp) 
