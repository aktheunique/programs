string=input()
maximum_count=0
letter=''
for char in range(len(string)):
    c=string.count(string[char])
    if maximum_count<c:
        maximum_count=c
        l=string[char]
print(l)

