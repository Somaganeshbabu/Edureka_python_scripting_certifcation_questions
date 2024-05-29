
# ---------- efficient approach ------------

# def count_Zeros(n):
#     count = 0
#     while(n>=5):
#         n=n//5
#         count+=n
#     return count


# n = int(input("enter n value"))
# print(count_Zeros(n))

# ------------ 2nd approach -------------------
import math
n = 100
factorial = math.factorial(n)
print(factorial)
count=0
fact_string = str(factorial)
for char in reversed(fact_string):
    if char =='0':
        count+=1
    else:
        break
print(count)