n_list = [10, 20, 30, 50, 60]
print("리스트 원소들 :", n_list)
max_value = n_list[0]
for num in n_list:
    if num > max_value:
        max_value = num
print("리스트 원소들 중 최댓값 :", max_value)
