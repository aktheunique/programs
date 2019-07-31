n,k=map(int,input().split())
x=list(input().split())
y=list(input().split())

for i in range(n):
    if x[i] in y:
        y.remove(x[i])
    else:
        continue
print("YES" if len(y)==0 else "NO")
    
