# def char_counts(chars):
#     char_count={}
#     for char in chars:
#         if char in char_count:
#             char_count[char]+=1
#         else:
#             char_count[char] = 1
#     return char_count

# input_string = input("enter string to count:- ")
# print(char_counts(input_string))

# # enter string to count:- abcdefgabc
# # {'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1, 'g': 1}

#----------another approach -------
def char_count(name):
    return {char:name.count(char) for char in name} #syntax : {key:value for item in iterable}

name = input("enter name to count chars:- ")
print(char_count(name))

