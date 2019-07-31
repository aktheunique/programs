string=input()
final=[]
for word in string.split():
    final.append(word[::-1])         #append the final each time by reversing the given word of string
print(' '.join(final))

    
