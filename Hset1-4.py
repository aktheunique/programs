seq=int(input())
ele=list(map(int,input().split()))
l=[]
for digit in range(seq):
    if ele.count(digit)==1:
        if str(digit) not in l:
            l.append(str(digit))
            break
if len(l)==0:
    print("-1")
print("".join(l))
        
