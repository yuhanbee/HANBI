def divisor(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total
for a in range(1, 20001):
    b = divisor(a)
    if b > a and b <= 20000:
        if divisor(b) == a:
            print(f"{a}의 친화수 {b}")
            print(f"{b}의 친화수 {a}")
