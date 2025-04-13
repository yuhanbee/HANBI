print("사전 프로그램 시작... 종료는 q를 입력")
dictionary = {}

while True:
    command = input("$ ").strip()
    
    if command == "q":
        break
    
  
    elif command.startswith("<"):
        content = command[1:].strip()
        if ":" in content:
            eng, kor = content.split(":", 1)
            dictionary[eng.strip()] = kor.strip()
        else:
            print("입력오류가 발생했습니다.")
    
    elif command.startswith(">"):
        search_word = command[1:].strip()
        if search_word in dictionary:
            print(dictionary[search_word])
        else:
            print(f"{search_word}가 사전에 없습니다.")
    
    else:
        print("입력오류가 발생했습니다.")

print("사전 프로그램을 종료합니다.")
