number=int(input())
elements=list(map(int,input().split()))
l=[]
for value in range(number):
    if elements[value]==value:
        l.append(str(value))
        l.sort()
print(" ".join(l))
