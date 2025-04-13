price = {'김밥': 5000, '어묵': 3000, '떡볶이': 2000}
print(price['김밥'])
price['김밥'] = 6000
print(price)
print(price.values())
print(price.keys())
print(f"이 식당의 메뉴 개수는 {len(price)} 개 입니다.")
