class GradeBook:

    def __init__(self, course_name = None, grades = None):
        self.__course_name = course_name
        self.__grades = []

    def set_name(self, name):
        self.__course_name

    def get_name(self):
        return self.__course_name

    def add(self, num):
        self.__grades.append(num)
        return self.__grades

    def get_minimum(self):
        low_grade = self.__grades[0]
        for index in range(0, len(self.__grades)):
            if self.__grades[index] < low_grade:
                low_grade = self.__grades

        return low_grade

    def get_maximum(self, numbers=list):
        highest_grade = numbers[0]
        for index in range( len(numbers)):
            if numbers[index] > highest_grade:
                highest_grade = numbers

        return highest_grade


    def get_average(self,num=list):
        total = 0
        for index in range(0,len(num)):
            total += index

        return total


