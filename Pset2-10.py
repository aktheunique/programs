string=input()
l=[]
for char in string:
    l.append(chr(ord(char)+3))        #character to ascii and ascii to character 
print("".join(l))
