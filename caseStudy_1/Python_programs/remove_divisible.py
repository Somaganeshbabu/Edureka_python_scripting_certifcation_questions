def delete_divisibles(list,divisibles):
    return [ele for ele in list if all (ele % div !=0 for div in divisibles)]

my_list = []
while True:
    value = input("enter elements in list:- ")
    if value=="":
        break
    else:
        my_list.append(int(value))
print(my_list)

divisibles = []
while True:
    value = input("enter element to remove from list after divisible:- ")
    if value=="":
        break
    else:
        divisibles.append(int(value))
print(divisibles)

updated_list = delete_divisibles(my_list,divisibles)
print(updated_list)