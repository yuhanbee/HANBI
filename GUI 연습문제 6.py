import tkinter as tk #tkinter 모듈을 tk라는 이름으로 불러옴

def resize(val): #슬라이더를 움직일 때 호출되는 함수
    label.config(font=("Arial", int(val))) #val은 슬라이더 현재 값(문자열), 이를 정수를 바꿔서 글꼴 크기로 설정

root = tk.Tk() #루트 윈도우 생성
scale = tk.Scale(root, from_=10, to=40, orient="horizontal", command=resize) #10부터 40까지 값이 있는 가로 방향 슬라이더 생성. 움직이면 resize 함수 실행
scale.pack()
label = tk.Label(root, text="Resizable Text") #폰트 크기를 조절할 텍스트 라벨 생성
label.pack()
root.mainloop() #이벤트 루프 시작
