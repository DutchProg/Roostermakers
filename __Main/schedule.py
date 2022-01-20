import csv
import random
import math as math

# room data
rooms_data = {"A1.04": 41, "A1.06": 22, "A1.08": 20, "A1.10": 56, "B0.201": 48, "C0.110": 117, "C1.112": 60}

# day and time data
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
times = ["09:00-11:00", "11:00-13:00", "13:00-15:00", "15:00-17:00"]
time_slots = []

class Room:
    def __init__(self, number, max_capacity, night):
        self.number = number
        self.max_capacity = max_capacity
        self.flag = False
        self.scheduled_activity = ["empty"]
        self.night = night

    def get_number(self):
        return self.number

    def add_activity(self, activity):
        self.scheduled_activity[0] = activity
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
    
    def is_night(self):
        return self.night

class Time:
    def __init__(self, time, night):
        self.time = time
        self.room_slots = []
        self.night = night
        if night == False:
            for key in rooms_data:
                self.room_slots.append(Room(key,rooms_data[key],False))
        else:
            self.room_slots.append(Room("C0.110", 117,True))
        

    def room_list(self):
        return self.room_slots

class Day:
    def __init__(self, day):
        self.day = day
        self.time_slots = []

        for i in times:
            self.time_slots.append(Time(i, False))

        self.time_slots.append(Time("17:00-19:00", True))

    def timeslot_list(self):
        return self.time_slots 

class Week:
    def __init__(self):
        self.schoolweek = []

        for i in days:
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