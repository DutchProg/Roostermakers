from data_loader import get_student_data

import schedule

student_data = get_student_data()

days = {"Monday": {"09:00-11:00": "none", "11:00-13:00": "none", "13:00-15:00": "none", "15:00-17:00": "none", "17:00-19:00": "none"}, 
        "Tuesday": {"09:00-11:00": "none", "11:00-13:00": "none", "13:00-15:00": "none", "15:00-17:00": "none", "17:00-19:00": "none"},
        "Wednesday": {"09:00-11:00": "none", "11:00-13:00": "none", "13:00-15:00": "none", "15:00-17:00": "none", "17:00-19:00": "none"},
        "Thursday": {"09:00-11:00": "none", "11:00-13:00": "none", "13:00-15:00": "none", "15:00-17:00": "none", "17:00-19:00": "none"},
        "Friday": {"09:00-11:00": "none", "11:00-13:00": "none", "13:00-15:00": "none", "15:00-17:00": "none", "17:00-19:00": "none"}}  
    
class Student:
    def __init__(self, student_number, name, courses):
        self.student_number = student_number
        self.name = name
        self.courses = courses
        self.activities = []

    def get_name(self):
        return self.name

    def get_student_number(self):
        return self.student_number

    def get_courses(self):
        return self.courses
    
    def add_activity(self, activity):
        self.activities.append(activity)

    def print_activities(self):
        
        # print(student_data)

        # for i in student_data[0].activities[0].day + . time
        # days

        # print(student_data)


        for i in student_data[0].activities:

            print(student_data)

            print(student_data[0].activities[0].day)

            print(student_data[0].activities[0].time)   

    # days[student_data[0].activities[0].day][student_data[0].activities[0].time] = student_data[0].activities[0].name

        # 
        # print(self.name)    
        # week = schedule.Week()

        # for day in week.day_list():
        #     print(day.day)
        
        #     for time in day.time_slots: 
        #         print(time.time)

        #         for activity in self.activities:
        #             # print("!")
        #             # print(activity.day)
        #             # print("!")
        #             # print(day.day)
        #             if day.day == activity.day:
        #                 if time.time == activity.time:
        #                     print(activity.name)
        #                     print(activity.room)
        #                 else:
        #                     print('empty')

        # print(self.activities)
        # for activity in self.activities:
        #     print(activity.time)
        #     print(activity.name)


def get_students():
    students_list = [] 

    for key in student_data:
        first_name = student_data[key][0]
        last_name = student_data[key][1]
        
        courses = []
        for i in range(2, 7):
            if (student_data[key][i]) != '':
                courses.append(student_data[key][i])

        students_list.append(Student(key, first_name + " " +last_name, courses))

    return students_list
