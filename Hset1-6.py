no_of_numbers=int(input())
final=[]
l=list(map(int,input().split()))
count=0
for i in range(no_of_numbers):
    if l[i] in final:           #if the element in first list is equal to element in second element
        count=1                 #assign it to new variable and print
        final=l[i]
        break
    else:
        final.append(l[i])      #else add it to the new list
if count==0:
    print("unique")
else:
    print(final)

    
        
