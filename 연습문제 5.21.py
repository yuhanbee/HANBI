def extract_birthday(id_number):
    birth_date = str(id_number)[:6]
    year = int(birth_date[:2])
    month = int(birth_date[2:4])
    day = int(birth_date[4:])
    if year > 22:
        year += 1900
    else:
        year += 2000
    return f"{year}년 {month}월 {day}일"
id_number = int(input("주민등록번호의 앞 6자리를 입력하세요: "))
print(extract_birthday(id_number))
