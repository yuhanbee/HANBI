#연습문제 10.11
class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__korean_quiz = 0
        self.__math_quiz = 0
        self.__science_quiz = 0
        self.__total_score = 0

    def __str__(self):
        avg = self.get_avg_score()
        return (f"이름 : {self.__name}, 학번 : {self.__student_id}\n"
                f"국어 성적 : {self.__korean_quiz}, 수학 성적 : {self.__math_quiz}, "
                f"과학 성적 : {self.__science_quiz} 합계 : {self.__total_score}, 평균 : {avg:.1f}")

    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id

    def get_korean_quiz(self):
        return self.__korean_quiz

    def get_math_quiz(self):
        return self.__math_quiz

    def get_science_quiz(self):
        return self.__science_quiz

    def set_korean_quiz(self, score):
        self.__korean_quiz = score
        self.__update_total_score()

    def set_math_quiz(self, score):
        self.__math_quiz = score
        self.__update_total_score()

    def set_science_quiz(self, score):
        self.__science_quiz = score
        self.__update_total_score()

    def get_total_score(self):
        return self.__total_score

    def get_avg_score(self):
        return self.__total_score / 3

    def __update_total_score(self):
        self.__total_score = (
            self.__korean_quiz + self.__math_quiz + self.__science_quiz
        )
