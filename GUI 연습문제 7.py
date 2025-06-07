import tkinter as tk #tkinter 모듈을 tk라는 이름으로 불러옴

def show_fruit(event):
    selection = listbox.get(listbox.curselection())
    label.config(text=f"Selected: {selection}") #선택된 항목을 라벨에 표시

root = tk.Tk() #루트 윈도우 생성
listbox = tk.Listbox(root)
for fruit in ["Apple", "Banana", "Cherry"]:
    listbox.insert(tk.END, fruit)
listbox.pack() #리스트박스를 창에 배치
listbox.bind("<<ListboxSelect>>", show_fruit)
label = tk.Label(root, text="")
label.pack() #라벨을 창에 배치
root.mainloop() #이벤트 루프 시작
