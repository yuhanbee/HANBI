from datetime import datetime
start_date = datetime(2019, 2, 14)
today = datetime.today()
days_passed = (today - start_date).days
print(f"춘향이와 몽룡이의 연애 시작일 : 2019년 2월 14일")
print(f"연애 시작일로부터 경과한 날짜 : {days_passed}일")
