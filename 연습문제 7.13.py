my_list = [5, 6, 3, 9, 12, 3, 8, 7]
print("주어진 리스트는 =", my_list)
for i in range(len(my_list)):
    for j in range(0, len(my_list)-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
print("정렬된 결과는 =", my_list)
