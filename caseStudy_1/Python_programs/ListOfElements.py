# def get_position(list_a):
#     positions=[]
#     for i in range(len(list_a)):
#         positions.append((i,list_a[i]))
#     return positions

# a = list(input("enter list of elements:-").split())
# print(get_position(a))

# input as 4 7 3 2 5 9
#  [(0, '4'), (1, '7'), (2, '3'), (3, '2'), (4, '5'), (5, '9')]

# ---------- alternative solution --------------

list_elements = []
while True:
    value = input("enter elements in list: ")
    if value == "":
        break
    list_elements.append(value)
print(list_elements)
pos = []
for i in range(len(list_elements)):
    pos.append((i,list_elements[i]))
print(pos) 