import tkinter as tk #tkinder 모듈을 tk라는 이름으로 불러옴

def change_color(): #버튼 선택 시 실행되는 함수
    root.configure(bg=color.get()) #현재 선택된 색상 문자열을 가져와서 창의 배경색으로 설정

root = tk.Tk() #루트 윈도우 생성
color = tk.StringVar()
tk.Radiobutton(root, text="Red", variable=color, value="red", command=change_color).pack() #Red 선택 시 color 값이 red가 되고 change color 함수 실행
tk.Radiobutton(root, text="Blue", variable=color, value="blue", command=change_color).pack() #Blue 선택 시 color 값이 blue가 되고 change color 함수 실행
tk.Radiobutton(root, text="Green", variable=color, value="green", command=change_color).pack() #Green color 값이 Green가 되고 change color 함수 실행
root.mainloop() #이벤트 루프 시작
