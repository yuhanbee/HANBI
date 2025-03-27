n = int(input("숫자를 입력하세요: "))
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print(n, "는 소수입니다.")
else:
    print(n, "는 소수가 아닙니다.")

