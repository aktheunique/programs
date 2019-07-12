s=int(input())
factorial=1
if s==0:
    print(1)
else:
    for i in range(1,s+1):
        factorial=factorial*i
print(factorial)
