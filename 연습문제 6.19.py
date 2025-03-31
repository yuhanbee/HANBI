s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []
for item in s_list:
    if item not in new_s_list:
        new_s_list.append(item)
print("s_list =", s_list, "new_s_list =", new_s_list)
