import tkinter as tk
#tkinter 모듈을 tk라는 이름으로 불러옴
def say_hello(): #버튼 클릭시 실행될 함수 정의
    label.config(text="Hello, World!") #label의 텍스트를 "Hello, World!"로 바꿈

root = tk.Tk() #tkinter의 기본 윈도우 생성
button = tk.Button(root, text="Click Me", command=say_hello) #root 윈도우에 속한 버튼 위젯 생성, 버튼에는 'Click Me'라고 써져 있게 함 
button.pack() #버튼을 윈도우에 배치
label = tk.Label(root, text="")
label.pack()
root.mainloop() #이벤트 루프 시작
