n = int(input("숫자를 입력하세요: "))
total = 0
for i in range(1, n+1):
    total = total + i ** 2
print("결과는", total, "입니다.")
