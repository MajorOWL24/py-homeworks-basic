def avg(grades):
    s = 0
    length = 0
    for value in grades.values():
        s = s + sum(value)
        length = length + len(value)
    return round(s / length, 1)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(grade, int) and 0 <= grade <= 10 and isinstance(lecturer, Lecturer) and \
                course in lecturer.courses_attached and course in self.courses_in_progress:
            if course not in lecturer.grades:
                lecturer.grades[course] = []
            lecturer.grades[course].append(grade)

    def __str__(self):
        return "Имя: " + self.name + "\nФамилия: " + self.surname + \
               "\nСредняя оценка за домашние задания: " + str(avg(self.grades)) + \
               "\nКурсы в процессе изучения: " + ", ".join(self.courses_in_progress) + \
               "\nЗавершенные курсы: " + ", ".join(self.finished_courses) + "\n"

    def __eq__(self, other):
        return avg(self.grades) == avg(other.grades)

    def __ne__(self, other):
        return avg(self.grades) != avg(other.grades)

    def __lt__(self, other):
        return avg(self.grades) < avg(other.grades)

    def __le__(self, other):
        return avg(self.grades) <= avg(other.grades)

    def __gt__(self, other):
        return avg(self.grades) > avg(other.grades)

    def __ge__(self, other):
        return avg(self.grades) >= avg(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return "Имя: " + self.name + "\nФамилия: " + self.surname + "\n"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return super().__str__() + "Средняя оценка за лекции:" + str(avg(self.grades)) + "\n"

    def __eq__(self, other):
        return avg(self.grades) == avg(other.grades)

    def __ne__(self, other):
        return avg(self.grades) != avg(other.grades)

    def __lt__(self, other):
        return avg(self.grades) < avg(other.grades)

    def __le__(self, other):
        return avg(self.grades) <= avg(other.grades)

    def __gt__(self, other):
        return avg(self.grades) > avg(other.grades)

    def __ge__(self, other):
        return avg(self.grades) >= avg(other.grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def students_course_rate(students, course):
    grades = []
    for student in students:
        if course in student.grades:
            grades += student.grades[course]
    return avg({'grades': grades})


def lecturers_course_rate(lecturers, course):
    grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades += lecturer.grades[course]
    return avg({'grades': grades})


student1 = Student('Alex', 'Smith', 'Male')
student1.courses_in_progress = ['Python', 'C']

student2 = Student('Mary', 'Jane', 'Female')
student2.courses_in_progress = ['Python']

lecturer1 = Lecturer('James', 'White')
lecturer1.courses_attached = ['Python']

lecturer2 = Lecturer('Adam', 'Black')
lecturer2.courses_attached = ['Python', 'C']

reviewer1 = Reviewer('John', 'Weak')
reviewer1.courses_attached = ['Python']
reviewer2 = Reviewer('Shon', 'Strong')
reviewer2.courses_attached = ['C']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student1, 'C', 9)
reviewer2.rate_hw(student1, 'C', 8)

student1.rate_lecturer(lecturer1, 'Python', 7)
student1.rate_lecturer(lecturer2, 'Python', 9)
student1.rate_lecturer(lecturer2, 'C', 10)
student2.rate_lecturer(lecturer1, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Python', 10)

student_rate_python = students_course_rate([student1, student2], 'Python')
student_rate_c = students_course_rate([student1], 'C')
lecturer_rate_python = lecturers_course_rate([lecturer1, lecturer2], 'Python')
lecturer_rate_c = lecturers_course_rate([lecturer2], 'C')

print('Средняя оценка студентов по курсу Python: ' + str(student_rate_python))
print('Средняя оценка студентов по курсу C: ' + str(student_rate_c))
print('Средняя оценка лекторов по курсу Python: ' + str(lecturer_rate_python))
print('Средняя оценка лекторов по курсу C: ' + str(lecturer_rate_c))
