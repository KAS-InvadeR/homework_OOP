
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_le(self, lecture, course, grade_le):
        if isinstance(lecture, Lecture) and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades_le:
                lecture.grades_le[course] += [grade_le]
            else:
                lecture.grades_le[course] = [grade_le]
        else:
            return 'Ошибка'

    def average_st(self):
        if len(self.grades) != 0:
            average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
            return average
        else:
            return 'Нет оценок'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return print('Нет такого студента')
        return self.average_st() < other.average_st()


    def __str__(self):
        some_lecturer = f'Имя: {self.name.title()}\nФамилия: {self.surname.title()}' \
                        f'\nСредняя оценка за домашние задания: {self.average_st()}' \
                        f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
                        f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return some_lecturer



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_le = {}


class Lecture(Mentor):
    def average_le(self):
        if len(self.grades_le) != 0:
            average = round(sum(sum(self.grades_le.values(), [])) / len(sum(self.grades_le.values(), [])), 1)
            return average
        else:
            return 'Нет оценок'

    def __lt__(self, other):
        if not isinstance(other, Lecture):
            return print('Нет такого лектора')
        return self.average_le() < other.average_le()

    def __str__(self):
        some_lecturer = f'Имя: {self.name.title()}\nФамилия: {self.surname.title()}' \
                        f'\nСредняя оценка за лекции: {self.average_le()}'
        return some_lecturer


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Имя: {self.name.title()}\nФамилия: {self.surname.title()}'
        return some_reviewer


def averages_st(students, courses):
    student_grade = []
    for student in students:
        for cours, grade_s in student.grades.items():
            if courses == cours:
                student_grade += grade_s
    averag = round(sum(student_grade)/len(student_grade), 1)
    return f'Cредня оценка у студентов по курсу {courses}: {averag}'

def averages_le(lectors, courses):
    lector_grade = []
    for lector in lectors:
        for cours, grade_l in lector.grades_le.items():
            if courses == cours:
                lector_grade += grade_l
    averag = round(sum(lector_grade)/len(lector_grade), 1)
    return f'Средняя оценка у лекторв по курсу {courses} {averag}'

lector_1 = Lecture('Anna', 'Volkova')
lector_2 = Lecture('Dima', 'Volkov')

reviewer_1 = Reviewer('Olya', 'Portikova')
reviewer_2 = Reviewer('Oleg', 'Portikov')

student_1 = Student('Masha', 'Ivanova', 'g')
student_2 = Student('Sasha', 'Ivanov', 'm')

lector_1.courses_attached += ['java']
lector_1.courses_attached += ['C++']
lector_1.courses_attached += ['pythone']
lector_2.courses_attached += ['java']
lector_2.courses_attached += ['C++']
lector_2.courses_attached += ['pythone']
reviewer_1.courses_attached += ['java']
reviewer_1.courses_attached += ['C++']
reviewer_1.courses_attached += ['pythone']

student_1.courses_in_progress += ['C++']
student_1.courses_in_progress += ['java']
student_1.courses_in_progress += ['pythone']
student_1.add_courses('html')
student_2.courses_in_progress += ['pythone']
student_2.courses_in_progress += ['C++']
student_2.courses_in_progress += ['java']

# Выставление оценок лекторам от студентов
student_1.rate_le(lector_1, 'java', 10)
student_1.rate_le(lector_1, 'C++', 6)
student_2.rate_le(lector_1, 'java', 5)
student_2.rate_le(lector_1, 'java', 8)
student_2.rate_le(lector_1, 'pythone', 1)
student_1.rate_le(lector_2, 'java', 10)
student_1.rate_le(lector_2, 'C++', 5)
student_2.rate_le(lector_2, 'java', 4)
student_2.rate_le(lector_2, 'java', 7)
student_2.rate_le(lector_2, 'pythone', 2)

# Выставление оценок студентам
reviewer_1.rate_hw(student_1, 'java', 5)
reviewer_1.rate_hw(student_1, 'java', 10)
reviewer_1.rate_hw(student_1, 'pythone', 6)
reviewer_1.rate_hw(student_1, 'pythone', 8)

reviewer_1.rate_hw(student_2, 'java', 4)
reviewer_1.rate_hw(student_2, 'java', 9)
reviewer_1.rate_hw(student_2, 'pythone', 5)
reviewer_1.rate_hw(student_2, 'pythone', 7)
reviewer_1.rate_hw(student_2, 'C++', 5)
reviewer_1.rate_hw(student_2, 'java', 8)
reviewer_1.rate_hw(student_2, 'java', 9)
reviewer_1.rate_hw(student_2, 'C++', 5)

# Задание 3 Перегрузите магический метод
print(reviewer_1)
print(lector_1)
print(student_1)

print(student_1 > student_2)
print(lector_1 < lector_2)



students =[student_1, student_2]
lectors = [lector_1, lector_2]

students_aver = averages_st(students, 'java')
lectors_aver = averages_le(lectors, 'pythone')

print(students_aver)
print(lectors_aver)