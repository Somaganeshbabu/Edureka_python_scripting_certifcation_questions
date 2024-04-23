def sequence(n):
    value = 0
    for i in range(0,n+1):
        one_term = i/(i+1)
        value+= one_term
    return value


n=int(input("enter n value :- "))
series_numbers = sequence(n)
print(f"For given input {n} the answer is :-  ", series_numbers)