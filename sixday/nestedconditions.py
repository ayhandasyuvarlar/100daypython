x = 10
y = 5

if x > y:
    print('x is greater than y')
    if x > 10:
        print('x is also greater than 10')

a = 1
b = 2
c = 'hello'
d = 30
k = '80'

if a > 1:
    if b < 20:
        if c == 'hello':
            if d == 30:
                print('Hello')
            else:
                if k == '80':
                    print('k is 80')
                if a > 20:
                    print('World')
                else:
                    print('!!')

name = 'Bob'
age = 30
homework_is_done = True

if name == 'Bob':
    print('Hey Bob!')
else:
    if name == 'Alice':
        print('How are you doing Alice?')
    else:
        if name == 'Anna':
            print('Hello, Anna!!!')
        else:
            if name == 'Martin':
                print('Hi, Martin')
            else:
                print('Wait! I don\'t not know you right?')
                # We can have some more nesting here...

if name == 'Bob':
    print('Hey Bob!')
elif name == 'Alice':
    print('How are you doing Alice?')
elif name == 'Anna':
    print('Hello, Anna!!!')
elif name == 'Martin':
    print('Hi, Martin')
else:
    print('Wait! I don\'t not know you right?')


if name == 'Bob':
    if age >= 18:
        print('Welcome')
    else:
        print('You are not allowed')
elif name == 'Anna':
    if age >= 18 and homework_is_done:
        print('Welcome')
    else:
        print('Sorry, not allowed')
else:
    print('I\'m not sure if I know you...')
