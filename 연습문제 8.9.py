import random
def guess_game():
    x = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("1~20까지의 숫자를 입력하세요: "))
        attempts += 1
        if guess < x:
            print("보다 큽니다!")
        elif guess > x:
            print("보다 작습니다!")
        else:
            print("정답입니다!")
            print(f"{attempts}번만에 맞추셨네요. 잘했어요^^")
            break
guess_game()
