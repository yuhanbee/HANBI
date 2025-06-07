import tkinter as tk #tkinter 모듈을 tk라는 이름으로 불러옴

def show_message(msg):
    label.config(text=msg) #라벨의 텍스트를 msg로 설정

root = tk.Tk() #루트 윈도우 생성
menu = tk.Menu(root) #메뉴바 객체 생성
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Open", command=lambda: show_message("Open clicked"))
menu.add_cascade(label="File", menu=file_menu)
help_menu = tk.Menu(menu, tearoff=0)
help_menu.add_command(label="About", command=lambda: show_message("About clicked"))
menu.add_cascade(label="Help", menu=help_menu)
root.config(menu=menu)
label = tk.Label(root, text="") #결과 메시지를 표시할 라벨 생성
label.pack() #라벨을 창에 배치
root.mainloop() #이벤트 루프 실행
