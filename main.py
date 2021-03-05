class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = 0

    def rate_lection(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.courses_attached:
                lecturer.mark_for_lection += [grade]
            else:
                lecturer.mark_for_lection = [grade]
        else:
            return "Провал"

    def medial_rate(self):
        all_marks = []
        for marks in self.grades.values():
            all_marks.extend(marks)
        self.avg_grade = sum(all_marks) / len(all_marks)
        return self.avg_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
        return self.avg_grade < other.avg_grade

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за дз: {self.medial_rate()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses} "


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super(Lecturer, self).__init__(name,surname)
        self.avg_mark_for_lection = 0
        self.mark_for_lection = []


    def avg_rate(self):
        self.avg_mark_for_lection = sum(self.mark_for_lection) / len(self.mark_for_lection)
        return self.avg_mark_for_lection

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
        return self.avg_mark_for_lection < other.avg_mark_for_lection

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rate()}"


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
        return f"Имя: {self.name} \nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['WEB']

best_student2 = Student('Boy', '2', 'y')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['WEB']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lecturer = Lecturer('SomeL', 'BuddyL')
cool_lecturer.courses_attached += ['Python']

cool_lecturer2 = Lecturer('SomeL2', 'BuddyL2')
cool_lecturer2.courses_attached += ['WEB']

cool_reviewer = Reviewer('SomeR', 'BuddyR')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['WEB']

cool_reviewer2 = Reviewer('SomeR2', 'BuddyR2')
cool_reviewer2.courses_attached += ['WEB']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'WEB', 9)
cool_reviewer.rate_hw(best_student, 'WEB', 8)
cool_reviewer.rate_hw(best_student, 'WEB', 7)

cool_reviewer2.rate_hw(best_student2, 'WEB', 5)
cool_reviewer2.rate_hw(best_student2, 'WEB', 5)
cool_reviewer2.rate_hw(best_student2, 'WEB', 8)
cool_reviewer.rate_hw(best_student2, 'Python', 5)
cool_reviewer.rate_hw(best_student2, 'Python', 5)
cool_reviewer.rate_hw(best_student2, 'Python', 8)

best_student.rate_lection(cool_lecturer, 'Python', 9)
best_student.rate_lection(cool_lecturer, 'Python', 4)
best_student2.rate_lection(cool_lecturer2, 'WEB', 5)
best_student2.rate_lection(cool_lecturer2, 'WEB', 7)

print(best_student.grades)
print(best_student2.grades)
print(cool_lecturer2.name)
print(cool_lecturer.mark_for_lection)
print(cool_lecturer2.mark_for_lection)
print(cool_lecturer)
print(cool_lecturer2)
print(cool_reviewer)
print(cool_reviewer2)
print(best_student)
print(best_student2)

print(cool_lecturer > cool_lecturer2)
print(cool_lecturer < cool_lecturer2)

print(best_student > best_student2)
print(best_student < best_student2)

def avg_stud_mark(studs, course):
    avg = 0
    avg_res =0
    i = 0
    for student in studs:
        if course in student.courses_in_progress:
            avg = sum(student.grades[course]) / len(student.grades[course])
            avg_res += avg
            i += 1
        else:
            return "не у всех студентов есть этот курс"
    avg_total = avg_res / i
    return avg_total


def avg_lector_mark(lectors, course):
    avg = 0
    i = 0
    for lector in lectors:
        if course in lector.courses_attached:
            i += 1
            avg += lector.avg_mark_for_lection
    return avg / i

stud = {best_student, best_student2}
lect = {cool_lecturer, cool_lecturer2}

print(avg_stud_mark(stud, 'Python'))

print(avg_lector_mark(lect,'WEB'))
