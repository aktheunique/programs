n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
l1=list(map(int,input().split()))
for i in range(len(l1)):
    if l[-1]==l1[i]:
        print(l[-1],end=" ")
    else:
        if l[-1]<l1[i]:
            print(l1[i],end=" ")
        else:
            print(l1[i-1])
            

    
