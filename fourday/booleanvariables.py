is_raining = True
is_sunny = False


print(bool(0))         # False
print(bool(1))         # True
print(bool('hello'))   # True
print(bool(''))        # False



print(True and False)  # False
print(True and True)   # True
print(False or True)   # True
print(False or False)  # False
print(not True)        # False
print(not False)       # True


a = 10
b = 20
greater = a > b      # False
smaller = a < b      # True
equal = 10 == 10     # True
print(greater, smaller, equal)