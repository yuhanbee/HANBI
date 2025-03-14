n = int(input("세 자리 정수를 입력하세요: "))
hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10
print(f"백의 자리 : {hundreds}")
print(f"십의 자리 : {tens}")
print(f"일의 자리 : {ones}")
