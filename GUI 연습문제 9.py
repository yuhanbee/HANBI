import tkinter as tk #tkinter 모듈을 tk라는 이름으로 불러옴

def save_file(): # Save 버튼 클릭 시 호출되는 함수
    with open("note.txt", "w") as f:
        f.write(text.get("1.0", tk.END))

root = tk.Tk() #루트 윈도우 생성
text = tk.Text(root)
text.pack() #창에 배치
button = tk.Button(root, text="Save", command=save_file) #Save 버튼 생성
button.pack() #버튼 배치
root.mainloop() #이벤트 루프 시작
