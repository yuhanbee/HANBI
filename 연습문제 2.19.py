n = int(input("정수를 입력하세요: "))
is_valid_even = (0 <= n <= 100) and (n % 2 == 0)
print(f"입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? {is_valid_even}")
