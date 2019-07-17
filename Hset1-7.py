numbers=int(input())
final_list=[]
list_of_elements=list(map(int,input().split()))

for ele in range(numbers):
    if list_of_elements[ele]%2==0 and ele%2!=0:     #even number at odd position
        final_list.append(str(list_of_elements[ele]))
    else:
        if list_of_elements[ele]%2!=0 and ele%2==0:  #odd number at even position
            final_list.append(str(list_of_elements[ele]))
print(" ".join(final_list))
