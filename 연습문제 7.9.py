tup = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 3, 7, 3)
unique_tup = tuple(sorted(set(tup)))
print(f"주어진 튜플: {tup}")
print(f"중복 제거 튜플: {unique_tup}")
