num1,num2=map(int,input().split())
for i in range(1,1000):
    if i%num1==0 and i%num2==0:       #finding the number that divide both the numbers 
        print(i)
        break
