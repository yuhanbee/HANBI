s = input("문자열을 입력하시오: ")
filtered = "".join(ch.lower() for ch in s if ch.isalpha())
if filtered == filtered[::-1]:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")
