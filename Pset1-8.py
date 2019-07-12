name=input()
for x in name[:].split():
    name=name.replace(x,x.capitalize())
print(name)
