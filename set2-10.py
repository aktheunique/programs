n=int(input())
multiples_list=[]
for i in range(1,n+1):
    multiples_list.append(str(n*i))     #append the list each time with its multiple
print(" ".join(multiples_list))
