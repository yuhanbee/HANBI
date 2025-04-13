s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'
def modify_string(s):
    modified_s = s.replace(' ', '').replace('-', '').upper()
    return modified_s
s1_modified = modify_string(s1)
s2_modified = modify_string(s2)
s3_modified = modify_string(s3)
s4_modified = modify_string(s4)
def count_n(modified_s):
    return modified_s.count('N')
print("s1 =", s1)
print("s2 =", s2)
print("s3 =", s3)
print("s4 =", s4)
print(f"{s1} 은(는) {s1_modified} 으로 수정됨")
print(f"{s2} 은(는) {s2_modified} 으로 수정됨")
print(f"{s3} 은(는) {s3_modified} 으로 수정됨")
print(f"{s4} 은(는) {s4_modified} 으로 수정됨")
print(f"{s1_modified} : {count_n(s1_modified)} 개의 N이 나타남")
print(f"{s2_modified} : {count_n(s2_modified)} 개의 N이 나타남")
print(f"{s3_modified} : {count_n(s3_modified)} 개의 N이 나타남")
print(f"{s4_modified} : {count_n(s4_modified)} 개의 N이 나타남")
