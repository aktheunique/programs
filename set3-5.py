s=int(input())

list_of_elements=input().split()
final=" ".join(sorted(list_of_elements))
length=len(final)//2
print(final[length])
