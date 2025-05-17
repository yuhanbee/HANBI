#연습문제 10.9
class Counter:
    def __init__(self, number):
        self.__number = number

    def __add__(self, other):
        result = self.__number + other.__number
        if result >= 100:
            result = 0
        return Counter(result)

    def __sub__(self, other):
        result = self.__number - other.__number
        return Counter(result)

    def __str__(self):
        return f"C({self.__number})"


