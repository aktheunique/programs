length=int(input())
elements=list(map(int,input().split()))
for i in range(len(elements)):
    if elements.count(i)==1:
        print(i)
        break
