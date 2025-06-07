import tkinter as tk #tkinter 모듈을 tk라는 이름으로 불러옴

def greet(): #버튼 클릭 시 실행될 함수 정의
    name = entry.get()
    label.config(text=f"Hello, {name}!")

root = tk.Tk()#tkinter의 루트 윈도우 생성
entry = tk.Entry(root)
entry.pack() #입력창을 윈도우에 배치
button = tk.Button(root, text="Greet", command=greet) #Greet라는 텍스트가 있는 버튼 생성
button.pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()
