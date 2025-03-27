fuel = 500
while True:
    change = int(input("충전 또는 사용한 연로를 +/- 기호와 함께 입력하세요: "))
    fuel += change
    print("현재 탱크량은", fuel, "입니다.")
    if fuel <= 50:
        print("경고: 연료가 10% 미만이니 충전하세요!")
        break
