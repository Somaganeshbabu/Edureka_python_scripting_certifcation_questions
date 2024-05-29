def print_missing_value(my_list,N):
    original_sum =( N*(N+1))/2
    sum = 0
    for i in range (len(my_list)):
        sum += my_list[i]
    missing_number = original_sum-sum
    return int(missing_number)


my_list =[]
while True:
    value = input("enter value:- ")
    if value=="":
        break
    my_list.append(int(value))
print("my_list is", my_list)
N= int(input("enter Number of values present in array :- "))
result = print_missing_value(my_list,N)
print(result)