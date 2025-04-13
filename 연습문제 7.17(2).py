population_A = (100, 150, 230, 120, 180, 100, 140, 95, 81, 21, 4)
population_B = (300, 420, 530, 420, 400, 300, 40, 5, 1, 1, 1)

old_A = sum(population_A[7:11])
old_B = sum(population_B[7:11])

total_A = sum(population_A)
total_B = sum(population_B)

aging_A = old_A / total_A
aging_B = old_B / total_B

print(f"마을 A와 B의 고령화 정도는 각각 {aging_A:.3f}와 {aging_B:.3f}입니다.")
