import tkinter as tk #tkinter 모듈을 tk라는 이름으로 불러옴

def show_selection(): #버튼 클릭 시 실행되는 함수 정의
    selections = []
    if var1.get(): selections.append("Option 1")
    if var2.get(): selections.append("Option 2")
    label.config(text=", ".join(selections))

root = tk.Tk()
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
tk.Checkbutton(root, text="Option 1", variable=var1).pack() #Option 1이라는 체크박스를 만들고, var1에 상태를 저장
tk.Checkbutton(root, text="Option 2", variable=var2).pack() #Option 2라는 체크박스를 만들고, var2에 상태를 저장
tk.Button(root, text="Show", command=show_selection).pack() 
label = tk.Label(root, text="")
label.pack()
root.mainloop() #이벤트 루프 시작
