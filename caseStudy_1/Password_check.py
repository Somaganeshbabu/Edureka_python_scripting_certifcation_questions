import re
def check_password(password):
    if len(password)<6:
        return "password should be min of 6 chars"
    elif len(password)>12:
        return " password should be max of 12 char"
    if not re.search('[a-z]', password):
        return "password should have at least 1 letter between [a-z]"
    if not re.search('[A-Z]', password):
        return "password should have at least 1 letter between [A-Z]"
    if not re.search('[0-9]', password):
        return "password should have at least 1 number between [0-9]"
    if not re.search('[$#@]', password):
        return "password should have at least 1 character from [$#@]"
    return "password is valid"

password = input("enter password :- ")
result = check_password(password)
print(result)