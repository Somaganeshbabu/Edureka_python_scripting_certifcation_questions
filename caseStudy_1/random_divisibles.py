import random
def random_generator(count,divisibles):
    numbers = []
    for _ in range(count):
        rand = random.randint(0,1000)
        while not all(rand % div==0 for div in divisibles):
            rand = random.randint(0,10)
        numbers.append(rand)
    return numbers

count = int(input("enter how many values you should be generated :- "))
divisibles = []
while True:
    value = input("enter value which should be divisibles from 1 to 1000:- ")
    if value =="":
        break
    else:
        divisibles.append(int(value))
print("divisibles are:-", divisibles)

divisibles_are = random_generator(count, divisibles)
print(divisibles_are)