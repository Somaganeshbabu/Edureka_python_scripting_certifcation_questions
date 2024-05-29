def even_index(name):
    result = ""
    for i in range(len(name)):
        if i%2==0:
            result+=name[i]
    return result        
name = input("enter string:- ")
print(even_index(name))

# --------------- alternate solution -------------------
# name = input("enter name:- ")
# result = name[::2]
# print("string with even index", result)

# enter name:- H1e2l3l4o5w6o7r8l9d
# string with even index Helloworld
