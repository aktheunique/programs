string=input()
count=0
for i in string:
    if not i.isdigit() and not i.isalpha():
        count+=1
print(count)
