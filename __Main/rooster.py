import csv
import random
import math as math

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
course_data = {}

with open('Courses.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for element in list(reader):
        #Naam - 0#Hoorcolleges,#Werkcolleges,Max. stud.,#Practica,Max. stud.,E(studenten)
        # we have a dict with name of course as key, and number of students lecture_count, tutorial_count, tut_max and practica_count and prac,maxin a list
        if int(element[2])== 0:
            if int(element[4]) == 0:
                course_data[element[0]] = [int(element[-1]),int(element[1]),int(element[2]),0,int(element[4]),0]
            else:
                course_data[element[0]] = [int(element[-1]),int(element[1]),int(element[2]),0,int(element[4]),int(element[5])]
        elif int(element[4]) == 0:
            if int(element[2])== 0:
                course_data[element[0]] = [int(element[-1]),int(element[1]),int(element[2]),0,int(element[4]),0]
            else:
                course_data[element[0]] = [int(element[-1]),int(element[1]),int(element[2]),int(element[3]),int(element[4]),0]
        else:
            course_data[element[0]] = [int(element[-1]),int(element[1]),int(element[2]),int(element[3]),int(element[4]),int(element[5])]
        

print(course_data)

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
    def __init__(self, time, night):
        self.time = time
        self.room_slots = []
        self.night = night
        if night == False:
            for key in rooms_data:
                self.room_slots.append(Room(key,rooms_data[key]))
        else:
            self.room_slots.append(Room("C0.110", 117))
        

    def room_list(self):
        return self.room_slots

class Day:
    def __init__(self, day):
        self.day = day
        self.time_slots = []

        for i in range(4):
            self.time_slots.append(Time(i, False))

        self.time_slots.append(Time(i, True))

    def timeslot_list(self):
        return self.time_slots 

class Week:
    def __init__(self):
        self.schoolweek = []

        for i in range(5):
            self.schoolweek.append(Day(i))

    def day_list(self):
        return self.schoolweek
        
    def weekprint(self):
        for k in self.schoolweek:
            print(k.day)
            for i in k.timeslot_list():
                print(i.time)
                for p in i.room_list():
                    print(p.number)

    # def small_change (stdent wisselen) eventuele method

week_data = Week()

week_data.weekprint()



class Activity:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity


class Course:
    def __init__(self, name, E_students, number_of_lectures, number_of_tutorials, capacity_tutorial, number_of_practica, capacity_practica):
        self.name = name
        self.E_students = E_students
        self.number_of_lectures = number_of_lectures
        self.number_of_tutorials = number_of_tutorials
        self.number_of_practica = number_of_practica
        self.capacity_tutorial = capacity_tutorial
        self.capacity_practica = capacity_practica

        if capacity_practica != 0:
            self.absolute_nr_practica = math.ceil(E_students/capacity_practica)*number_of_practica
        else:
            self.absolute_nr_practica= 0
        if capacity_tutorial != 0:
            self.absolute_nr_tutorial = math.ceil(E_students/capacity_tutorial)*number_of_tutorials
        else:
            self.absolute_nr_tutorial=0
        self.total_number_of_activities = number_of_lectures+ self.absolute_nr_practica  + self.absolute_nr_tutorial
        self.activity_list = []

        self.activity_list.append(Activity(name, "lecture", E_students ))

        for i in range(int(self.absolute_nr_practica)):
            self.activity_list.append(Activity(name, "practica",capacity_practica ))

        for i in range(int(self.absolute_nr_tutorial)):
            self.activity_list.append(Activity(name, "tutorial",capacity_tutorial ))

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

    def get_total_activities(self):
        return self.total_number_of_activities

    def get_activity_list(self):
        return self.activity_list

        #Naam - 0#Hoorcolleges,#Werkcolleges,Max. stud.,#Practica,Max. stud.,E(studenten)
        # we have a dict with name of course as key, and number of students lecture_count, tutorial_count, tut_max and practica_count and prac,maxin a list
        #name, E_students, number_of_lectures, number_of_tutorials, number_of_practica, capacity_tutorial, capacity_practica)


courses_list = []

for key in course_data:
    courses_list.append(Course(key, course_data[key][0], course_data[key][1], course_data[key][2], course_data[key][3], course_data[key][4], course_data[key][5]))

total_activity = 0
for i in courses_list:
    for k in i.get_activity_list():
        print(k.name)
        print(k.type)
        print(k.capacity)
        total_activity +=1

print("total activities")
print(total_activity)

    
# for k in week_data.day_list():
#     print(k.day)
#     for i in k.timeslot_list():
#         print(i.time)
#         for p in i.room_list():
#             print(p.number)
