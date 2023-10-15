class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        sum_value = 0
        amount = 0
        for grade in self.grades.values():
            amount += len(grade)
            for i in grade:
                sum_value += i
        if sum_value:
            return round(sum_value / amount, 1)
        else:
            return 'Значений нет'
        
    def __lt__(self, other):
        if self.average_grades() < other.average_grades():
            return f"Лектор {other.name} показал лучший результат, чем лектор {self.name}"
        else:
            return f"Лектор {self.name} показал лучший результат, чем лектор {other.name}"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades()}\n"
        
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
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"

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

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def average_grades(self):
        sum_value = 0
        amount = 0
        for grade in self.grades.values():
            amount += len(grade)
            for i in grade:
                sum_value += i
        if sum_value:
            return round(sum_value / amount, 1)
        else:
            return 'Значений нет'
        

    def __lt__(self, other):
        if self.average_grades() < other.average_grades():
            return f"Студент {other.name} учится лучше студента {self.name}"
        else:
            return f"Студент {self.name} учится лучше студента {other.name}"        

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grades()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}\n"

# Экземпляры классов
student_1 = Student('Mary', 'Xmas', 'F')
student_1.courses_in_progress += ['Python', 'Java']
student_1.finished_courses += ['Git', 'OOP']

student_2 = Student('Leo', 'Nardeu', 'M')
student_2.courses_in_progress += ['Python', 'C']
student_2.finished_courses += ['Git', 'Вводный модуль']
 
lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python', 'Java']

lecturer_2 = Lecturer('Any', 'Body')
lecturer_2.courses_attached += ['C']

reviewer_1 = Reviewer('My', 'Pleasure')
reviewer_1.courses_attached += ['Java', 'Python']

reviewer_2 = Reviewer('Hello', 'World')
reviewer_2.courses_attached += ['Java', 'C']

# Методы
student_1.rate_lecture(lecturer_1, 'Python', 8)
student_1.rate_lecture(lecturer_1, 'Java', 9)

student_2.rate_lecture(lecturer_1, 'Python', 5)
student_2.rate_lecture(lecturer_2, 'C', 7)
student_2.rate_lecture(lecturer_2, 'C', 4)
 
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Java', 5)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 9)

reviewer_2.rate_hw(student_1, 'Java', 10)
reviewer_2.rate_hw(student_2, 'C', 8)
reviewer_2.rate_hw(student_2, 'C', 5)

# Проверки вызванных методов
print(student_1, student_2)
print(student_1 < student_2)

print(lecturer_1, lecturer_2)
print(lecturer_1 < lecturer_2)

print(reviewer_1, reviewer_2)

# Задание 4
all_students = [student_1, student_2]
all_lecturers = [lecturer_1, lecturer_2]

def grades_for_course(course, all_students):
    sum_value = []
    amount = 0
    for student in all_students:
        if course in student.courses_in_progress:
            amount += len(student.grades[course])
            sum_value += student.grades[course]
    if sum_value:
        return round(sum(sum_value) / amount, 1)
    else:
        return 'Значений нет'
    
def grades_for_mentors(course, all_lecturers):
    sum_value = []
    amount = 0
    for lecturers in all_lecturers:
        if course in lecturers.courses_attached:
            amount += len(lecturers.grades[course])
            sum_value += lecturers.grades[course]
    if sum_value:
        return round(sum(sum_value) / amount, 1)
    else:
        return 'Значений нет'

# Все проверки для задания 4

print(grades_for_course('Java', all_students))
# print(grades_for_course('C', all_students))
# print(grades_for_course('Python', all_students))

print(grades_for_mentors('Java', all_lecturers))
# print(grades_for_mentors('C', all_lecturers))
# print(grades_for_mentors('Python', all_lecturers))