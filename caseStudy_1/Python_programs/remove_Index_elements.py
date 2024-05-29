def remove_indexes_elements(list, indexes):
    return [ele for index,ele in enumerate(list) if index not in indexes]

my_list = []
while True:
    value = input("enter elements in list:- ")
    if value=="":
        break
    else:
        my_list.append(value)
print(my_list)

Indexes = []
while True:
    value = input("enter index to remove from list:- ")
    if value=="":
        break
    else:
        Indexes.append(int(value))
print(Indexes)
updated_list = remove_indexes_elements(my_list,Indexes)
print("list after removing mentioned indexes:-", updated_list)