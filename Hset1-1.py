no_of_elements=int(input())
list_of_elements=list(map(int,input().split()))
l=[]
for digit in list_of_elements:
    if list_of_elements.count(digit)>1:
        if str(digit) not in l:
            l.append(str(digit))
if len(l)==0:
    print("unique")
else:
    list_of_elements.sort()
    print(" ".join(l))
