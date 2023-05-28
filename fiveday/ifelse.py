# The start of the program...
condition = '1'
if condition == '1':
    print(condition)

x = 10
if x > 5:
    print('x is greater than 5')
    # code to be executed if the condition is True
# The rest of the program...



x = 10   # Or get x from input with `x = int(input())`

if x > 5:
    print('x is greater than 5')
else:
    print('x is not greater than 5')


x = 5
y = 10
print(x == y)   # False   -> check if x is equal to y
print(x != y)   # True    -> check if x is different from y
print(x > y)    # False   -> check if x is greater than y
print(x < y)    # True    -> check if x is smaller than y
print(x >= y)   # False   -> check if x is greater than or equal to y
print(x <= y)   # True    -> check if x is smaller than or equal to y