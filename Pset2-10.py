string=input()
l=[]
for char in string:
    if char=='X':
        l.append('A')
    elif char=='Y':
        l.append('B')
    elif char=='Z':
        l.append('C')
    else:
        l.append(chr(ord(char)+3))             #character to ascii and viceversa
print("".join(l))
