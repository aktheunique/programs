number=int(input())
for i in range(2,number+1):
    if number%i==0:
        flag=0
        for j in range(2,i+1):
            if i%j==0 and j!=i:
                flag=1
                break
        if flag==0:
            print(i,end=" ")
            
        
