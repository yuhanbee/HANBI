depth = 30
position = 0
day = 0
while True:
    day += 1
    position += 7
    print("day:", day, "달팽이의 위치 :", position, "미터")
    if position >= depth:
        break
    position -= 5
print("우물을 탈출하는 데 걸린 날은", day, "일입니다.")
