integer=int(input())
list_of_numbers=list(input().split())

list_of_numbers.sort()
final="".join(list_of_numbers[::-1])
print(int(final))
