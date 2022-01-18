import math

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

class Student:
    def __init__(self, name, student_id, courses):
        self.name = name
        self.student_id = student_id
        courses = []
        """ read through csv and append list of all subjects p/ student"""
        self.courses = courses

