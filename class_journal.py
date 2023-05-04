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
    
    def rate_lecturer(self, lecturer, course, grades_lecturer):
        if course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lecturer:
                cool_lecturer.grades_lecturer[course] += [grades_lecturer]
            else:
                cool_lecturer.grades_lecturer[course] = [grades_lecturer]
        else:
            return 'Ошибка'  
    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {cool_lecturer._average_grade(self.grades)}\
               \nКурсы в процессе изучения: {"," .join(self.courses_in_progress)}\nЗавершенные курсы: {"," .join(self.finished_courses)}')
        return res
    # def __lt__(self, another):
    #     return self._average_grade(self.grades) < another._average_grade(self.grades)
    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):    
    grades_lecturer = {}
    
    def _average_grade(self, grades_lecturer):
        for subject, j in grades_lecturer.items():
            count_value = len(j)
            middle_grade  = sum(j) / count_value  
            return round(middle_grade, 1)   

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


best_student = Student('Ruoy', 'Eman', 'male')
some_student = Student('James', 'Hetfield', 'male')
best_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
some_lecturer = Lecturer('Bill', 'Murray')
cool_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer,'Python', 10)
best_student.rate_lecturer(cool_lecturer,'Python', 10)
best_student.rate_lecturer(cool_lecturer,'Python', 10)

print(cool_lecturer.grades_lecturer)

some_student.rate_lecturer(some_lecturer,'Python', 4)
some_student.rate_lecturer(some_lecturer,'Python', 4)
some_student.rate_lecturer(some_lecturer,'Python', 4)

print(some_lecturer.grades_lecturer)

cool_reviewer.rate_hw(best_student, 'Python', 2)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 2)
print(cool_lecturer < some_lecturer)
# print(best_student < some_student)
# print(cool_reviewer) 
# print()
# print(cool_lecturer)
# print()
# print(best_student)
