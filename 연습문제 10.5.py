#연습문제 10.5
a = 1
b = 1
c = 2
d = 3
e = 3

lst = [a, b, c, d, e]

for i in range(1, 11):
    count = 0
    for var in lst:
        if var is i:
            count += 1
    print(f"{i} : {count}개")
