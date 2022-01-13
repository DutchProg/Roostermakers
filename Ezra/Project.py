import math
import pandas as pd
import csv
import numpy as np

file = open("Courses.csv")
csvreader = csv.reader(file)
courses_dataframe = pd.read_csv(r'Courses.csv')



# for index,row in courses_dataframe.iterrows():
#     print(row)

Data_test = pd.DataFrame(
    {
            "Day": ("Monday 9-11","Monday 11-13","Monday 13-15","Monday 15-17","Monday 17-19","Tueseday 9-11","Tueseday 11-13","Tueseday 13-15","Tueseday 15-17","Tueseday 17-19","Wednesday 9-11","Wednesday 11-13","Wednesday 13-15","Wednesday 15-17","Wednesday 17-19","Thursday 9-11","Thursday 11-13","Thursday 13-15","Thursday 15-17","Thursday 17-19","Friday 9-11","Friday 11-13","Friday 13-15","Friday 15-17","Friday 17-19"),
            "Course": 1,
            "Class_room": 1,
            "Student_count": 1,
            "List_of_students": 1,
            
           


        }
)
print(Data_test)


class Course_activities:
    def __init__(self, course_name, number_of_students):
        self.number_of_students = number_of_students

class Course:
    def __init__(self, number_of_lectures, number_of_tutorials, number_of_practical, total_students, max_tutorial, max_practical):
        self.number_of_lectures = number_of_lectures
        self.number_of_tutorials = number_of_tutorials
        self.number_of_practical = number_of_practical
        self.total_students = total_students
        self.max_tutorial = max_tutorial
        self.max_practical = max_practical

        number_of_tutorials = math.ceil(total_students / max_tutorial)


    






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
