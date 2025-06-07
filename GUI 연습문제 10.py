import tkinter as tk #tkinter 모듈을 tk라는 이름으로 가져
import time옴 #현재 시간을 가져오기 위한 time 모듈 import

def update_time(): #현재 시간을 가져와 라벨에 표시하고 1초마다 반복하는 함수
    current = time.strftime("%H:%M:%S") #현재 시간을 "시:분:초" 형식으로 문자열로 가져옴
    label.config(text=current) #라벨의 텍스트를 현재 시간으로 설정
    root.after(1000, update_time) #1000밀리초(1초) 후에 다시 update_time() 호출

root = tk.Tk() #루트 윈도우 생성
label = tk.Label(root, font=("Arial", 24)) #시계를 보여줄 라벨 생성, 글꼴은 Arial, 크기 24
label.pack() #라벨을 창에 배치
update_time() #프로그램 시작 시 바로 시간 표시 시작
root.mainloop() #이벤트 루프 시작
