import math


class Course_activities:
    def __init__(self, number_of_students):
        self.number_of_students = number_of_students

class Rooms:
    def __init__(self, room_number, max_capacity):
        self.room_number = room_number
        self.max_capacity = max_capacity

    def under_max_capacity(self, number_of_students):
        if number_of_students <= self.max_capacity:
            return True
        else:
            return False

class Lecture:
    def __init__(self, course):
        self.course = course

class Student:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

class Course:
    def __init__(self, number_of_lectures, number_of_tutorials, number_of_practical, total_students, max_tutorial, max_practical):
        self.number_of_lectures = number_of_lectures
        self.number_of_tutorials = number_of_tutorials
        self.number_of_practical = number_of_practical
        self.total_students = total_students
        self.max_tutorial = max_tutorial
        self.max_practical = max_practical

        number_of_tutorials = math.ceil(total_students / max_tutorial)
