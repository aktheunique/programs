lower,upper=map(int,input().split())
final_list=[]
for i in range(lower+1,upper):
    sum=0
    new_list=list(map(int,list(str(i))))   #number to a list of its digits
    length=len(new_list)                   #length of the list
    for number in new_list:
        sum+=(number**length)              
    if sum==i:                             
        final_list.append(str(i))
    else:
        pass
print(" ".join(final_list))
