n=int(input())
if n>2:
for i in range(2,n):
	if n%i:
		flag=1
		break
if flag==1:
	print("no")
else:
	print("yes")
