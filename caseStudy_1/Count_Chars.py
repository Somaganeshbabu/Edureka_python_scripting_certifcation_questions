def char_counts(chars):
    char_count={}
    for char in chars:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char] = 1
    return char_count

input_string = input("enter string to count:- ")
print(char_counts(input_string))

# enter string to count:- abcdefgabc
# {'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1, 'g': 1}