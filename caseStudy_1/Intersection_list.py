list_a = input("enter list of elements in list_a:- ")
list_b = input("enter list of elements in list_b:- ")
intersection = set((list_a).split(',')) & set((list_b).split(','))
print(intersection)

# enter list of elements in list_a:- [1,3,6,78,35,55]
# enter list of elements in list_b:- [12,24,35,24,88,120,155]
# {'35'}