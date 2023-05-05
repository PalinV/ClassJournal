class Student:
    list_students = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.list_students.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
    
    def rate_lecturer(self, lecturer, course, grades_lecturer):
        if course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grades_lecturer]
            else:
                lecturer.grades_lecturer[course] = [grades_lecturer]
        else:
            return 'Ошибка'  
    
    def _average_grade(self, grades):
        final_middle_grade = 0
        for i, subject in enumerate(grades.values()):
            count_value = len(subject)
            middle_grade_course  = sum(subject) / count_value  
            final_middle_grade += middle_grade_course
        return round(final_middle_grade / (i + 1), 1)  
    
    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grade(self.grades)}\
               \nКурсы в процессе изучения: {", " .join(self.courses_in_progress)} \nЗавершенные курсы: {"," .join(self.finished_courses)}')
        return res
    
    def __lt__(other, another):
         return other._average_grade(other.grades) < another._average_grade(another.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):    
    list_lecturer = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}
        Lecturer.list_lecturer.append(self)

    def _average_grade(self, grades_lecturer):
        final_middle_grade = 0
        for i, subject in enumerate(grades_lecturer.values()):
            count_value = len(subject)
            middle_grade  = sum(subject) / count_value  
            final_middle_grade += middle_grade
        return round(final_middle_grade / (i + 1), 1)  

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade(self.grades_lecturer)}')
        return res
    
    def __lt__(other, another):
        return other._average_grade(other.grades_lecturer) < another._average_grade(another.grades_lecturer)

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
        res = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return res

def average_rating_student(*list_students, course):
    list_res = [sum(student.grades[course]) / len(student.grades[course]) for student in list_students if course in student.grades]
    res = sum(list_res) / len(list_res)
    print(f'Средняя оценка студентов на курсе {course} - {round(res, 1)}')

def average_rating_lecterer(*list_lecturer, course):
    list_res = [sum(lecturer.grades_lecturer[course]) / len(lecturer.grades_lecturer[course]) for lecturer in list_lecturer if course in lecturer.grades_lecturer] 
    res = sum(list_res) / len(list_res)
    print(f'Средняя оценка лекторов на курсе {course} - {round(res, 1)}')

cool_lecturer = Lecturer('Thomas', 'Harris')  
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['GIT']

some_lecturer = Lecturer('Hannibal', 'Lecter')    
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['GIT']

best_student = Student('Clarice', 'Starling', 'male')  
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']
best_student.finished_courses += ['Введение в программирование']
best_student.rate_lecturer(cool_lecturer,'Python', 10)
best_student.rate_lecturer(cool_lecturer,'Python', 10)
best_student.rate_lecturer(cool_lecturer,'Python', 10)
best_student.rate_lecturer(some_lecturer,'GIT', 9)
best_student.rate_lecturer(some_lecturer,'GIT', 9)
best_student.rate_lecturer(some_lecturer,'GIT', 10)

some_student = Student('Buffalo', 'Bill', 'female')
some_student.courses_in_progress += ['Python']
some_student.finished_courses += ['Снятие кожи']
some_student.rate_lecturer(some_lecturer,'Python', 6)
some_student.rate_lecturer(some_lecturer,'Python', 9)
some_student.rate_lecturer(some_lecturer,'Python', 7)

cool_reviewer = Reviewer('Jack', 'Crawford')  
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(some_student, 'Python', 7)
cool_reviewer.rate_hw(some_student, 'Python', 6)
cool_reviewer.rate_hw(some_student, 'Python', 5)

some_reviewer = Reviewer('Jonathan', 'Demme')  
some_reviewer.courses_attached += ['GIT']
some_reviewer.rate_hw(best_student, 'GIT', 9)
some_reviewer.rate_hw(best_student, 'GIT', 9)
some_reviewer.rate_hw(best_student, 'GIT', 9)

print(cool_reviewer) 
print()
print(cool_lecturer)
print()
print(some_lecturer)
print()
print(best_student)
print()
print(some_student)
print()
print(best_student < some_student)
print()
print(cool_lecturer < some_lecturer)
print()
average_rating_student(*Student.list_students, course='Python')
print()
average_rating_lecterer(*Lecturer.list_lecturer, course='GIT')