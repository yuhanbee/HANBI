def how_many_persons(person_list):
    return len(person_list) // 5

def compute_average_age(person_list):
    total_age = 0
    n = len(person_list) // 5
    for i in range(n):
        total_age += person_list[i * 5 + 1]
    return total_age / n

def count_males_females(person_list):
    n = len(person_list) // 5
    male = 0
    female = 0
    for i in range(n):
        gender = person_list[i * 5 + 2]
        if gender == 1:
            male += 1
        else:
            female += 1
    return male, female

def display_persons(person_list):
    n = len(person_list) // 5
    for i in range(n):
        person = person_list[i * 5 : i * 5 + 5]
        print(person)

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['험거세', 40, 1, 150.0, 50.0]

person_list = person1 + person2 + person3 + person4

# (1)
n_persons = how_many_persons(person_list)
print(str(n_persons) + '명의 정보가 담겨 있습니다.')

# (2)
average_age = compute_average_age(person_list)
print('평균 나이는 ' + str(average_age) + '세입니다.')

# (3)
n_male, n_female = count_males_females(person_list)
print('리스트에는 남자가', n_male, '명, 여자가', n_female, '명입니다.')

# (4)
display_persons(person_list)
