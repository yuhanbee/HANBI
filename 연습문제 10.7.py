#연습문제 10.7
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"이름은 {self.name}이고 나이는 {self.age}살입니다."

cute_dog = Dog("Mango", 3)
print(cute_dog)
