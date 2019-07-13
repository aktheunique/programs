string_length=map(int,input())
name=input()

vowels=['a','e','i','o','u','A','E','I','O','U']
reversed_name="".join(reversed(name))
for char in reversed_name:
    if char in vowels:
        reversed_name=reversed_name.replace(char,"")
print(reversed_name)
        
