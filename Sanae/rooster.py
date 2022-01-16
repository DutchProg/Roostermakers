import csv
import random
import pandas as pd

# room data
rooms_data = {"A1.04": 41, "A1.06": 22, "A1.08": 20, "A1.10": 56, "B0.201": 48, "C0.110": 117, "C1.112": 60}

# day and time data
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
times = ["09:00-11:00", "11:00-13:00", "13:00-15:00", "15:00-17:00"]
time_slots = []
for i in days:
    for j in times:
        weekday_time_list = []
        weekday_time_list.append(i)
        weekday_time_list.append(j)
        time_slots.append(weekday_time_list)

# course data
course_data_E = {}
course_data_lectures = {}
course_data_tutorials = {}
course_data_practica = {}

with open('Courses.csv', newline = '') as f:
    reader = csv.reader(f)
    next(reader)
    for element in list(reader):
        course_data_E[element[0]] = int(element[len(element) - 1])
        course_data_lectures[element[0]] = int(element[1])
        course_data_tutorials[element[0]] = int(element[2])
        course_data_practica[element[0]] = int(element[4])

class Room:
    def __init__(self, number, max_capacity):
        self.number = number
        self.max_capacity = max_capacity

    def get_number(self):
        return self.number

    def get_max_capacity(self):
        return self.max_capacity

    def has_space(self, E_students):
        if E_students <= self.max_capacity:
            return True
        else:
            return False

class Time:
    def __init__(self, day, time):
        self.day = day
        self.time = time

    def get_day(self):
        return self.day

    def get_time(self):
        return self.time

class Course:
    def __init__(self, name, E_students, number_of_lectures, number_of_tutorials, number_of_practica):
        self.name = name
        self.E_students = E_students
        self.number_of_lectures = number_of_lectures
        self.number_of_tutorials = number_of_tutorials
        self.number_of_practica = number_of_practica

    def get_name(self):
        return self.name

    def get_E_students(self):
        return self.E_students

    def get_number_of_lectures(self):
        return self.number_of_lectures

    def get_number_of_tutorials(self):
        return self.number_of_tutorials

    def get_number_of_practica(self):
        return self.number_of_practica

class Data:
    def __init__(self):
        self.rooms = []
        self.time_and_day = []
        self.courses = []

        keys_list = list(rooms_data.keys())

        for i in range(0, len(rooms_data)):
            self.rooms.append(Room(keys_list[i], rooms_data[keys_list[i]]))

        for i in range(0, len(time_slots)):
            self.time_and_day.append(Time(time_slots[i][0], time_slots[i][1]))   

        keys_list = list(course_data_E.keys())

        for i in range(len(course_data_E)):
            self.courses.append(Course(keys_list[i], course_data_E[keys_list[i]], course_data_lectures[keys_list[i]], course_data_tutorials[keys_list[i]], course_data_practica[keys_list[i]]))

    def get_rooms(self):
        return self.rooms

    def get_time_and_day(self):
        return self.time_and_day

    def get_courses(self):
        return self.courses

data = Data()

days = []
times = []
courses = []

r = random.sample(range(len(data.get_time_and_day())), 20)

for i in r:
    days.append(data.get_time_and_day()[i].get_day())
    times.append(data.get_time_and_day()[i].get_time())
    courses.append(data.get_courses()[i].get_name())

rooster = pd.DataFrame({'Day': days, 'Time': times, 'Course': courses})

print(rooster)

