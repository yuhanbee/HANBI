# (1) 
try:
    a, b = input('두 수를 입력하세요 : ').split()
    result = int(a) * int(b)
except ValueError:
    print("입력이 올바르지 않습니다. 두 개의 정수를 입력해주세요.")
else:
    print("결과:", result)

# (2
try:
    a, b = input('두 수를 입력하세요 : ').split()
    result = int(a) * int(b)
except ValueError:
    print("입력이 올바르지 않습니다. 두 개의 정수를 입력해주세요.")
else:
    print("결과:", result)

# (3)
a_list = [200, 300, 400]
print('a_list :', a_list)

try:
    idx = int(input('구하고자 하는 값의 인덱스를 0,1,2 중에서 입력하세요 : '))
    result = a_list[idx]
except ValueError:
    print("정수를 입력해주세요.")
except IndexError:
    print("0, 1, 2 중에서 입력해주세요.")
else:
    print("결과 :", result)

# (4) 
try:
    f_name = input('읽어들일 파일 이름을 입력하세요 : ')
    in_file = open(f_name, 'r')
    buf = in_file.readline()
    print(buf)
    in_file.close()
except FileNotFoundError:
    print("파일이 존재하지 않습니다. 파일 이름을 정확히 입력해주세요.")
else:
    print("파일을 성공적으로 읽었습니다.")
