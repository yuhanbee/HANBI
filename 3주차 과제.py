a, b = 1,1

for i in range(101):
    b = a + b
    a = b - a

    print('{}th Fib. Number is {}'.format(i+2, b))
