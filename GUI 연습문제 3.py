import tkinter as tk #tkinter 모듈을 tk라는 이름으로 불러옴

def add(): #버튼 클릭 시 실행되는 함수 정의
    result = int(entry1.get()) + int(entry2.get())
    label.config(text=f"Result: {result}")

root = tk.Tk() #루트 윈도우 생성
entry1 = tk.Entry(root) #첫 번째 숫자를 입력받을 입력창 생성
entry1.pack()
entry2 = tk.Entry(root) #두 번째 숫자를 입력받을 입력창 생성
entry2.pack()
button = tk.Button(root, text="Add", command=add)
button.pack()
label = tk.Label(root, text="")
label.pack() #라벨을 창에 배치
root.mainloop() #이벤트 루프 실행

