import math
a = int(input("밑변을 입력하세요: "))
b = int(input("높이를 입력하세요: "))

c = math.sqrt(a**2 + b**2)
print(f"빗변: {c:.1f}")
