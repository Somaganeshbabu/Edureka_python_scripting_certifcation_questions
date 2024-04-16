def remove_duplicates(list_a):
    unique_list= []

    for i in list_a:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


list_a = [12,24,35,24,88,120,155,88,120,155]
result = remove_duplicates(list_a)
print(result)
