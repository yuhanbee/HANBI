import math
n = int(input("n을 입력하세요: "))
nums = list(map(int, input(f"{n}개의 수를 입력하세요: ").split()))
total = sum(nums)
mean = total / n
s = 0
for x in nums:
    s += (x - mean) ** 2
std = math.sqrt(s / n)
print("합 :", total)
print("평균 :", round(mean, 1))
print("표준편차 :", round(std, 2))
