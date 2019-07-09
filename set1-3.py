s=input()
l=['a','e','i','o','u','A','E','I','O','U']
if((int(ord(s))>=65 and int(ord(s))<=90) or(int(ord(s))>=97 and int(ord(s))<=122)):
	if s in l:
		print("Vowel")
	else:
		print("Consonant")
elif((int(ord(s))>=48 and int(ord(s))<=57)):
	pass
else:
	print("invalid")
