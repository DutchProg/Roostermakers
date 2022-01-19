import math
import csv

class Course:
    def __init__(self, name, lectures, tutorials, t_cap, practicals, p_cap, E_students):
        self.name = name
        self.lectures = lectures
        self.tutorials = tutorials
        self.t_cap = t_cap 
        self.practicals = practicals
        self.p_cap = p_cap
        self.E_students = E_students

    def total_classes(self, number_t, number_p, total_c):
        self.number_t = math.ceil(self.E_students/self.t_cap)
        self.number_p = math.ceil(self.E_students/self.p_cap)
        self.total_c = self.lectures + self.number_t + self.number_p

class Room:
    def __init__(self, room_number, max_cap):
        self.room_number = room_number
        self.max_cap = max_cap




students = []

with open('Students.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    
    for element in reader:

        subjects = []
        for item in element[3:]:
            if len(item) != 0:
                subjects.append(item)

        students.append({'name': element[1] + ' ' + element[0], 'student_id': int(element[2]), 'courses': subjects})

print(students)

class Student:
    def __init__(self, name, student_id, courses):
        for student in students:
            for item in student:
                self.name = item[0]
                self.student_id = item[1]
                self.courses = item[2]

