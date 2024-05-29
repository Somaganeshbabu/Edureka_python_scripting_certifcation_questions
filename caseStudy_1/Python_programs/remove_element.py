def remove_element(list, element):
    if element in list:
        list.remove(element)
    return list


my_list =[]
while True:
    value = input("enter value:- ")
    if value=="":
        break
    my_list.append(value)
print("my_list is", my_list)
element_to_remove = input("enter element to remove from list:-")
List_after_removing = remove_element(my_list,element_to_remove)
print(List_after_removing)