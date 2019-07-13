s1,s2=input().split()
count=0
for i in range(0,len(s1)):
    for j in range(0,i+1):
        if s1[i]!=s2[j]:
            count+=1
            break
if count==1:
    print("yes")
else:
    print("no")
