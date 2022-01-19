import csv
import random

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

with open('Courses.csv') as f:
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
        self.flag = False
        self.scheduled_activity = []
    def get_number(self):
        return self.number

    def add_activity(self, activity):
        self.scheduled_activity.append(activity)
        self.flag = True

    def get_max_capacity(self):
        return self.max_capacity

    def has_space(self, E_students):
        if E_students <= self.max_capacity:
            return True
        else:
            return False

    def occupied(self):
        return self.flag
    
    

class Time:
    def __init__(self, time):
        self.time = time
        self.room_slots = []
        for key in rooms_data:
            self.room_slots.append(Room(key,rooms_data[key]))

    def room_list(self):
        return self.room_slots

class Day:
    def __init__(self, day):
        self.day = day
        self.time_slots = []

        for i in range(5):
            self.time_slots.append(Time(i))
    
    def timeslot_list(self):
        return self.time_slots 

class Week:
    def __init__(self):
        self.schoolweek = []

        for i in range(5):
            self.schoolweek.append(Day(i))

    def day_list(self):
        return self.schoolweek

week_data = Week()

for k in week_data.day_list():
    print(k.day)
    for i in k.timeslot_list():
        print(i.time)
        for p in i.room_list():
            print(p.number)

class Activity:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity


class Course:
    def __init__(self, name, E_students, number_of_lectures, number_of_tutorials, number_of_practica):
        self.name = name
        self.E_students = E_students
        self.number_of_lectures = number_of_lectures
        self.number_of_tutorials = number_of_tutorials
        self.number_of_practica = number_of_practica
        self.absolute_nr_practica = 0
        self.absolute_nr_tutorial = 0

        def calc_absolute_nr_practica:
            absolute_nr_practica = 

        def calc_absolute_nr_tutorial:

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